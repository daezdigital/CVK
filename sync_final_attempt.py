import os

# Use absolute paths for everything
current_dir = os.path.dirname(os.path.abspath(__file__))
dst_dir = os.path.join(current_dir, "cvk_images_v1")

src_files = [
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\cvk_logo_1778012047100.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\chris_portrait_1778012017308.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\hero_fallback_1778012032882.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\services_section_1778012307271.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\about_section_1778012315025.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\reviews_section_1778012308575.png"
]

dst_names = [
    "logo.png",
    "chris-profile.png",
    "hero-fallback.png",
    "services-section.png",
    "about-section.png",
    "reviews-section.png"
]

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

for src, name in zip(src_files, dst_names):
    dst = os.path.join(dst_dir, name)
    try:
        with open(src, 'rb') as f_src:
            content = f_src.read()
        with open(dst, 'wb') as f_dst:
            f_dst.write(content)
        print(f"Synced {name}")
    except Exception as e:
        print(f"Error syncing {name}: {e}")
