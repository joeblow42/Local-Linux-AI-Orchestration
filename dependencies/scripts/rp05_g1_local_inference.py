#!/usr/bin/env python3
"""Single existing-G1 Bifrost->local Ollama inference witness. No key persistence."""
import argparse
import getpass
import json
import sys
import urllib.error
import urllib.request

OLLAMA = 'http://127.0.0.1:11434'
GATEWAY = 'http://127.0.0.1:8080'

def call(url, payload=None, secret=None):
    headers = {'Content-Type': 'application/json'}
    if secret:
        headers['x-bf-vk'] = secret
    req = urllib.request.Request(
        url, headers=headers,
        data=(json.dumps(payload).encode() if payload is not None else None))
    with urllib.request.urlopen(req, timeout=120 if payload is not None else 6) as res:
        return json.load(res)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--model', required=True, help='Exact local Ollama model tag, optionally prefixed ollama/')
    args = p.parse_args()
    try:
        tags = {m.get('name') for m in call(OLLAMA + '/api/tags').get('models', [])}
    except (OSError, ValueError, urllib.error.URLError):
        print('INFERENCE_RESULT=LOCAL_OLLAMA_TAGS_UNAVAILABLE', file=sys.stderr)
        return 1
    if args.model.removeprefix('ollama/') not in tags:
        print('STOP: requested model is not in local Ollama tags', file=sys.stderr)
        return 2
    secret = getpass.getpass('Existing Bifrost virtual key (hidden; never saved): ')
    if not secret:
        print('STOP: no key provided', file=sys.stderr)
        return 2
    try:
        result = call(GATEWAY + '/v1/chat/completions', {
            'model': args.model, 'messages': [{'role':'user','content':'Reply with the word READY.'}],
            'stream': False, 'max_tokens': 32, 'temperature': 0
        }, secret)
    except urllib.error.HTTPError as exc:
        print(f'INFERENCE_RESULT=HTTP_{exc.code}_FAIL', file=sys.stderr)
        return 1
    except (OSError, ValueError, urllib.error.URLError):
        print('INFERENCE_RESULT=TRANSPORT_OR_JSON_FAILURE', file=sys.stderr)
        return 1
    choices = result.get('choices', [])
    content = choices[0].get('message', {}).get('content') if choices else None
    if not isinstance(content, str) or not content.strip():
        print('INFERENCE_RESULT=EMPTY_OR_MISSING_ASSISTANT_REPLY', file=sys.stderr)
        return 1
    print('INFERENCE_RESULT=SUCCESS_NONEMPTY_LOCAL_MODEL_RESPONSE')
    print('INFERENCE_MODEL_REQUESTED=' + args.model)
    print('INFERENCE_RESPONSE_CONTENT=REDACTED')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
