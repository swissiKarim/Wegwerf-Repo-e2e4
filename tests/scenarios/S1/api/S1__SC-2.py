# scenario-id: S1/SC-2
"""GET /health liefert keinen Fehler-Statuscode."""
import json
import os
import urllib.request

base = os.environ["ASB_SVC_WEB_URL"].rstrip("/")
url = f"{base}/health"

with urllib.request.urlopen(url) as resp:
    status = resp.status
    body = resp.read().decode("utf-8")

print(json.dumps({"status": status, "body": body}))
