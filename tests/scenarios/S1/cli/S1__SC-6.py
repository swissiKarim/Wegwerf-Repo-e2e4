# scenario-id: S1/SC-6
import json
import subprocess

result = subprocess.run(
    ["pytest", "--tb=short", "-q"],
    capture_output=True,
    text=True,
)

print(json.dumps({
    "exit_code": result.returncode,
    "stdout": result.stdout,
    "stderr": result.stderr,
}))
