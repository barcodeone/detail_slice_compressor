import glob
import re
import os

files = [
    'barcode.html', 'public/barcode.html',
    'margin.html', 'public/margin.html',
    'ocr-keyword.html', 'public/ocr-keyword.html',
    'title-combiner.html', 'public/title-combiner.html',
    'thumbnail.html', 'public/thumbnail.html',
    'index.html', 'public/index.html'
]

pattern = re.compile(r'\s*<!-- Seller Affiliate Section.*?-->\s*<section[^>]*id=["\']affiliateSection["\'][^>]*>.*?</section>', re.DOTALL)
fallback_pattern = re.compile(r'\s*<section[^>]*id=["\']affiliateSection["\'][^>]*>.*?</section>', re.DOTALL)

for fpath in files:
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    orig_len = len(content)
    new_content = pattern.sub('', content)
    if 'affiliateSection' in new_content:
        new_content = fallback_pattern.sub('', new_content)
    
    diff = orig_len - len(new_content)
    print(f"{fpath}: diff={diff} bytes, remaining affiliateSection: {'affiliateSection' in new_content}")
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("모든 파일 정리 완료!")
