import os
import shutil

src_dir = r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c"
dst_dir = os.path.join(os.getcwd(), "images_fix")

# os.makedirs(dst_dir) # Skipped because it fails on this system, directory created by write_to_file

mapping = {
    "logo.png": "cvk_logo_1778012047100.png",
    "chris-profile.png": "chris_portrait_1778012017308.png",
    "hero-fallback.png": "hero_fallback_1778012032882.png",
    "services-section.png": "services_section_1778012307271.png",
    "about-section.png": "about_section_1778012315025.png",
    "reviews-section.png": "reviews_section_1778012308575.png"
}

for dst_name, src_name in mapping.items():
    src_path = os.path.join(src_dir, src_name)
    dst_path = os.path.join(dst_dir, dst_name)
    try:
        shutil.copyfile(src_path, dst_path) # Use copyfile for simplicity
        print(f"Copied {src_name} to {dst_name}")
    except Exception as e:
        print(f"Error copying {src_name}: {e}")

print(f"Files in {dst_dir}: {os.listdir(dst_dir)}")
