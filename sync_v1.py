import os

# Mapping of original filenames to new local names
files = {
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\cvk_logo_1778012047100.png": r"cvk_images_v1\logo.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\chris_portrait_1778012017308.png": r"cvk_images_v1\chris-profile.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\hero_fallback_1778012032882.png": r"cvk_images_v1\hero-fallback.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\services_section_1778012307271.png": r"cvk_images_v1\services-section.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\about_section_1778012315025.png": r"cvk_images_v1\about-section.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\reviews_section_1778012308575.png": r"cvk_images_v1\reviews-section.png"
}

if not os.path.exists('cvk_images_v1'):
    os.makedirs('cvk_images_v1')

for src, dst in files.items():
    try:
        with open(src, 'rb') as f_src:
            data = f_src.read()
        with open(dst, 'wb') as f_dst:
            f_dst.write(data)
        print(f"Synced {dst}")
    except Exception as e:
        print(f"Failed to sync {dst}: {e}")
