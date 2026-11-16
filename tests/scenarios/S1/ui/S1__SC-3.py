# scenario-id: S1/SC-3
from asb_ui import page_session, screenshot
import json

with page_session() as (page, base_url):
    page.goto(base_url)
    title = page.title()
    text = page.inner_text("body")
    visible = {"headline": page.is_visible('[data-testid="headline"]')}
    screenshot(page, "S1/SC-3")
    print(json.dumps({
        "title": title,
        "url": page.url,
        "text": text,
        "visible": visible,
    }))
