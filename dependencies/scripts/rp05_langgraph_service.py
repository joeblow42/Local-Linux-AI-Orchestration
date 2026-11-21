#!/usr/bin/env python3
"""Run the RP-05 LangGraph runtime and checkpoint-store readiness endpoint."""

import argparse
from contextlib import closing
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import sqlite3

from langgraph.checkpoint.sqlite import SqliteSaver


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint-db", required=True, type=Path)
    parser.add_argument("--port", type=int, default=8010)
    args = parser.parse_args()
    database = args.checkpoint_db.resolve()

    with SqliteSaver.from_conn_string(str(database)) as saver:
        saver.setup()

    class ReadinessHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path != "/ready":
                self.send_error(404)
                return
            try:
                with closing(sqlite3.connect(f"{database.as_uri()}?mode=ro", uri=True)) as conn:
                    conn.execute("SELECT 1 FROM checkpoints LIMIT 1").fetchone()
            except sqlite3.Error:
                self.send_error(503, "Checkpoint store unavailable")
                return
            body = b'{"status":"ready"}\n'
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    with ThreadingHTTPServer(("127.0.0.1", args.port), ReadinessHandler) as server:
        server.serve_forever()


if __name__ == "__main__":
    main()
