"""Candidate IF-02 HTTP delivery client for a vetted *isolated* Open WebUI fixture.

No CLI, no credentials or services configured here. Import and invoke explicitly
only within an authorized test fixture; NOT approved as production G-A protocol.
The Open WebUI route is an upsert and cannot prevent concurrent deletion races.
"""
from dataclasses import dataclass
import json
import re
from urllib import error, parse, request

MAX_CHAT_BYTES = 8 * 1024 * 1024
MAX_RESULT_CHARS = 500_000
ID_RE = re.compile(r"[A-Za-z0-9_-]{1,128}\Z")


class _NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


@dataclass(frozen=True)
class DeliveryStatus:
    code: str  # DELIVERED, ALREADY_PRESENT, PENDING, REFUSED
    reason: str = ""


class CandidateDeliveryClient:
    """Full-content replacement to a previously verified, existing assistant slot.

    Authentication is with the operator's own API key. Never persist the key in
    chat/task metadata or print it. This class does NOT perform task ownership
    checking; the independent supervisor must establish task-to-slot mapping.
    """

    def __init__(self, base_url, operator_api_key, *, timeout=5):
        parts = parse.urlsplit(base_url)
        if (parts.scheme not in ("http", "https") or
            parts.hostname not in ("127.0.0.1", "::1") or
            parts.username or parts.password or parts.path not in ("", "/") or
            parts.query or parts.fragment):
            raise ValueError("isolated_numeric_loopback_required")
        _ = parts.port  # Validate the port syntax.
        if not operator_api_key or "\r" in operator_api_key or "\n" in operator_api_key:
            raise ValueError("valid_preexisting_api_key_required")
        self._base = parse.urlunsplit((parts.scheme, parts.netloc, "", "", ""))
        self._key = operator_api_key
        self._timeout = timeout
        self._opener = request.build_opener(request.ProxyHandler({}), _NoRedirect())

    def _http_json(self, url, *, post=None):
        headers = {"Authorization": "Bearer " + self._key, "Accept": "application/json"}
        if post is not None:
            body = json.dumps(post, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
            headers["Content-Type"] = "application/json"
            method = "POST"
        else:
            body, method = None, "GET"
        req = request.Request(url, data=body, headers=headers, method=method)
        with self._opener.open(req, timeout=self._timeout) as response:
            if response.status != 200:
                raise ValueError("unexpected_http_status")
            data = response.read(MAX_CHAT_BYTES + 1)
            if len(data) > MAX_CHAT_BYTES:
                raise ValueError("response_too_large")
            return json.loads(data)

    def _message(self, chat_id, message_id):
        obj = self._http_json(self._base + "/api/v1/chats/" + parse.quote(chat_id, safe=""))
        if not isinstance(obj, dict) or not isinstance(obj.get("chat"), dict):
            raise ValueError("invalid_chat_response")
        history = obj["chat"].get("history")
        messages = history.get("messages") if isinstance(history, dict) else None
        if not isinstance(messages, dict):
            raise ValueError("no_saved_message_map")
        return messages.get(message_id)

    @staticmethod
    def _matches_slot(msg, message_id, expected_parent_id):
        return (isinstance(msg, dict) and msg.get("id") == message_id
                and msg.get("role") == "assistant"
                and msg.get("parentId") == expected_parent_id)

    def deliver(self, *, chat_id, message_id, expected_parent_id,
                original_acknowledgement, final_content):
        """Best-effort idempotent update. NOT an atomic conditional write.

        The supervisor must already have committed the terminal task result and
        the immutable message correlation before calling this method.
        """
        if any(not isinstance(s, str) or not ID_RE.fullmatch(s)
               for s in (chat_id, message_id, expected_parent_id)):
            return DeliveryStatus("REFUSED", "invalid_slot_identity")
        if (not isinstance(original_acknowledgement, str)
            or not original_acknowledgement or not isinstance(final_content, str)
            or not final_content or len(final_content) > MAX_RESULT_CHARS):
            return DeliveryStatus("REFUSED", "invalid_content")
        try:
            msg = self._message(chat_id, message_id)
            if not self._matches_slot(msg, message_id, expected_parent_id):
                return DeliveryStatus("REFUSED", "original_slot_missing_or_changed")
            if msg.get("content") == final_content:
                return DeliveryStatus("ALREADY_PRESENT")
            if msg.get("content") != original_acknowledgement:
                return DeliveryStatus("REFUSED", "slot_modified_since_acceptance")
            url = (self._base + "/api/v1/chats/" + parse.quote(chat_id, safe="")
                   + "/messages/" + parse.quote(message_id, safe=""))
            self._http_json(url, post={"content": final_content})
            persisted = self._message(chat_id, message_id)
            if (self._matches_slot(persisted, message_id, expected_parent_id)
                    and persisted.get("content") == final_content):
                return DeliveryStatus("DELIVERED")
            return DeliveryStatus("PENDING", "postwrite_readback_mismatch")
        except (error.HTTPError, error.URLError, OSError, TimeoutError, ValueError,
                TypeError, UnicodeError):
            # The POST may have been committed even if the response was lost.
            # The supervisor should retry later using the same immutable IDs/content.
            return DeliveryStatus("PENDING", "webui_request_unavailable_or_unverified")
