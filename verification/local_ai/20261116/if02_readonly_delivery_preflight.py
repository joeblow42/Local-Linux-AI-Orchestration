#!/usr/bin/env python3
"""Read-only IF-02 isolated-fixture preflight; never creates credentials or edits chats.

Requires a preexisting operator-owned WebUI API key in IF02_WEBUI_API_KEY.
Run only against an explicitly approved isolated localhost fixture, NOT G1.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

LIMIT = 16 * 1024 * 1024
ID = re.compile(r"[A-Za-z0-9._-]{1,128}\Z")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


def fail(code):
    print(json.dumps({"result": "FAIL", "reason": code, "mode": "READ_ONLY"}))
    return 1


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--api-url", required=True, help="Local isolated WebUI URL, e.g. http://127.0.0.1:8080")
    p.add_argument("--chat-id", required=True, help="Existing SAVED WebUI chat ID")
    p.add_argument("--message-id", required=True, help="Existing assistant acknowledgement message ID")
    p.add_argument("--expected-parent-id", help="Optional existing user message ID for correlation")
    p.add_argument("--confirm-isolated-fixture", action="store_true", help="Required opt-in; never run against G1")
    args = p.parse_args(argv)
    if not args.confirm_isolated_fixture:
        return fail("ISOLATED_FIXTURE_CONFIRMATION_REQUIRED")
    ids = [args.chat_id, args.message_id] + ([args.expected_parent_id] if args.expected_parent_id else [])
    if any(ID.fullmatch(i) is None for i in ids):
        return fail("INVALID_ID_FORMAT")
    try:
        u = urllib.parse.urlsplit(args.api_url)
        if (u.scheme not in ("http", "https") or u.hostname not in ("127.0.0.1", "::1")
                or u.username or u.password or u.path not in ("", "/") or u.query or u.fragment):
            return fail("NON_LOOPBACK_OR_INVALID_URL")
        _ = u.port
    except ValueError:
        return fail("INVALID_URL_PORT")
    token = os.environ.get("IF02_WEBUI_API_KEY", "")
    if not token or "\n" in token or "\r" in token:
        return fail("API_KEY_ENV_UNAVAILABLE")
    url = urllib.parse.urlunsplit((u.scheme, u.netloc, "/api/v1/chats/" + urllib.parse.quote(args.chat_id, safe=""), "", ""))
    request = urllib.request.Request(url, headers={"Authorization": "Bearer " + token, "Accept": "application/json"}, method="GET")
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    try:
        with opener.open(request, timeout=8) as response:
            if response.status != 200:
                return fail("UNEXPECTED_HTTP_STATUS")
            body = response.read(LIMIT + 1)
    except urllib.error.HTTPError as exc:
        return fail("HTTP_STATUS_" + str(exc.code))
    except (urllib.error.URLError, TimeoutError, OSError):
        return fail("NETWORK_OR_TLS_ERROR")
    if len(body) > LIMIT:
        return fail("CHAT_RESPONSE_TOO_LARGE")
    try:
        obj = json.loads(body)
        chat = obj.get("chat")
        if not isinstance(chat, dict):
            return fail("CHAT_DATA_UNAVAILABLE")
        history = chat.get("history")
        messages = history.get("messages") if isinstance(history, dict) else None
        if not isinstance(messages, dict):
            return fail("SAVED_MESSAGE_MAP_UNAVAILABLE")
        message = messages.get(args.message_id)
        if not isinstance(message, dict):
            return fail("ACKNOWLEDGEMENT_MESSAGE_NOT_FOUND")
        if message.get("id", args.message_id) != args.message_id or message.get("role") != "assistant":
            return fail("NOT_THE_EXPECTED_ASSISTANT_MESSAGE")
        if args.expected_parent_id and message.get("parentId") != args.expected_parent_id:
            return fail("PARENT_ID_MISMATCH")
    except (TypeError, ValueError, AttributeError):
        return fail("CHAT_RESPONSE_PARSE_ERROR")
    print(json.dumps({"result": "PASS", "mode": "READ_ONLY", "scope": "ISOLATED_LOOPBACK",
                      "chat_access": "VERIFIED", "saved_assistant_message": "VERIFIED",
                      "parent_verified": bool(args.expected_parent_id), "changes": 0}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
