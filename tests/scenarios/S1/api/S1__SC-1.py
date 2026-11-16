# scenario-id: S1/SC-1
"""GET /health antwortet mit HTTP 200 und Body ready."""
import json
import os
import urllib.request

base = os.environ["ASB_SVC_WEB_URL"].rstrip("/")
url = f"{base}/health"

with urllib.request.urlopen(url) as resp:
    status = resp.status
    body = resp.read().decode("utf-8")

print(json.dumps({"status": status, "body": body}))
