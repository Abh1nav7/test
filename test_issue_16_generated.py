import re


def test_background_color_is_yellow_issue_16():
    """Ensure the CSS background color is set to yellow as requested in issue #16."""
    with open("style.css", "r", encoding="utf-8") as f:
        css = f.read()

    # Find background-color property value
    m = re.search(r'background-color\s*:\s*([^;]+);', css, re.IGNORECASE)
    assert m is not None, "No background-color property found in style.css"

    value = m.group(1).strip().lower()
    assert value == "yellow", f"Expected background-color to be 'yellow', but found '{value}'"
