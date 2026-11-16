# scenario-id: S1/SC-5
import json
import subprocess

result = subprocess.run(
    ["ruff", "check", "."],
    capture_output=True,
    text=True,
)

print(json.dumps({
    "exit_code": result.returncode,
    "stdout": result.stdout,
    "stderr": result.stderr,
}))
