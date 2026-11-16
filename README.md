# Wegwerf-Repo-e2e4

Lokaler Seed für den bezahlten E2E-4-Lauf (Demo-Webapp, stdlib only).

## Lokal

```bash
python app.py          # http://127.0.0.1:8099/  health: /health
pytest -q
ruff check .
```

Kein `.agentsphere/` im Seed — der Env-Agent soll den Vertrag ableiten.
