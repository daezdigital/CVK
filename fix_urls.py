import os
import re

# Mapping of the localhost URLs to the new relative paths
url_mapping = {
    "http://localhost:3001/cvk_logo_1778012047100.png": "assets/logo.png",
    "http://localhost:3001/chris_portrait_1778012017308.png": "assets/chris-profile.png",
    "http://localhost:3001/hero_fallback_1778012032882.png": "assets/hero-fallback.png",
    "http://localhost:3001/services_section_1778012307271.png": "assets/services-section.png",
    "http://localhost:3001/about_section_1778012315025.png": "assets/about-section.png",
    "http://localhost:3001/reviews_section_1778012308575.png": "assets/reviews-section.png"
}

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for old_url, new_path in url_mapping.items():
        content = content.replace(old_url, new_path)
    
    if content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated URLs in {html_file}")
    else:
        print(f"No URLs to update in {html_file}")
