import os
import shutil

# Mapping of original filenames in the brain directory to their local assets names
files = {
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\cvk_logo_1778012047100.png": r"assets\logo.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\chris_portrait_1778012017308.png": r"assets\chris-profile.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\hero_fallback_1778012032882.png": r"assets\hero-fallback.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\services_section_1778012307271.png": r"assets\services-section.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\about_section_1778012315025.png": r"assets\about-section.png",
    r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\reviews_section_1778012308575.png": r"assets\reviews-section.png"
}

for src, dst in files.items():
    try:
        # Get absolute path for destination to be sure
        abs_dst = os.path.join(os.getcwd(), dst)
        os.makedirs(os.path.dirname(abs_dst), exist_ok=True)
        shutil.copy2(src, abs_dst)
        print(f"Copied {os.path.basename(src)} to {dst}")
    except Exception as e:
        print(f"Failed to copy {os.path.basename(src)}: {e}")
