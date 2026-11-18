"""Synthetic local HTTP/SQLite protocol checks; NOT a real Open WebUI test."""
import json
import os
import sqlite3
import tempfile
import threading
import unittest
from contextlib import closing
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

from if02_delivery_client_candidate import CandidateDeliveryClient


class Store:
    def __init__(self, path):
        self.path = path
        self.lock = threading.Lock()
        self.fail_before = False
        self.reply_lost_after = False
        self.delete_just_before_write = False
        self.post_count = 0
        self.force_redirect = False
        with closing(sqlite3.connect(path)) as db:
            db.execute("CREATE TABLE chats (id TEXT PRIMARY KEY, data TEXT NOT NULL)")
            db.execute("INSERT INTO chats VALUES (?,?)", ("c1", json.dumps({"history": {"messages": {
                "u1": {"id": "u1", "role": "user", "content": "request"},
                "a1": {"id": "a1", "role": "assistant", "parentId": "u1", "content": "Accepted T-1"}
            }}})))
            db.commit()

    def get_chat(self):
        with self.lock, closing(sqlite3.connect(self.path)) as db:
            row = db.execute("SELECT data FROM chats WHERE id='c1'").fetchone()
            return json.loads(row[0]) if row else None

    def mutate(self, fn):
        with self.lock, closing(sqlite3.connect(self.path)) as db:
            row = db.execute("SELECT data FROM chats WHERE id='c1'").fetchone()
            if not row:
                return
            chat = json.loads(row[0]); fn(chat)
            db.execute("UPDATE chats SET data=? WHERE id='c1'", (json.dumps(chat),))
            db.commit()


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def _json(self, code, data):
        b = json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        try:
            self.wfile.write(b)
        except BrokenPipeError:
            pass

    def _authorized(self):
        if self.headers.get('Authorization') != 'Bearer fixture-key':
            self._json(401, {"detail": "not authenticated"})
            return False
        return True

    def do_GET(self):
        if self.server.store.force_redirect:
            self.send_response(302)
            self.send_header("Location", "https://example.com/")
            self.end_headers()
            return
        if not self._authorized(): return
        if self.path != "/api/v1/chats/c1":
            return self._json(404, {"detail": "not found"})
        chat = self.server.store.get_chat()
        if not chat:
            return self._json(404, {"detail": "not found"})
        self._json(200, {"id": "c1", "chat": chat})

    def do_POST(self):
        if not self._authorized(): return
        if self.path != "/api/v1/chats/c1/messages/a1":
            return self._json(404, {"detail": "not found"})
        if self.server.store.fail_before:
            return self._json(503, {"detail": "outage"})
        try:
            content = json.loads(self.rfile.read(int(self.headers['Content-Length'])))['content']
        except (ValueError, KeyError):
            return self._json(400, {})
        self.server.store.post_count += 1
        def apply(chat):
            messages = chat['history']['messages']
            if self.server.store.delete_just_before_write:
                messages.pop('a1', None)
            if 'a1' not in messages:
                # Synthetic behavior faithfully mimics source upsert's *risk*,
                # not Open WebUI's full implementation.
                messages['a1'] = {'id':'a1','role':'assistant','parentId':None}
            messages['a1']['content'] = content
        self.server.store.mutate(apply)
        if self.server.store.reply_lost_after:
            return self._json(503, {"detail": "reply lost after commit"})
        self._json(200, {"id": "c1", "chat": self.server.store.get_chat()})


class TestDelivery(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory(prefix="if02-http-fixture-")
        self.store = Store(os.path.join(self.dir.name, 'webui.sqlite3'))
        self.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        self.server.store = self.store
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.client = CandidateDeliveryClient('http://127.0.0.1:%d' % self.server.server_address[1], 'fixture-key')
        self.kwargs = dict(chat_id="c1",message_id="a1",expected_parent_id="u1",
                           original_acknowledgement="Accepted T-1",final_content="The task has completed.")

    def tearDown(self):
        self.server.shutdown(); self.server.server_close(); self.thread.join(timeout=3); self.dir.cleanup()

    def test_real_http_sqlite_persisted_delivery(self):
        self.assertEqual(self.client.deliver(**self.kwargs).code, 'DELIVERED')
        self.assertEqual(self.store.get_chat()['history']['messages']['a1']['content'], self.kwargs['final_content'])

    def test_repeat_same_content_is_idempotent(self):
        self.assertEqual(self.client.deliver(**self.kwargs).code, 'DELIVERED')
        self.assertEqual(self.client.deliver(**self.kwargs).code, 'ALREADY_PRESENT')
        self.assertEqual(self.store.post_count, 1)

    def test_original_placeholder_modified_refuses_write(self):
        self.store.mutate(lambda chat: chat['history']['messages']['a1'].update(content='Operator edited'))
        self.assertEqual(self.client.deliver(**self.kwargs).reason,'slot_modified_since_acceptance')
        self.assertEqual(self.store.post_count, 0)

    def test_missing_placeholder_refuses_write(self):
        self.store.mutate(lambda chat: chat['history']['messages'].pop('a1'))
        self.assertEqual(self.client.deliver(**self.kwargs).reason,'original_slot_missing_or_changed')
        self.assertEqual(self.store.post_count, 0)

    def test_parent_mismatch_refuses_write(self):
        self.store.mutate(lambda chat: chat['history']['messages']['a1'].update(parentId='u2'))
        self.assertEqual(self.client.deliver(**self.kwargs).code,'REFUSED')
        self.assertEqual(self.store.post_count, 0)

    def test_wrong_key_does_not_write(self):
        other = CandidateDeliveryClient('http://127.0.0.1:%d' % self.server.server_address[1], 'wrong-key')
        self.assertEqual(other.deliver(**self.kwargs).code, 'PENDING')
        self.assertEqual(self.store.post_count,0)

    def test_unavailable_write_does_not_erase_result(self):
        self.store.fail_before = True
        self.assertEqual(self.client.deliver(**self.kwargs).code, 'PENDING')
        self.assertEqual(self.store.post_count,0)
        self.store.fail_before = False
        self.assertEqual(self.client.deliver(**self.kwargs).code, 'DELIVERED')

    def test_lost_response_after_committed_write_retry(self):
        self.store.reply_lost_after = True
        self.assertEqual(self.client.deliver(**self.kwargs).code, 'PENDING')
        self.assertEqual(self.store.post_count,1)
        self.store.reply_lost_after = False
        self.assertEqual(self.client.deliver(**self.kwargs).code, 'ALREADY_PRESENT')
        self.assertEqual(self.store.post_count,1)

    def test_delete_during_write_exposes_source_upsert_race(self):
        self.store.delete_just_before_write = True
        result = self.client.deliver(**self.kwargs)
        # The client detects post-write mismatch; the upstream-style upsert
        # nevertheless recreated a message, so strict atomic safety is UNPROVEN.
        self.assertEqual((result.code,result.reason),('PENDING','postwrite_readback_mismatch'))
        recreated = self.store.get_chat()['history']['messages']['a1']
        self.assertEqual(recreated['content'], self.kwargs['final_content'])
        self.assertIsNone(recreated['parentId'])

    def test_non_loopback_refused(self):
        with self.assertRaisesRegex(ValueError,'isolated_numeric_loopback_required'):
            CandidateDeliveryClient('http://example.com:8888', 'fixture-key')

    def test_no_redirects(self):
        self.store.force_redirect = True
        self.assertEqual(self.client.deliver(**self.kwargs).code, "PENDING")
        self.assertEqual(self.store.post_count, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
