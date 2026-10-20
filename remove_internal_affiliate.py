import re
import os

files = [
    "barcode.html",
    "public/barcode.html",
    "margin.html",
    "public/margin.html",
    "ocr-keyword.html",
    "public/ocr-keyword.html",
    "title-combiner.html",
    "public/title-combiner.html",
    "thumbnail.html",
    "public/thumbnail.html",
    "index.html",
    "public/index.html"
]

pattern = re.compile(r'\s*<!-- Seller Affiliate Section.*?-->\s*<section[^>]*id=["\']affiliateSection["\'][^>]*>.*?</section>', re.DOTALL)

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = pattern.sub("", content)

        # Also remove if no comment before
        if "id=\"affiliateSection\"" in new_content:
            new_content = re.sub(r'\s*<section[^>]*id=["\']affiliateSection["\'][^>]*>.*?</section>', '', new_content, flags=re.DOTALL)

        if len(content) != len(new_content):
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"[제거 완료] {fpath}: {len(content) - len(new_content)} bytes 삭제됨")
        else:
            print(f"[변경 없음] {fpath}")

print("\n모든 툴 파일 내 내부 중복 광고 섹션 제거 완료!")
