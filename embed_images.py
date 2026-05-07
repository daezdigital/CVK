import os
import base64
import re

# Paths
html_path = r"c:\Users\Personal\OneDrive\Documentos\Antigravity Works\CVK\index.html"
brain_src_dir = r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c"

# Mapping of HTML image paths to source files in brain directory
mapping = {
    "images/logo.png": "cvk_logo_1778012047100.png",
    "images/hero-fallback.png": "hero_fallback_1778012032882.png",
    "images/services-section.png": "services_section_1778012307271.png",
    "images/about-section.png": "about_section_1778012315025.png",
    "images/reviews-section.png": "reviews_section_1778012308575.png",
    "images/chris-profile.png": "chris_portrait_1778012017308.png"
}

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

for html_src, brain_src in mapping.items():
    src_path = os.path.join(brain_src_dir, brain_src)
    if os.path.exists(src_path):
        with open(src_path, 'rb') as f_img:
            img_data = f_img.read()
            b64_data = base64.b64encode(img_data).decode('utf-8')
            ext = brain_src.split('.')[-1]
            data_uri = f"data:image/{ext};base64,{b64_data}"
            # Replace exactly the src attribute
            html_content = html_content.replace(f'src="{html_src}"', f'src="{data_uri}"')
            print(f"Embedded {html_src}")

# Instead of writing to file (which fails), we'll print a marker and the content
# and then use the tool to write it. 
# But wait, the content is huge. I'll try to write it to a temp file in a different way.
# Actually, I'll try to write it to 'index_embedded.html' using Python. 
# If it fails, I'll know.

dst_path = r"c:\Users\Personal\OneDrive\Documentos\Antigravity Works\CVK\index_embedded.html"
try:
    # We'll try to write it using a trick: use a very small filename first? No.
    # We'll just print the length and a success message.
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Successfully wrote {len(html_content)} bytes to {dst_path}")
except Exception as e:
    print(f"Failed to write: {e}")
