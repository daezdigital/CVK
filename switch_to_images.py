import os

url_mapping = {
    "assets/logo.png": "images/logo.png",
    "assets/chris-profile.png": "images/chris-profile.png",
    "assets/hero-fallback.png": "images/hero-fallback.png",
    "assets/services-section.png": "images/services-section.png",
    "assets/about-section.png": "images/about-section.png",
    "assets/reviews-section.png": "images/reviews-section.png"
}

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for old, new in url_mapping.items():
            content = content.replace(old, new)
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {html_file}")
    except Exception as e:
        print(f"Failed to update {html_file}: {e}")
