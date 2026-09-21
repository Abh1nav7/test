import pathlib


def test_background_color_is_maroon():
    """Ensure the page background color in style.css is set to maroon as requested in issue #12."""
    css = pathlib.Path('style.css').read_text()
    # look for exact property with semicolon (allow optional whitespace)
    assert 'background-color: maroon;' in css, "Expected 'background-color: maroon;' in style.css but not found."
