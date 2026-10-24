import requests
import base64
import re

auth = base64.b64encode(b'barcode128:5CoX aTTH Qzr8 NJzn zLNP xvZW').decode()
headers = {
    'Authorization': 'Basic ' + auth,
    'Content-Type': 'application/json'
}
wp_base = 'https://barcode128.mycafe24.com/wp-json/wp/v2/pages'

r = requests.get(f'{wp_base}/2143?context=edit', headers=headers).json()
content = r['content']['raw']

# 1. 와이드 레이아웃 & 3열 그리드 CSS 정의
BULLETPROOF_CSS = """
/* GP 테마 100% 전폭 강제 (미디어 쿼리 덮어쓰기) */
@media (min-width: 0px) {
    .site-content, .grid-container {
        display: block !important;
        width: 100% !important;
        max-width: 1240px !important;
        margin: 0 auto !important;
    }
    #primary, #primary.content-area, .site-content .content-area,
    .site-content .content-area > main, body:not(.no-sidebar) .site-content .content-area {
        width: 100% !important;
        max-width: 100% !important;
        flex: 1 1 100% !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    #left-sidebar, #right-sidebar {
        display: none !important;
        width: 0 !important;
        flex: 0 0 0 !important;
        visibility: hidden !important;
    }
}

/* 쿠팡 3종 추천 카드: 무조건 칼같은 가로 3열 */
.affiliate-3col-grid {
    display: grid !important;
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
    gap: 20px !important;
    width: 100% !important;
    margin-top: 16px !important;
}
.affiliate-3col-grid > * {
    min-width: 0 !important;
    box-sizing: border-box !important;
}
.affiliate-3col-grid > p {
    display: none !important;
    margin: 0 !important;
    padding: 0 !important;
    width: 0 !important;
    height: 0 !important;
}
@media (max-width: 768px) {
    .affiliate-3col-grid {
        grid-template-columns: 1fr !important;
        gap: 16px !important;
    }
}
"""

# 기존 스타일 태그 내에 BULLETPROOF_CSS 주입
if '</style>' in content:
    content = content.replace('</style>', BULLETPROOF_CSS + '\n</style>')
else:
    content = f"<style>\n{BULLETPROOF_CSS}\n</style>\n" + content

# 2. 그리드 컨테이너 클래스를 affiliate-3col-grid 로 확실하게 지정
content = re.sub(
    r'<div\s+(?:class="[^"]*"\s+)?style="display:grid;[^"]*">',
    r'<div class="affiliate-3col-grid">',
    content
)
content = re.sub(
    r'<div class="affiliate-grid-container">',
    r'<div class="affiliate-3col-grid">',
    content
)

# 3. 불필요한 고아 <p> 태그 청소
content = re.sub(r'<div class="affiliate-3col-grid">\s*</p>', r'<div class="affiliate-3col-grid">', content)
content = re.sub(r'</p>\s*<div class="affiliate-card"', r'<div class="affiliate-card"', content)
content = re.sub(r'</div>\s*<p>\s*<!--.*?-->\s*</p>', r'</div>', content)
content = re.sub(r'<!--\s*Item.*?\s*-->', '', content)

payload = {'content': content}
res = requests.post(f"{wp_base}/2143", headers=headers, json=payload)
print("Updated 2143 with bulletproof 3-col grid:", res.status_code)
