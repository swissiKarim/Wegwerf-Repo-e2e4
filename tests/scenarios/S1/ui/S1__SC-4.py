# scenario-id: S1/SC-4
from asb_ui import page_session, screenshot
import json

with page_session() as (page, base_url):
    page.goto(base_url)
    page.click('[data-testid="greet"]')
    page.wait_for_selector('[data-testid="greeting"]:not([hidden])')
    title = page.title()
    text = page.inner_text("body")
    visible = {"greeting": page.is_visible('[data-testid="greeting"]')}
    screenshot(page, "S1/SC-4")
    print(json.dumps({
        "title": title,
        "url": page.url,
        "text": text,
        "visible": visible,
    }))
