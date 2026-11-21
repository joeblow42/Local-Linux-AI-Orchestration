"""
title: Local AI Delegated Task
description: Submit a saved chat turn to the Local AI supervisor or control a task by ID.
version: 0.1.0
"""

import asyncio
import json
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

from pydantic import BaseModel


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Pipe:
    class Valves(BaseModel):
        PIPE_KEY_FILE: str = ""

    def __init__(self):
        self.valves = self.Valves()

    def request(self, actor, route, payload=None):
        key = Path(self.valves.PIPE_KEY_FILE).read_text().strip()
        request = Request(
            "http://127.0.0.1:8010" + route,
            data=None if payload is None else json.dumps(payload).encode(),
            headers={
                "Authorization": "Bearer " + key,
                "X-LocalAI-Actor": actor,
                "Content-Type": "application/json",
            },
        )
        opener = build_opener(ProxyHandler({}), NoRedirect())
        with opener.open(request, timeout=8) as response:
            return json.load(response)

    async def pipe(self, body: dict, __user__: dict, __metadata__: dict):
        if __metadata__.get("task"):
            # Title, tags, and follow-up generation are not operator requests.
            return ""
        if not __user__.get("id"):
            return "Sign in to submit or control a delegated task."
        messages = body.get("messages", [])
        last = messages[-1] if messages else {}
        content = last.get("content")
        if last.get("role") != "user" or not isinstance(content, str) or not content.strip():
            return "Enter a text request in a saved chat."
        prompt = content.strip()
        command = re.fullmatch(r"task (status|cancel) ([0-9a-f]{32})", prompt)
        try:
            if command:
                action, task_id = command.groups()
                suffix = "/cancel" if action == "cancel" else ""
                payload = {} if action == "cancel" else None
                task = await asyncio.to_thread(
                    self.request, __user__["id"], f"/tasks/{task_id}{suffix}", payload
                )
                summary = f"Task `{task['id']}`: {task['state']}."
                if task.get("delivery"):
                    summary += f" Automatic delivery: {task['delivery']}."
                return f"{summary}\n\n{task['result']}" if task.get("result") else summary
            if prompt.startswith(("task status", "task cancel")):
                return "Use `task status <task-id>` or `task cancel <task-id>`."
            identifiers = {
                "chat": __metadata__.get("chat_id"),
                "message": __metadata__.get("message_id"),
                "parent": __metadata__.get("user_message_id"),
            }
            if not all(identifiers.values()):
                return "Start a saved chat to submit a delegated task."
            task = await asyncio.to_thread(
                self.request, __user__["id"], "/tasks", {**identifiers, "prompt": prompt}
            )
            return f"Delegated task accepted: `{task['id']}`."
        except HTTPError as exc:
            return f"The supervisor rejected the request (HTTP {exc.code})."
        except (OSError, ValueError, URLError):
            return "The supervisor is unavailable or its credential is not configured."
