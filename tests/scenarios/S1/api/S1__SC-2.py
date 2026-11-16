# scenario-id: S1/SC-2
import json
import os
import urllib.request

base_url = os.environ.get("ASB_SVC_WEB_URL", os.environ.get("ASB_API_BASE", "http://localhost:8099"))
url = base_url.rstrip("/") + "/health"

with urllib.request.urlopen(url) as resp:
    status = resp.status
    body = resp.read().decode("utf-8")

print(json.dumps({"status": status, "body": body}))
