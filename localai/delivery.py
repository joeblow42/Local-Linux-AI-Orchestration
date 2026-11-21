"""Best-effort delivery to the existing Open WebUI acknowledgement."""

import json
from urllib.error import HTTPError
from urllib.request import Request


class WebUIDelivery:
    def __init__(self, opener, key):
        self.opener = opener
        self.key = key

    def request(self, path, payload=None):
        body = None if payload is None else json.dumps(payload).encode()
        req = Request(
            "http://127.0.0.1:3000/api/v1/chats/" + path,
            data=body,
            headers={"Authorization": "Bearer " + self.key, "Content-Type": "application/json"},
        )
        with self.opener.open(req, timeout=5) as response:
            data = response.read(8 * 1024 * 1024 + 1)
            if len(data) > 8 * 1024 * 1024:
                raise ValueError("Chat response too large")
            return json.loads(data)

    def slot(self, task):
        response = self.request(task["chat"])
        if response["id"] != task["chat"] or response["user_id"] != task["actor"]:
            return "refused", None
        message = response["chat"]["history"]["messages"].get(task["message"])
        if message is None:
            return "pending", None
        if (message.get("id") != task["message"] or message.get("role") != "assistant"
                or message.get("parentId") != task["parent"]):
            return "refused", None
        if message.get("done") is False:
            return "pending", None
        return "present", message

    @staticmethod
    def updated_output(message, acknowledgement, final):
        output = message.get("output")
        if not output:
            return [{
                "id": "msg_" + message["id"], "type": "message",
                "role": "assistant", "status": "completed",
                "content": [{"type": "output_text", "text": final}],
            }]
        if len(output) != 1 or output[0].get("type") != "message":
            return None
        parts = output[0].get("content", [])
        if (len(parts) != 1 or parts[0].get("type") != "output_text"
                or parts[0].get("text") not in (acknowledgement, final)):
            return None
        return [{**output[0], "content": [{**parts[0], "text": final}]}]

    def deliver(self, task):
        ack = f"Delegated task accepted: `{task['id']}`."
        final = f"{ack}\n\n{task['result']}"
        try:
            state, message = self.slot(task)
            if state != "present":
                return state
            content = message.get("content")
            if not content:
                return "pending"
            if content not in (ack, final):
                return "refused"
            output = self.updated_output(message, ack, final)
            if output is None:
                return "refused"
            if content != final or message.get("output") != output:
                # This API merges history by message ID. FUT-002 tracks the
                # race for the target message between this read and the write.
                updated = {**message, "content": final, "output": output}
                self.request(task["chat"], {"chat": {"history": {"messages": {
                    task["message"]: updated,
                }}}})
            state, persisted = self.slot(task)
            if state != "present" or persisted.get("content") != final or persisted.get("output") != output:
                return "pending"
            # Send the structured output without finishing the browser's
            # already-closed generation a second time.
            noticed = self.request(f"{task['chat']}/messages/{task['message']}/event", {
                "type": "chat:completion", "data": {"output": output},
            })
            return "delivered" if noticed is True else "pending"
        except HTTPError as error:
            return "refused" if error.code in (401, 403) else "pending"
        except (OSError, KeyError, TypeError, ValueError):
            return "pending"
