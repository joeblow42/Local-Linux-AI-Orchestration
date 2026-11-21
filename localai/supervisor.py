"""Release 1 loopback task supervisor for the trusted Open WebUI Pipe."""

import argparse
from contextlib import closing, contextmanager
from hmac import compare_digest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import sqlite3
from threading import Event, Thread
from time import monotonic, time
from typing import TypedDict
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener
from uuid import uuid4

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph

from delivery import WebUIDelivery

IDENTITY = re.compile(r"[A-Za-z0-9_-]{1,128}")
TASK_PATH = re.compile(r"/tasks/([0-9a-f]{32})(/cancel)?")
DIAGNOSTIC_RETENTION_SECONDS = 30 * 24 * 60 * 60


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class TaskState(TypedDict, total=False):
    prompt: str
    analysis: str
    review: str
    result: str


class Cancelled(Exception):
    pass


class Supervisor:
    def __init__(self, database, gateway_key, webui_key, model):
        self.database = database
        self.gateway_key = gateway_key
        self.model = model
        self.wake = Event()
        self.opener = build_opener(ProxyHandler({}), NoRedirect())
        self.delivery = WebUIDelivery(self.opener, webui_key)
        with self.connect() as db:
            db.execute(
                """CREATE TABLE IF NOT EXISTS localai_tasks (
                       id TEXT PRIMARY KEY, actor TEXT NOT NULL, chat TEXT NOT NULL,
                       message TEXT NOT NULL, parent TEXT NOT NULL, prompt TEXT NOT NULL,
                       state TEXT NOT NULL, result TEXT,
                       UNIQUE (actor, chat, message)
                   )"""
            )
            db.execute(
                """CREATE TABLE IF NOT EXISTS localai_delivery (
                       task_id TEXT PRIMARY KEY, state TEXT NOT NULL,
                       attempts INTEGER NOT NULL, next_attempt REAL NOT NULL
                   )"""
            )
            db.execute(
                """CREATE TABLE IF NOT EXISTS localai_inference_metadata (
                       observed_at INTEGER NOT NULL, task_id TEXT NOT NULL,
                       stage TEXT NOT NULL, outcome TEXT NOT NULL, elapsed_ms INTEGER NOT NULL,
                       prompt_tokens INTEGER, completion_tokens INTEGER
                   )"""
            )
            db.execute(
                """CREATE INDEX IF NOT EXISTS localai_inference_metadata_time
                   ON localai_inference_metadata (observed_at)"""
            )
        with SqliteSaver.from_conn_string(str(database)) as saver:
            saver.setup()

    @contextmanager
    def connect(self):
        with closing(sqlite3.connect(self.database, timeout=15)) as db, db:
            db.row_factory = sqlite3.Row
            yield db

    def submit(self, fields):
        actor, chat, message, parent, prompt = fields
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            db.execute(
                """INSERT INTO localai_tasks VALUES (?, ?, ?, ?, ?, ?, 'queued', NULL)
                   ON CONFLICT(actor, chat, message) DO NOTHING""",
                (uuid4().hex, actor, chat, message, parent, prompt),
            )
            row = db.execute(
                "SELECT * FROM localai_tasks WHERE actor=? AND chat=? AND message=?",
                (actor, chat, message),
            ).fetchone()
            if row["parent"] != parent or row["prompt"] != prompt:
                raise ValueError("Conflicting retry for this assistant message")
        self.wake.set()
        return {"id": row["id"], "state": row["state"]}

    def status(self, task_id, actor, cancel):
        with self.connect() as db:
            if cancel:
                db.execute(
                    """UPDATE localai_tasks SET state=CASE state
                       WHEN 'queued' THEN 'cancelled' ELSE 'cancelling' END
                       WHERE id=? AND actor=? AND state IN ('queued', 'running')""",
                    (task_id, actor),
                )
            row = db.execute(
                """SELECT t.id, t.state, t.result, d.state AS delivery
                   FROM localai_tasks AS t LEFT JOIN localai_delivery AS d ON t.id=d.task_id
                   WHERE t.id=? AND t.actor=?""",
                (task_id, actor),
            ).fetchone()
        return dict(row) if row else None

    def purge_metadata(self, now):
        with self.connect() as db:
            return db.execute(
                "DELETE FROM localai_inference_metadata WHERE observed_at < ?",
                (now - DIAGNOSTIC_RETENTION_SECONDS,),
            ).rowcount

    def record_inference(self, task_id, stage, outcome, elapsed_ms, usage):
        def observed_count(key):
            count = usage.get(key)
            return count if type(count) is int and count >= 0 else None

        with self.connect() as db:
            db.execute(
                "INSERT INTO localai_inference_metadata VALUES (?, ?, ?, ?, ?, ?, ?)",
                (int(time()), task_id, stage, outcome, elapsed_ms,
                 observed_count("prompt_tokens"), observed_count("completion_tokens")),
            )

    def infer(self, task_id, stage, role, text, limit):
        # This read is the admission point for a specialist. Cancellation
        # prevents admission to later nodes, while an admitted call can finish.
        with self.connect() as db:
            state = db.execute("SELECT state FROM localai_tasks WHERE id=?", (task_id,)).fetchone()
            if state["state"] != "running":
                raise Cancelled
        payload = {
            "model": self.model,
            "messages": [{"role": "system", "content": role}, {"role": "user", "content": text}],
            "max_tokens": limit,
            "temperature": 0,
        }
        req = Request(
            "http://127.0.0.1:8080/v1/chat/completions",
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json", "x-bf-vk": self.gateway_key},
        )
        started = monotonic()
        outcome = "failed"
        usage = {}
        try:
            with self.opener.open(req, timeout=90) as response:
                data = json.load(response)
            if not isinstance(data, dict):
                raise ValueError("Invalid local model response")
            if isinstance(data.get("usage"), dict):
                usage = data["usage"]
            content = data["choices"][0]["message"]["content"]
            if not isinstance(content, str) or not content.strip():
                raise ValueError("Empty local model response")
            outcome = "completed"
            return content.strip()
        finally:
            self.record_inference(task_id, stage, outcome, round((monotonic() - started) * 1000), usage)

    def execute(self, task):
        task_id = task["id"]
        cfg = {"configurable": {"thread_id": task_id}}
        with SqliteSaver.from_conn_string(str(self.database)) as saver:
            graph = StateGraph(TaskState)
            graph.add_node("analysis", lambda state: {"analysis": self.infer(
                task_id, "analysis", "Analyze the user's request and propose a concise solution.",
                state["prompt"], 384,
            )})
            graph.add_node("review", lambda state: {"review": self.infer(
                task_id, "review", "Independently review the proposed solution and identify errors or omissions.",
                f"Request:\n{state['prompt']}\n\nProposal:\n{state['analysis']}", 256,
            )})
            graph.add_node("synthesis", lambda state: {"result": self.infer(
                task_id, "synthesis", "Answer the user's request using the analysis and review. Give only the final answer.",
                f"Request:\n{state['prompt']}\n\nAnalysis:\n{state['analysis']}\n\nReview:\n{state['review']}", 512,
            )})
            graph.add_edge(START, "analysis")
            graph.add_edge("analysis", "review")
            graph.add_edge("review", "synthesis")
            graph.add_edge("synthesis", END)
            app = graph.compile(checkpointer=saver)
            snapshot = app.get_state(cfg)
            if snapshot.values.get("result") and not snapshot.next:
                return snapshot.values["result"]
            start = None if snapshot.next else {"prompt": task["prompt"]}
            return app.invoke(start, cfg)["result"]

    def deliver_pending(self):
        with self.connect() as db:
            task = db.execute(
                """SELECT t.*, d.attempts FROM localai_delivery AS d
                   JOIN localai_tasks AS t ON t.id=d.task_id
                   WHERE d.state='pending' AND d.next_attempt<=?
                   ORDER BY d.next_attempt LIMIT 1""",
                (time(),),
            ).fetchone()
        if not task:
            return
        state = self.delivery.deliver(task)
        attempts = task["attempts"] + 1
        if state == "pending" and attempts >= 40:
            state = "unverified"
        with self.connect() as db:
            db.execute(
                """UPDATE localai_delivery SET state=?, attempts=?, next_attempt=?
                   WHERE task_id=?""",
                (state, attempts, time() + 15, task["id"]),
            )

    def run(self):
        # One worker serializes local tasks and avoids competing model requests.
        next_purge = 0
        while True:
            self.wake.clear()
            if time() >= next_purge:
                self.purge_metadata(int(time()))
                next_purge = time() + 3600
            self.deliver_pending()
            with self.connect() as db:
                db.execute("BEGIN IMMEDIATE")
                db.execute("UPDATE localai_tasks SET state='cancelled' WHERE state='cancelling'")
                task = db.execute(
                    "SELECT * FROM localai_tasks WHERE state IN ('queued','running') ORDER BY rowid LIMIT 1"
                ).fetchone()
                if task:
                    db.execute("UPDATE localai_tasks SET state='running' WHERE id=?", (task["id"],))
            if not task:
                self.wake.wait(5)
                continue
            state, result = "completed", None
            try:
                result = self.execute(task)
            except Cancelled:
                state = "cancelled"
            except (OSError, KeyError, IndexError, TypeError, ValueError):
                state = "failed"
            with self.connect() as db:
                db.execute(
                    """UPDATE localai_tasks SET
                       result=CASE WHEN state='cancelling' THEN NULL ELSE ? END,
                       state=CASE WHEN state='cancelling' THEN 'cancelled' ELSE ? END
                       WHERE id=?""",
                    (result, state, task["id"]),
                )
                db.execute(
                    """INSERT INTO localai_delivery (task_id, state, attempts, next_attempt)
                       SELECT id, 'pending', 0, 0 FROM localai_tasks
                       WHERE id=? AND state='completed'
                       ON CONFLICT(task_id) DO NOTHING""",
                    (task["id"],),
                )


def handler_for(supervisor, secret):
    class Handler(BaseHTTPRequestHandler):
        def log_request(self, code="-", size="-"):
            # Request paths carry task IDs. Keep only the explicit metadata records.
            pass

        def reply(self, status, payload):
            body = json.dumps(payload).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def actor(self):
            bearer = self.headers.get("Authorization", "").encode()
            actor = self.headers.get("X-LocalAI-Actor", "")
            if not compare_digest(bearer, b"Bearer " + secret) or not IDENTITY.fullmatch(actor):
                self.reply(401, {"error": "Unauthorized"})
                return None
            return actor

        def do_GET(self):
            if self.path == "/ready":
                with supervisor.connect() as db:
                    db.execute("SELECT 1 FROM localai_tasks LIMIT 1").fetchone()
                self.reply(200, {"status": "ready"})
                return
            match = TASK_PATH.fullmatch(self.path)
            if not match or match[2]:
                self.reply(404, {"error": "Not found"})
                return
            if actor := self.actor():
                self.send_task(match[1], actor, False)

        def send_task(self, task_id, actor, cancel):
            task = supervisor.status(task_id, actor, cancel)
            self.reply(200 if task else 404, task or {"error": "Task not found"})

        def do_POST(self):
            match = TASK_PATH.fullmatch(self.path)
            if self.path != "/tasks" and (not match or not match[2]):
                self.reply(404, {"error": "Not found"})
                return
            if not (actor := self.actor()):
                return
            if match:
                self.send_task(match[1], actor, True)
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 16_384:
                    raise ValueError
                body = json.loads(self.rfile.read(length))
                chat, message, parent = (body[key] for key in ("chat", "message", "parent"))
                prompt = body["prompt"]
                if not all(isinstance(value, str) and IDENTITY.fullmatch(value)
                           for value in (chat, message, parent)):
                    raise ValueError
                if not isinstance(prompt, str) or not prompt.strip() or len(prompt) > 3000:
                    raise ValueError
            except (ValueError, KeyError, TypeError):
                self.reply(400, {"error": "Invalid saved chat, message, or prompt"})
                return
            try:
                task = supervisor.submit((actor, chat, message, parent, prompt))
            except ValueError:
                self.reply(409, {"error": "Conflicting submission"})
                return
            self.reply(202, task)

    return Handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint-db", required=True, type=Path)
    parser.add_argument("--gateway-key-file", required=True, type=Path)
    parser.add_argument("--pipe-key-file", required=True, type=Path)
    parser.add_argument("--webui-key-file", required=True, type=Path)
    parser.add_argument("--model", required=True)
    parser.add_argument("--port", type=int, default=8010)
    args = parser.parse_args()
    gateway_key = args.gateway_key_file.read_text().strip()
    pipe_key = args.pipe_key_file.read_bytes().strip()
    webui_key = args.webui_key_file.read_text().strip()
    if not args.model.startswith("ollama/") or not all((gateway_key, pipe_key, webui_key)):
        parser.error("An Ollama model and all three local credentials are required")
    supervisor = Supervisor(args.checkpoint_db, gateway_key, webui_key, args.model)
    with ThreadingHTTPServer(("127.0.0.1", args.port), handler_for(supervisor, pipe_key)) as server:
        Thread(target=supervisor.run, daemon=True).start()
        server.serve_forever()


if __name__ == "__main__":
    main()
