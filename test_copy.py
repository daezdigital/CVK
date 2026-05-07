import os

src = r"C:\Users\Personal\.gemini\antigravity\brain\17b0d90b-0e15-4546-bf24-7710910a634c\cvk_logo_1778012047100.png"
dst = "x.png"

try:
    with open(src, 'rb') as f_src:
        data = f_src.read()
    with open(dst, 'wb') as f_dst:
        f_dst.write(data)
    print(f"Success: Created {os.path.abspath(dst)}")
except Exception as e:
    print(f"Error: {e}")
