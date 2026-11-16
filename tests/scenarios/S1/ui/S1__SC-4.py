# scenario-id: S1/SC-4
"""Klick auf Begrüßen zeigt Hallo, Karim!"""
import json
from asb_ui import page_session, screenshot

with page_session() as (pw, browser, context, page):
    page.click('[data-testid="greet"]')
    page.wait_for_selector('[data-testid="greeting"]:not([hidden])')
    text = page.inner_text("body")
    greeting_visible = page.is_visible('[data-testid="greeting"]')
    screenshot(page, "S1/SC-4")
    print(json.dumps({
        "title": page.title(),
        "url": page.url,
        "text": text,
        "visible": {"greeting": greeting_visible},
    }))
