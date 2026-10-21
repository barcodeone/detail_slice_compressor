import requests
import base64
import re

auth = base64.b64encode(b'barcode128:5CoX aTTH Qzr8 NJzn zLNP xvZW').decode()
headers = {
    'Authorization': 'Basic ' + auth,
    'Content-Type': 'application/json'
}
wp_base = "https://barcode128.mycafe24.com/wp-json/wp/v2/pages"

SLIM_HEADER_CSS = """
/* 0. [옵션 A] 초슬림 미니멀 헤더 최적화 */
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
.grid-container { max-width: 1280px !important; }
.entry-header { display: none !important; }
"""

def clean_html(h):
    h = re.sub(r'>\s+<', '><', h.strip())
    h = re.sub(r'[\r\n]+', '', h)
    return h

# 1. Page electricity-calculator
raw_html = f"""<!-- wp:html -->
<style>{SLIM_HEADER_CSS}</style>
<div style="width:100%; max-width:1200px; margin:0 auto; padding-bottom:50px; font-family:'Pretendard', sans-serif;">
    <iframe src="https://barcodeone.github.io/detail_slice_compressor/electricity-calculator.html" style="width:100%; height:980px; border:none; border-radius:20px; box-shadow:0 4px 20px rgba(0,0,0,0.06); margin-bottom:40px; display:block;" scrolling="auto"></iframe>

    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:24px; padding:32px; margin-top:30px;">
        <div style="margin-bottom:24px;">
            <span style="font-size:12px; font-weight:800; color:#4f46e5; text-transform:uppercase; letter-spacing:0.5px;">RECOMMENDATION</span>
            <h3 style="font-size:20px; font-weight:900; color:#0f172a; margin:4px 0 6px 0;">⚡ 가정용 스마트 절전 &amp; 대기전력 차단 추천 아이템 3종</h3>
            <p style="font-size:13px; color:#64748b; margin:0;">낭비되는 대기전력을 1초 만에 차단하고 전기세를 획기적으로 줄여주는 인기 절전템입니다.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px;">
            <!-- Item 1: 필립스 개별 스위치 멀티탭 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h0uYoZNm6m" target="_blank" referrerpolicy="unsafe-url"><img src="https://img1a.coupangcdn.com/image/affiliate/banner/711a78887e59bbf6cfb8e05c873347f3@2x.jpg" alt="필립스 개별 스위치 과부하 서지 보호 멀티탭 6구, 3m" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#eef2ff; color:#4338ca; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">대기전력 100% 차단</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">필립스 6구 개별 스위치 과부하·서지 보호 안전 멀티탭 (3M)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">안 쓰는 가전제품의 플러그를 뽑지 않아도 개별 버튼으로 대기전력을 완벽 차단해 전기요금 절약.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">로켓배송</span>
                    <a href="https://link.coupang.com/a/h0uYoZNm6m" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 2: Airwit 와이드 모니터 조명 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h0uJyr16d2" target="_blank" referrerpolicy="unsafe-url"><img src="https://image7.coupangcdn.com/image/affiliate/banner/e96fbb37ea94982ecbf6292184130156@2x.jpg" alt="Airwit 와이드 모니터 LED 클립 조명 스탠드" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#fef3c7; color:#b45309; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">초절전 LED 조명</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">Airwit 듀얼헤드 플리커프리 와이드 모니터 LED 조명 (80cm)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">형광등 대비 전력 소비가 70% 적은 고효율 LED로 방 전체 불을 켜지 않고도 책상만 집중 조명.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">만족도 1위</span>
                    <a href="https://link.coupang.com/a/h0uJyr16d2" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 3: ValleyCraft 360도 쿨링팬 거치대 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h0uOKcDDt6" target="_blank" referrerpolicy="unsafe-url"><img src="https://img3a.coupangcdn.com/image/affiliate/banner/ba9d13b4f950386ec6c1f41768510c26@2x.jpg" alt="ValleyCraft 360도 회전 듀얼 쿨링팬 거치대" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#ecfdf5; color:#047857; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">발열 및 전력 저감</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">ValleyCraft 360도 회전 듀얼 저소음 쿨링팬 노트북 거치대</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">USB 저전력 듀얼 팬으로 노트북 내부 과열을 방지하여 기기 수명 연장 및 전력 소모 감소.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">로켓배송</span>
                    <a href="https://link.coupang.com/a/h0uOKcDDt6" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>
        </div>
        <p style="text-align:center; font-size:11px; color:#94a3b8; margin:24px 0 0 0;">이 포스팅은 쿠팡 파트너스 활동의 일환으로 이에 따른 일정액의 수수료를 제공받습니다.</p>
    </div>
</div>
<!-- /wp:html -->"""

slug = "electricity-calculator"
title = "한전 주택용 전기세 계산기 & 에어컨·가전제품 누진세 시뮬레이터 | Barcode128"

chk_res = requests.get(f"{wp_base}?slug={slug}", headers=headers).json()
if chk_res:
    pid = chk_res[0]["id"]
    res = requests.post(f"{wp_base}/{pid}", headers=headers, json={"title": title, "content": clean_html(raw_html)})
    print(f"Electricity Calculator updated (ID: {pid}):", res.status_code)
else:
    res = requests.post(wp_base, headers=headers, json={"title": title, "content": clean_html(raw_html), "slug": slug, "status": "publish"})
    print(f"Electricity Calculator created (ID: {res.json().get('id')}):", res.status_code)

# 2. Update Daily Hub (ID: 2148) with 5th Tool
hub_html_raw = """
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

        <!-- 5. 전기세 계산기 -->
        <div class="daily-box">
            <div class="daily-box-top">
                <div class="daily-icon-row">
                    <div class="daily-emoji" style="background:#fef9c3;">⚡</div>
                    <span class="daily-badge-pill" style="background:#fef08a; color:#a16207;">누진제 시뮬레이션</span>
                </div>
                <h3 class="daily-box-title">한전 주택용 전기세 계산기 &amp; 누진세 툴</h3>
                <p class="daily-box-desc">저압/고압 아파트 누진제 구간별 예상 전기요금, 에어컨·건조기·전열기 등 가전제품 소비전력에 따른 한 달 요금 증가액을 계산합니다.</p>
            </div>
            <a href="/electricity-calculator/" class="daily-go-btn">도구 실행하기 ➔</a>
        </div>

    </div>
</div>
"""

res_hub = requests.post(f"{wp_base}/2148", headers=headers, json={
    "title": "일상 속 유용한 꿀툴 모음 (직장인·학생 생활 유틸리티 5대 솔루션) | Barcode128",
    "content": clean_html(hub_html_raw)
})
print("Daily Hub updated with 5th tool (electricity-calculator):", res_hub.status_code)
