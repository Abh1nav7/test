import re


def test_background_color_is_blue_issue_24():
    """Ensure the CSS background color is set to blue as requested in issue #24."""
    with open("style.css", "r", encoding="utf-8") as f:
        css = f.read()

    # Find background-color property value
    m = re.search(r'background-color\s*:\s*([^;]+);', css, re.IGNORECASE)
    assert m is not None, "No background-color property found in style.css"

    value = m.group(1).strip().lower()
    assert value == "blue", f"Expected background-color to be 'blue', but found '{value}'"
