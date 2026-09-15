import re


def test_background_color_is_purple():
    """Ensure the CSS background color is set to purple as requested in issue #6."""
    with open("style.css", "r", encoding="utf-8") as f:
        css = f.read()

    # Find background-color property value
    m = re.search(r'background-color\s*:\s*([^;]+);', css, re.IGNORECASE)
    assert m is not None, "No background-color property found in style.css"

    value = m.group(1).strip().lower()
    assert value == "purple", f"Expected background-color to be 'purple', but found '{value}'"

