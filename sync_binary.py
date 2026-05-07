import os

# Absolute paths for reliability
base_dir = r"c:\Users\Personal\OneDrive\Documentos\Webs Clients Daez\CVK"
src_base = r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c"
dst_base = os.path.join(base_dir, "images")

files = {
    os.path.join(src_base, "cvk_logo_1778012047100.png"): os.path.join(dst_base, "logo.png"),
    os.path.join(src_base, "chris_portrait_1778012017308.png"): os.path.join(dst_base, "chris-profile.png"),
    os.path.join(src_base, "hero_fallback_1778012032882.png"): os.path.join(dst_base, "hero-fallback.png"),
    os.path.join(src_base, "services_section_1778012307271.png"): os.path.join(dst_base, "services-section.png"),
    os.path.join(src_base, "about_section_1778012315025.png"): os.path.join(dst_base, "about-section.png"),
    os.path.join(src_base, "reviews_section_1778012308575.png"): os.path.join(dst_base, "reviews-section.png")
}

if not os.path.exists(dst_base):
    os.makedirs(dst_base)
    print(f"Created directory: {dst_base}")

for src, dst in files.items():
    try:
        if not os.path.exists(src):
            print(f"Source missing: {src}")
            continue
            
        with open(src, 'rb') as f_src:
            data = f_src.read()
        with open(dst, 'wb') as f_dst:
            f_dst.write(data)
        print(f"Successfully synced: {os.path.basename(dst)}")
    except Exception as e:
        print(f"Failed to sync {os.path.basename(dst)}: {e}")

print("\nSync process finished.")
