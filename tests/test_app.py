"""Unit tests for app.py covering AC-1 through AC-4."""
from __future__ import annotations

import threading
import urllib.request

from app import Handler, render_index
from http.server import HTTPServer


def test_render_index_contains_demo_markers():
    """AC-2: Startseite hat Titel Demo und Überschrift Hallo Welt."""
    html = render_index()
    assert "<title>Demo</title>" in html
    assert 'data-testid="headline"' in html
    assert "Hallo Welt" in html
    assert 'data-testid="greet"' in html
    assert "Begrüßen" in html
    assert 'data-testid="greeting"' in html
    assert "Hallo, Karim!" in html


def test_health_endpoint_returns_200_and_ready():
    """AC-1: GET /health antwortet mit HTTP 200 und Body 'ready'."""
    server = HTTPServer(("127.0.0.1", 0), Handler)
    port = server.server_address[1]
    t = threading.Thread(target=server.handle_request)
    t.start()
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/health") as resp:
            assert resp.status == 200
            body = resp.read().decode("utf-8")
            assert body == "ready"
    finally:
        t.join(timeout=2)
        server.server_close()


def test_greeting_in_index():
    """AC-3: Hallo, Karim! ist in der Startseite enthalten (JS zeigt es)."""
    html = render_index()
    assert "Hallo, Karim!" in html
    assert "hidden" in html  # initially hidden, revealed by JS on click
