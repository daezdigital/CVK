import os
import base64

brain_dir = r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c"

assets = {
    "assets/logo.png": os.path.join(brain_dir, "cvk_logo_1778012047100.png"),
    "assets/chris-profile.png": os.path.join(brain_dir, "chris_portrait_1778012017308.png"),
    "assets/hero-fallback.png": os.path.join(brain_dir, "hero_fallback_1778012032882.png")
}

def get_base64_uri(file_path, mime_type="image/png"):
    with open(file_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"

# Process index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

html_content = html_content.replace('src="assets/logo.png"', f'src="{get_base64_uri(assets["assets/logo.png"])}"')
html_content = html_content.replace('src="assets/chris-profile.png"', f'src="{get_base64_uri(assets["assets/chris-profile.png"])}"')
html_content = html_content.replace('"assets/logo.png"', f'"{get_base64_uri(assets["assets/logo.png"])}"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Process style.css
with open("style.css", "r", encoding="utf-8") as f:
    css_content = f.read()

css_content = css_content.replace("url('assets/hero-fallback.png')", f"url('{get_base64_uri(assets['assets/hero-fallback.png'])}')")
css_content = css_content.replace("url(\"assets/hero-fallback.png\")", f"url('{get_base64_uri(assets['assets/hero-fallback.png'])}')")
css_content = css_content.replace("url(assets/hero-fallback.png)", f"url('{get_base64_uri(assets['assets/hero-fallback.png'])}')")

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("Assets successfully embedded as Base64 in index.html and style.css!")
