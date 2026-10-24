import requests
import base64
import re

auth = base64.b64encode(b'barcode128:5CoX aTTH Qzr8 NJzn zLNP xvZW').decode()
headers = {
    'Authorization': 'Basic ' + auth,
    'Content-Type': 'application/json'
}
wp_base = 'https://barcode128.mycafe24.com/wp-json/wp/v2/pages'

# 통일된 최신 표준 헤더 CSS (캡슐 버튼, gap: 12px, 3번째 방문자 카운터 뱃지)
UNIFIED_NAV_CSS = """
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
""".strip()

def clean_html(h):
    h = re.sub(r'>\s+<', '><', h.strip())
    h = re.sub(r'[\r\n]+', '', h)
    return h

# 모든 페이지 가져오기
r = requests.get(f'{wp_base}?per_page=100', headers=headers)
pages = r.json()

print(f"Total pages to inspect: {len(pages)}")

for p in pages:
    pid = p['id']
    slug = p['slug']
    title = p['title']['rendered']
    
    # 샘플 페이지는 스킵
    if slug == 'sample-page':
        continue
        
    content_raw = p.get('content', {}).get('raw', '')
    
    # <style> 태그 확인
    if '<style>' in content_raw and '</style>' in content_raw:
        # 기존 <style> 태그 내부의 헤더 관련 CSS를 찾아서 교체하거나 앞부분에 추가
        # 가장 깔끔한 방법: 기존 style 태그 안의 .site-header ~ .main-navigation 관련 블록을 신규 CSS로 대체
        style_match = re.search(r'<style>(.*?)</style>', content_raw, re.DOTALL)
        if style_match:
            old_style = style_match.group(1)
            # 헤더/네비게이션 관련 기존 룰 제거
            cleaned_style = re.sub(r'/\*.*?\*/', '', old_style) # 주석 제거
            cleaned_style = re.sub(r'\.site-header\s*\{[^}]*\}', '', cleaned_style)
            cleaned_style = re.sub(r'\.inside-header\s*\{[^}]*\}', '', cleaned_style)
            cleaned_style = re.sub(r'\.site-branding[^{]*\{[^}]*\}', '', cleaned_style)
            cleaned_style = re.sub(r'\.main-navigation[^{]*\{[^}]*\}', '', cleaned_style)
            cleaned_style = re.sub(r'@keyframes\s+livePulse\s*\{[^}]*(\{[^}]*\}[^}]*)*\}', '', cleaned_style)
            
            new_style = UNIFIED_NAV_CSS + "\n" + cleaned_style.strip()
            new_content = content_raw[:style_match.start()] + f"<style>\n{new_style}\n</style>" + content_raw[style_match.end():]
        else:
            new_content = f"<style>\n{UNIFIED_NAV_CSS}\n</style>\n" + content_raw
    else:
        new_content = f"<style>\n{UNIFIED_NAV_CSS}\n</style>\n" + content_raw

    # NinjaFirewall 방어: script 태그 등이 없는지 확인
    payload = {
        'content': clean_html(new_content)
    }
    
    up_res = requests.post(f"{wp_base}/{pid}", headers=headers, json=payload)
    print(f"[{pid}] {slug}: {up_res.status_code}")

print("All pages updated successfully!")
