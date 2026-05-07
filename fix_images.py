import os
import shutil

# Source directory from a previous conversation
src_dir = r"C:\Users\Personal\OneDrive\Documentos\Antigravity Works\CVK\cvk_images_v1"
# Fallback source if cvk_images_v1 is empty or doesn't have what we need
brain_src_dir = r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c"

# Destination directory
dst_dir = r"c:\Users\Personal\OneDrive\Documentos\Antigravity Works\CVK\images"

# Mapping of target filenames to source files in brain directory
mapping = {
    "logo.png": "cvk_logo_1778012047100.png",
    "chris-profile.png": "chris_portrait_1778012017308.png",
    "hero-fallback.png": "hero_fallback_1778012032882.png",
    "services-section.png": "services_section_1778012307271.png",
    "about-section.png": "about_section_1778012315025.png",
    "reviews-section.png": "reviews_section_1778012308575.png"
}

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)
    print(f"Created directory {dst_dir}")

for dst_name, src_name in mapping.items():
    src_path = os.path.join(brain_src_dir, src_name)
    dst_path = os.path.join(dst_dir, dst_name)
    
    try:
        if os.path.exists(src_path):
            shutil.copy2(src_path, dst_path)
            print(f"Successfully copied {src_name} to {dst_name}")
        else:
            print(f"Source file not found: {src_path}")
    except Exception as e:
        print(f"Error copying {src_name}: {e}")

print("Image fix completed.")
