"""Minimal stdlib web app for E2E-4 seed (no third-party deps)."""

from __future__ import annotations

from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8099


def render_index() -> str:
    """HTML for GET /. Importable for unit tests."""
    return """<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <h1 data-testid="headline">Hallo Welt</h1>
    <button type="button" data-testid="greet" id="greet">Begrüßen</button>
    <p data-testid="greeting" id="greeting" hidden>Hallo, Karim!</p>
    <script>
      document.getElementById("greet").addEventListener("click", function () {
        var el = document.getElementById("greeting");
        el.hidden = false;
      });
    </script>
  </body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format: str, *args) -> None:  # noqa: A003
        return

    def do_GET(self) -> None:  # noqa: N802
        if self.path.split("?", 1)[0] == "/health":
            body = b"ready"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if self.path.split("?", 1)[0] in ("/", "/index.html"):
            html = render_index().encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html)))
            self.end_headers()
            self.wfile.write(html)
            return
        self.send_response(404)
        self.end_headers()


def main() -> None:
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()


if __name__ == "__main__":
    main()
