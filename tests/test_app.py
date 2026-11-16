from app import render_index


def test_render_index_contains_demo_markers():
    html = render_index()
    assert "<title>Demo</title>" in html
    assert 'data-testid="headline"' in html
    assert "Hallo Welt" in html
    assert 'data-testid="greet"' in html
    assert "Begrüßen" in html
    assert 'data-testid="greeting"' in html
    assert "Hallo, Karim!" in html
