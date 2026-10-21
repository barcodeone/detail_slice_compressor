import requests
import base64
import re

auth = base64.b64encode(b'barcode128:5CoX aTTH Qzr8 NJzn zLNP xvZW').decode()
headers = {
    'Authorization': 'Basic ' + auth,
    'Content-Type': 'application/json'
}
wp_base = "https://barcode128.mycafe24.com/wp-json/wp/v2"

# 1. Add "일상 꿀툴 모음" to Primary Menu (Menu ID: 18)
r_menu = requests.post(f"{wp_base}/menu-items", headers=headers, json={
    'title': '일상 꿀툴 모음',
    'url': 'https://barcode128.mycafe24.com/daily/',
    'menus': 18,
    'status': 'publish',
    'menu_order': 2
})
print("Menu Item added:", r_menu.status_code)

# 2. Daily Tools Hub Content (Slug: daily)
html_raw = """
<style>
/* 0. 초슬림 미니멀 헤더 */
.site-header {
    padding: 8px 0 !important;
    background: #ffffff !important;
    border-bottom: 1px solid #e2e8f0 !important;
}
.inside-header {
    padding: 4px 16px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
}
.site-branding .main-title {
    margin: 0 !important;
    font-size: 19px !important;
    font-weight: 800 !important;
    line-height: 1.2 !important;
}
.site-branding .main-title a {
    color: #0f172a !important;
    text-decoration: none !important;
}
.main-navigation .main-nav ul {
    display: flex !important;
    gap: 8px !important;
}
.main-navigation .main-nav ul li a {
    padding: 6px 14px !important;
    font-size: 12.5px !important;
    font-weight: 700 !important;
    color: #4f46e5 !important;
    background: #eef2ff !important;
    border-radius: 6px !important;
    transition: all 0.15s ease !important;
}
.main-navigation .main-nav ul li a:hover {
    background: #e0e7ff !important;
}
.separate-containers .site-main { margin-top: 8px !important; }
.inside-article { padding-top: 8px !important; }
#left-sidebar, #right-sidebar { display: none !important; }
#primary.content-area, .site-content .content-area { width: 100% !important; max-width: 100% !important; float: none !important; }
.grid-container { max-width: 1200px !important; }
.entry-header { display: none !important; }

/* Hub Styles */
.daily-hub-wrap p:empty, .daily-card-grid > p { display: none !important; margin: 0 !important; }
.daily-hub-wrap {
    font-family: -apple-system, BlinkMacSystemFont, "Pretendard", "Segoe UI", Roboto, sans-serif;
    color: #1e293b;
    margin: 0 auto;
    max-width: 1140px;
}
.daily-header { text-align: center; padding: 24px 10px 20px 10px; }
.daily-pill { display: inline-block; padding: 5px 12px; background: #ecfdf5; color: #059669; font-size: 12px; font-weight: 700; border-radius: 999px; margin-bottom: 10px; }
.daily-title { font-size: 28px; font-weight: 900; color: #0f172a; margin: 0 0 8px 0; letter-spacing: -0.5px; }
.daily-subtitle { font-size: 14px; color: #64748b; margin: 0; line-height: 1.5; }

.daily-card-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    margin-top: 20px;
}
.daily-box {
    flex: 1 1 calc(50% - 10px);
    min-width: 300px;
    box-sizing: border-box;
    background: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-radius: 18px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.2s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}
.daily-box:hover {
    border-color: #4f46e5;
    box-shadow: 0 10px 20px -5px rgba(79, 70, 229, 0.15);
    transform: translateY(-3px);
}
.daily-box-top { margin-bottom: 16px; }
.daily-icon-row { display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; }
.daily-emoji {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
}
.daily-badge-pill {
    font-size: 11px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 6px;
    background: #f1f5f9;
    color: #475569;
}
.daily-box-title { font-size: 18px; font-weight: 800; color: #0f172a; margin: 0 0 8px 0; line-height: 1.4; }
.daily-box-desc { font-size: 13px; color: #64748b; margin: 0; line-height: 1.6; }
.daily-go-btn {
    display: block;
    width: 100%;
    padding: 11px 0;
    text-align: center;
    background: #0f172a;
    color: #ffffff !important;
    text-decoration: none !important;
    font-size: 13.5px;
    font-weight: 700;
    border-radius: 8px;
    transition: all 0.2s ease;
    margin-top: 16px;
}
.daily-box:hover .daily-go-btn { background: #4f46e5; }

@media (max-width: 640px) {
    .daily-box { flex: 1 1 100%; }
}
</style>

<div class="daily-hub-wrap">
    <div class="daily-header">
        <span class="daily-pill">🌿 생활 밀착형 무료 유틸리티 모음</span>
        <h1 class="daily-title">일상 속 유용한 꿀툴 모음</h1>
        <p class="daily-subtitle">직장인, 취준생, 학생 누구나 매일 유용하게 쓸 수 있는 개인정보 안전 무료 유틸리티 모음입니다.</p>
    </div>

    <div class="daily-card-grid">

        <!-- 1. 급여 & 퇴직금 -->
        <div class="daily-box">
            <div class="daily-box-top">
                <div class="daily-icon-row">
                    <div class="daily-emoji" style="background:#eef2ff;">💼</div>
                    <span class="daily-badge-pill" style="background:#e0e7ff; color:#4338ca;">급여·정산</span>
                </div>
                <h3 class="daily-box-title">연봉 실수령액 &amp; 주휴수당·퇴직금 계산기</h3>
                <p class="daily-box-desc">2026년 최신 4대보험 요율 반영 연봉별 세후 실수령액, 알바 시급 및 주휴수당, 평균임금 기준 예상 퇴직금과 실업급여를 한 번에 계산합니다.</p>
            </div>
            <a href="/salary-calculator/" class="daily-go-btn">도구 실행하기 ➔</a>
        </div>

        <!-- 2. PDF Tools -->
        <div class="daily-box">
            <div class="daily-box-top">
                <div class="daily-icon-row">
                    <div class="daily-emoji" style="background:#fee2e2;">📄</div>
                    <span class="daily-badge-pill" style="background:#fecdd3; color:#be123c;">100% 무서버 보안</span>
                </div>
                <h3 class="daily-box-title">초고속 PDF 합치기 &amp; 페이지 분할기</h3>
                <p class="daily-box-desc">계약서, 주민등록등본, 이력서 등 민감한 개인정보 문서를 서버 업로드 없이 브라우저 메모리에서 1초 만에 안전하게 병합하고 분할 추출합니다.</p>
            </div>
            <a href="/pdf-tools/" class="daily-go-btn">도구 실행하기 ➔</a>
        </div>

        <!-- 3. Word Counter -->
        <div class="daily-box">
            <div class="daily-box-top">
                <div class="daily-icon-row">
                    <div class="daily-emoji" style="background:#f0fdf4;">✍️</div>
                    <span class="daily-badge-pill" style="background:#dcfce7; color:#15803d;">자소서·블로그</span>
                </div>
                <h3 class="daily-box-title">글자수 세기 &amp; 바이트(Byte) 계산기</h3>
                <p class="daily-box-desc">공백 포함/제외 실시간 글자수, 공기업·대기업 채용 사이트 맞춤 2Byte(EUC-KR) 및 3Byte(UTF-8) 바이트 계산, 원고지 매수 환산을 지원합니다.</p>
            </div>
            <a href="/word-counter/" class="daily-go-btn">도구 실행하기 ➔</a>
        </div>

        <!-- 4. D-Day -->
        <div class="daily-box">
            <div class="daily-box-top">
                <div class="daily-icon-row">
                    <div class="daily-emoji" style="background:#fef3c7;">📅</div>
                    <span class="daily-badge-pill" style="background:#fde68a; color:#92400e;">일정·기념일</span>
                </div>
                <h3 class="daily-box-title">스마트 디데이(D-Day) &amp; 기념일·만나이 카운터</h3>
                <p class="daily-box-desc">시험·수능·여행 목표일 D-Day 카운트다운, 커플 100일/1주년 달력 리스트, 개정된 대한민국 공식 '만 나이' 및 띠/별자리를 원클릭 확인합니다.</p>
            </div>
            <a href="/dday-calculator/" class="daily-go-btn">도구 실행하기 ➔</a>
        </div>

    </div>
</div>
"""

def clean_html(h):
    h = re.sub(r'>\s+<', '><', h.strip())
    h = re.sub(r'[\r\n]+', '', h)
    return h

# Check existing page for slug: daily
r_chk = requests.get(f"{wp_base}/pages?slug=daily", headers=headers).json()
if r_chk:
    pid = r_chk[0]["id"]
    res = requests.post(f"{wp_base}/pages/{pid}", headers=headers, json={
        "title": "일상 속 유용한 꿀툴 모음 (직장인·학생 생활 유틸리티) | Barcode128",
        "content": clean_html(html_raw)
    })
    print(f"Daily Hub updated (ID: {pid}):", res.status_code)
else:
    res = requests.post(f"{wp_base}/pages", headers=headers, json={
        "title": "일상 속 유용한 꿀툴 모음 (직장인·학생 생활 유틸리티) | Barcode128",
        "content": clean_html(html_raw),
        "slug": "daily",
        "status": "publish"
    })
    print(f"Daily Hub created (ID: {res.json().get('id')}):", res.status_code)
