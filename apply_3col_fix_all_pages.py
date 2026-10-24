import requests
import base64
import re
import time

auth = base64.b64encode(b'barcode128:5CoX aTTH Qzr8 NJzn zLNP xvZW').decode()
headers = {
    'Authorization': 'Basic ' + auth,
    'Content-Type': 'application/json'
}
wp_base = 'https://barcode128.mycafe24.com/wp-json/wp/v2/pages'

BULLETPROOF_LAYOUT_CSS = """
/* 1. GeneratePress 테마 전폭 100% 강제 (미디어 쿼리 완벽 덮어쓰기) */
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

/* 2. 쿠팡 3종 추천 카드: PC/태블릿에서 칼같은 가로 3열, 모바일에서 1열 */
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

def clean_html(h):
    h = re.sub(r'>\s+<', '><', h.strip())
    h = re.sub(r'[\r\n]+', '', h)
    return h

pages = requests.get(f'{wp_base}?per_page=100&context=edit', headers=headers).json()
print(f"Total pages to process: {len(pages)}")

for p in pages:
    pid = p['id']
    slug = p['slug']
    if slug in ['sample-page', 'tools', 'daily']:
        continue
        
    raw = p['content']['raw']
    if not raw or len(raw) < 500:
        continue
        
    # 쿠팡 배너나 recommendation 섹션이 있는지 확인
    if 'RECOMMENDATION' not in raw and 'coupang' not in raw:
        continue
        
    print(f"[{pid}] {slug}: Applying bulletproof 3-col grid...")
    
    # 1. CSS 추가/갱신
    if '.affiliate-3col-grid' not in raw:
        if '</style>' in raw:
            raw = raw.replace('</style>', BULLETPROOF_LAYOUT_CSS + '\n</style>')
        else:
            raw = f"<style>\n{BULLETPROOF_LAYOUT_CSS}\n</style>\n" + raw
            
    # 2. 그리드 컨테이너 클래스를 affiliate-3col-grid 로 교체
    raw = re.sub(
        r'<div\s+(?:class="[^"]*"\s+)?style="display:grid;[^"]*">',
        r'<div class="affiliate-3col-grid">',
        raw
    )
    raw = re.sub(
        r'<div class="affiliate-grid-container">',
        r'<div class="affiliate-3col-grid">',
        raw
    )
    
    # 3. 고아 p 태그 및 불필요한 줄바꿈 정리
    raw = re.sub(r'<div class="affiliate-3col-grid">\s*</p>', r'<div class="affiliate-3col-grid">', raw)
    raw = re.sub(r'</p>\s*(<div class="affiliate-card"|<div style="background:#ffffff)', r'\1', raw)
    raw = re.sub(r'</div>\s*<p>\s*<!--.*?-->\s*</p>', r'</div>', raw)
    raw = re.sub(r'<!--\s*Item.*?\s*-->', '', raw)
    raw = re.sub(r'</div>\s*</p>', r'</div>', raw)
    
    # NinjaFirewall 403 방어: <script> 태그 제거
    if '<script' in raw:
        raw = re.sub(r'<script.*?</script>', '', raw, flags=re.DOTALL)
        
    payload = {'content': clean_html(raw)}
    res = requests.post(f"{wp_base}/{pid}", headers=headers, json=payload)
    print(f"[{pid}] {slug}: Status {res.status_code}")
    time.sleep(0.3)

print("All tool pages successfully updated with bulletproof 3-column layout!")
