# scenario-id: S1/SC-3
"""Startseite zeigt Titel Demo und Überschrift Hallo Welt."""
import json
from asb_ui import page_session, screenshot

with page_session() as (pw, browser, context, page):
    title = page.title()
    text = page.inner_text("body")
    headline_visible = page.is_visible('[data-testid="headline"]')
    screenshot(page, "S1/SC-3")
    print(json.dumps({
        "title": title,
        "url": page.url,
        "text": text,
        "visible": {"headline": headline_visible},
    }))
