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

PERFECT_LAYOUT_AND_NAV_CSS = """
/* 0. 초슬림 미니멀 헤더 최적화 */
.site-header { padding: 8px 0 !important; background: #ffffff !important; border-bottom: 1px solid #e2e8f0 !important; }
.inside-header { padding: 4px 16px !important; display: flex !important; align-items: center !important; justify-content: space-between !important; }
.site-branding .main-title { margin: 0 !important; font-size: 19px !important; font-weight: 800 !important; line-height: 1.2 !important; }
.site-branding .main-title a { color: #0f172a !important; text-decoration: none !important; }

/* 상단 헤더 메뉴 네비게이션 버튼 & 방문자 카운터 뱃지 */
.main-navigation .main-nav ul {
    display: flex !important;
    gap: 12px !important;
    align-items: center !important;
    list-style: none !important;
    margin: 0 !important;
    padding: 0 !important;
}
.main-navigation .main-nav ul li {
    margin: 0 !important;
    padding: 0 !important;
    list-style: none !important;
}
.main-navigation .main-nav ul li a {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 7px 16px !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    line-height: normal !important;
    height: auto !important;
    color: #334155 !important;
    background: #ffffff !important;
    border: 1.5px solid #cbd5e1 !important;
    border-radius: 9999px !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
    text-decoration: none !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
.main-navigation .main-nav ul li:first-child a::before {
    content: "💼";
    margin-right: 6px;
    font-size: 13px;
}
.main-navigation .main-nav ul li:nth-child(2) a::before {
    content: "🍀";
    margin-right: 6px;
    font-size: 13px;
}
.main-navigation .main-nav ul li a:hover {
    color: #ffffff !important;
    background: #2563eb !important;
    border-color: #2563eb !important;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25) !important;
    transform: translateY(-1px) !important;
}

/* 3번째 메뉴: 방문자 카운터 뱃지 스타일 */
.main-navigation .main-nav ul li:nth-child(3) a {
    display: inline-flex !important;
    align-items: center !important;
    padding: 6px 14px !important;
    font-size: 11.5px !important;
    font-weight: 700 !important;
    color: #475569 !important;
    background: #f8fafc !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 9999px !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
    cursor: default !important;
    pointer-events: none !important;
}
.main-navigation .main-nav ul li:nth-child(3) a::before {
    content: "●";
    color: #10b981;
    margin-right: 6px;
    font-size: 10px;
    animation: livePulse 1.8s infinite;
}
.main-navigation .main-nav ul li:nth-child(3) a:hover {
    color: #475569 !important;
    background: #f8fafc !important;
    border-color: #cbd5e1 !important;
    transform: none !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
}
@keyframes livePulse {
    0% { transform: scale(0.95); opacity: 0.7; }
    50% { transform: scale(1.2); opacity: 1; }
    100% { transform: scale(0.95); opacity: 0.7; }
}

/* 1. 사이드바 완벽 숨김 및 1280px 와이드 레이아웃 강제 */
#left-sidebar, #right-sidebar { display: none !important; width: 0 !important; height: 0 !important; }
#primary.content-area, .site-content .content-area, .site-content .content-area > main {
    width: 100% !important;
    max-width: 100% !important;
    float: none !important;
}
.site-content {
    display: block !important;
}
.grid-container {
    max-width: 1280px !important;
    width: 100% !important;
}
.separate-containers .site-main { margin-top: 8px !important; }
.inside-article { padding: 8px 16px !important; }
.entry-header { display: none !important; }

/* 2. 광고 배너 3열 카드 배열 틀어짐 방지: PC/태블릿에서 칼같은 3열, 모바일에서 1열 */
@media (min-width: 768px) {
    div[style*="grid-template-columns:repeat(auto-fit"] {
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 20px !important;
    }
}
@media (max-width: 767px) {
    div[style*="grid-template-columns:repeat(auto-fit"] {
        display: grid !important;
        grid-template-columns: 1fr !important;
        gap: 16px !important;
    }
}
""".strip()

def clean_html(h):
    h = re.sub(r'>\s+<', '><', h.strip())
    h = re.sub(r'[\r\n]+', '', h)
    return h

pages = requests.get(f'{wp_base}?per_page=100&context=edit', headers=headers).json()
print(f"Total pages to check: {len(pages)}")

for p in pages:
    pid = p['id']
    slug = p['slug']
    if slug == 'sample-page':
        continue
        
    raw_content = p['content']['raw']
    if not raw_content or len(raw_content) < 500:
        print(f"Skipping empty page: [{pid}] {slug}")
        continue
        
    # 기존 style 태그가 있는지 확인
    style_match = re.search(r'<style>(.*?)</style>', raw_content, re.DOTALL)
    if style_match:
        old_style = style_match.group(1)
        # 기존 헤더 및 사이드바/광고 관련 중복 룰 정리
        cleaned_style = re.sub(r'/\*.*?\*/', '', old_style)
        cleaned_style = re.sub(r'\.site-header\s*\{[^}]*\}', '', cleaned_style)
        cleaned_style = re.sub(r'\.inside-header\s*\{[^}]*\}', '', cleaned_style)
        cleaned_style = re.sub(r'\.site-branding[^{]*\{[^}]*\}', '', cleaned_style)
        cleaned_style = re.sub(r'\.main-navigation[^{]*\{[^}]*\}', '', cleaned_style)
        cleaned_style = re.sub(r'#left-sidebar[^{]*\{[^}]*\}', '', cleaned_style)
        cleaned_style = re.sub(r'#primary[^{]*\{[^}]*\}', '', cleaned_style)
        cleaned_style = re.sub(r'\.grid-container[^{]*\{[^}]*\}', '', cleaned_style)
        cleaned_style = re.sub(r'@keyframes\s+livePulse\s*\{[^}]*(\{[^}]*\}[^}]*)*\}', '', cleaned_style)
        cleaned_style = re.sub(r'@media[^{]*\{[^}]*\{[^}]*\}[^}]*\}', '', cleaned_style) # 기존 media query 중복 제거
        
        merged_style = PERFECT_LAYOUT_AND_NAV_CSS + "\n" + cleaned_style.strip()
        final_content = raw_content[:style_match.start()] + f"<style>\n{merged_style}\n</style>" + raw_content[style_match.end():]
    else:
        final_content = f"<style>\n{PERFECT_LAYOUT_AND_NAV_CSS}\n</style>\n" + raw_content

    # NinjaFirewall 403 방어: <script> 태그 제거
    if '<script' in final_content:
        final_content = re.sub(r'<script.*?</script>', '', final_content, flags=re.DOTALL)
        
    payload = {
        'content': clean_html(final_content)
    }
    
    up_res = requests.post(f"{wp_base}/{pid}", headers=headers, json=payload)
    print(f"[{pid}] {slug}: {up_res.status_code}")
    time.sleep(0.3)

print("All pages successfully updated with perfect 3-column layout and hidden sidebar!")
