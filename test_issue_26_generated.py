import re


def test_background_color_is_red_issue_26():
    """Ensure the CSS background color is set to red as requested in issue #26."""
    with open("style.css", "r", encoding="utf-8") as f:
        css = f.read()

    m = re.search(r'background-color\s*:\s*([^;]+);', css, re.IGNORECASE)
    assert m is not None, "No background-color property found in style.css"

    value = m.group(1).strip().lower()
    assert value == "red", f"Expected background-color to be 'red', but found '{value}'"
