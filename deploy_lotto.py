import requests
import base64
import re

auth = base64.b64encode(b'barcode128:5CoX aTTH Qzr8 NJzn zLNP xvZW').decode()
headers = {
    'Authorization': 'Basic ' + auth,
    'Content-Type': 'application/json'
}
wp_base = "https://barcode128.mycafe24.com/wp-json/wp/v2/pages"

# 최신 표준 헤더 및 레이아웃 CSS
SLIM_HEADER_CSS = """
/* 0. 초슬림 미니멀 헤더 최적화 */
.site-header { padding: 8px 0 !important; background: #ffffff !important; border-bottom: 1px solid #e2e8f0 !important; }
.inside-header { padding: 4px 16px !important; display: flex !important; align-items: center !important; justify-content: space-between !important; }
.site-branding .main-title { margin: 0 !important; font-size: 19px !important; font-weight: 800 !important; line-height: 1.2 !important; }
.site-branding .main-title a { color: #0f172a !important; text-decoration: none !important; }
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
.main-navigation .main-nav ul li:last-child a::before {
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
.separate-containers .site-main { margin-top: 8px !important; }
.separate-containers .inside-article { padding: 0 !important; background: transparent !important; box-shadow: none !important; border: none !important; }
#left-sidebar, #right-sidebar { display: none !important; }
#primary.content-area, .site-content .content-area { width: 100% !important; max-width: 100% !important; float: none !important; }
.grid-container { max-width: 1280px !important; }
.entry-header { display: none !important; }

/* Coupang Button Protection against visited / theme color overwrite */
a.coupang-btn, a.coupang-btn:visited, a.coupang-btn:hover, a.coupang-btn:active, a.coupang-btn:focus,
a.coupang-btn *, a.coupang-btn span {
    color: #ffffff !important;
    text-decoration: none !important;
}
a.coupang-btn {
    padding: 8px 16px !important;
    background: #2563eb !important;
    font-size: 12.5px !important;
    font-weight: 800 !important;
    border-radius: 8px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 4px !important;
    box-shadow: 0 2px 6px rgba(37,99,235,0.28) !important;
    transition: all 0.15s ease !important;
}
a.coupang-btn:hover {
    background: #1d4ed8 !important;
}
"""

def clean_html(h):
    h = re.sub(r'>\s+<', '><', h.strip())
    h = re.sub(r'[\r\n]+', '', h)
    return h

# 1. Page lotto-generator
lotto_raw_html = f"""<!-- wp:html -->
<style>{SLIM_HEADER_CSS}</style>
<div style="width:100%; max-width:1200px; margin:0 auto; padding-bottom:50px; font-family:'Pretendard', sans-serif;">
    <!-- 1) 도구 Iframe 삽입 (무포장 일체형, 클립보드 및 웹공유 권한 허용) -->
    <iframe src="https://barcodeone.github.io/detail_slice_compressor/lotto-generator.html" allow="clipboard-write; clipboard-read; web-share" style="width:100%; height:940px; border:none; margin-bottom:30px; display:block;" scrolling="auto"></iframe>

    <!-- 2) 하단 추천 쿠팡 파트너스 배너 섹션 (가로 3열) -->
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:24px; padding:32px; margin-top:20px;">
        <div style="margin-bottom:24px;">
            <span style="font-size:12px; font-weight:800; color:#4f46e5; text-transform:uppercase; letter-spacing:0.5px;">RECOMMENDATION</span>
            <h3 style="font-size:20px; font-weight:900; color:#0f172a; margin:4px 0 6px 0;">🍀 1등 당첨 대박 기원 &amp; 행운의 힐링 추천템 3종</h3>
            <p style="font-size:13px; color:#64748b; margin:0;">기분 좋은 행운과 대박의 기운을 불러오는 인기 베스트셀러 아이템입니다.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px;">
            <!-- Item 1: 미소로운 영수증 보관 아코디언 영수증정리함 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h3JeuuJKrQ" target="_blank" referrerpolicy="unsafe-url"><img src="https://img5a.coupangcdn.com/image/affiliate/banner/2dbb78ee252f77a929eca28727fa0e6d@2x.jpg" alt="미소로운 영수증 보관 아코디언 영수증정리함 + 인덱스스티커, 투명블랙, 2개" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#fef3c7; color:#b45309; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">복권·영수증 깔끔 보관</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">미소로운 영수증·로또 복권 보관 아코디언 정리함 (인덱스 스티커 세트)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">구매한 로또 용지와 영수증을 구김이나 분실 없이 회차별로 안전하고 깔끔하게 보관하는 정리함.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">로켓배송</span>
                    <a href="https://link.coupang.com/a/h3JeuuJKrQ" target="_blank" referrerpolicy="unsafe-url" class="coupang-btn" style="padding:8px 16px; background:#2563eb !important; color:#ffffff !important; font-size:12.5px; font-weight:800; border-radius:8px; text-decoration:none; display:inline-flex; align-items:center; gap:4px; box-shadow:0 2px 6px rgba(37,99,235,0.28);"><span style="color:#ffffff !important; font-weight:800; text-decoration:none;">상품 보기 ➔</span></a>
                </div>
            </div>

            <!-- Item 2: 금전운 골드바 키링 행운 재물운 키홀더 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h3Jhyr6eI0" target="_blank" referrerpolicy="unsafe-url"><img src="https://img2a.coupangcdn.com/image/affiliate/banner/fa9241c31b8fb999ff4fbc384a6134a2@2x.jpg" alt="금전운 골드바 키링 행운 재물운 키홀더 설날 새해 개업 취업 선물포장" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#eef2ff; color:#4338ca; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">금전운·재물운 부적</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">1등 당첨 기원 금전운 골드바 키링 (행운 재물운 키홀더)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">매일 휴대하며 행운과 대박 재물운을 불러오는 묵직한 럭셔리 골드바 디자인의 행운 키링.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">선물 추천</span>
                    <a href="https://link.coupang.com/a/h3Jhyr6eI0" target="_blank" referrerpolicy="unsafe-url" class="coupang-btn" style="padding:8px 16px; background:#2563eb !important; color:#ffffff !important; font-size:12.5px; font-weight:800; border-radius:8px; text-decoration:none; display:inline-flex; align-items:center; gap:4px; box-shadow:0 2px 6px rgba(37,99,235,0.28);"><span style="color:#ffffff !important; font-weight:800; text-decoration:none;">상품 보기 ➔</span></a>
                </div>
            </div>

            <!-- Item 3: 제이에스리빙 풍수 돈들어오는 황금 금전수 돈나무 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h3Jp8qnbxs" target="_blank" referrerpolicy="unsafe-url"><img src="https://image6.coupangcdn.com/image/affiliate/banner/80bb7af903ca52f66b272e442a2bbac5@2x.jpg" alt="제이에스리빙 풍수 돈들어오는 장식품 돈복 황금 금전수 돈나무, 골드" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#ecfdf5; color:#047857; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">풍수 대박 인테리어</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">제이에스리빙 풍수 돈 들어오는 황금 금전수 돈나무 (골드)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">가정과 사무실에 황금빛 번영과 재물복을 불어넣어 주는 풍수 인테리어 베스트셀러 장식품.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">인기 상품</span>
                    <a href="https://link.coupang.com/a/h3Jp8qnbxs" target="_blank" referrerpolicy="unsafe-url" class="coupang-btn" style="padding:8px 16px; background:#2563eb !important; color:#ffffff !important; font-size:12.5px; font-weight:800; border-radius:8px; text-decoration:none; display:inline-flex; align-items:center; gap:4px; box-shadow:0 2px 6px rgba(37,99,235,0.28);"><span style="color:#ffffff !important; font-weight:800; text-decoration:none;">상품 보기 ➔</span></a>
                </div>
            </div>
        </div>

        <!-- 3) 쿠팡 실시간 검색 위젯 (표준 내장) -->
        <div style="margin-top:24px; padding-top:20px; border-top:1px solid #e2e8f0;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
                <span style="font-size:13px; font-weight:800; color:#0f172a; display:flex; align-items:center; gap:6px;">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    원하는 상품 직접 검색
                </span>
                <span style="font-size:11.5px; color:#64748b;">쿠팡 실시간 최저가 &amp; 로켓배송 상품 검색</span>
            </div>
            <div style="border-radius:14px; overflow:hidden; background:#ffffff; box-shadow:0 2px 8px rgba(0,0,0,0.04); border:1px solid #e2e8f0; line-height:0;">
                <iframe src="https://coupa.ng/cqkfar" width="100%" height="75" frameborder="0" scrolling="no" referrerpolicy="unsafe-url" style="width:100%; height:75px; border:none; display:block;"></iframe>
            </div>
        </div>

        <!-- 4) 공정위 필수 문구 -->
        <p style="text-align:center; font-size:11px; color:#94a3b8; margin:24px 0 0 0;">이 포스팅은 쿠팡 파트너스 활동의 일환으로 이에 따른 일정액의 수수료를 제공받습니다.</p>
    </div>
</div>
<!-- /wp:html -->"""

slug = "lotto-generator"
title = "스마트 로또 번호 생성기 & 생년월일·이름·커플 궁합 행운의 수비학 추첨기 | Barcode128"

chk_res = requests.get(f"{wp_base}?slug={slug}", headers=headers).json()
if chk_res:
    pid = chk_res[0]["id"]
    res = requests.post(f"{wp_base}/{pid}", headers=headers, json={"title": title, "content": clean_html(lotto_raw_html)})
    print(f"Lotto Generator updated (ID: {pid}):", res.status_code)
else:
    res = requests.post(wp_base, headers=headers, json={"title": title, "content": clean_html(lotto_raw_html), "slug": slug, "status": "publish"})
    print(f"Lotto Generator created (ID: {res.json().get('id')}):", res.status_code)

# 2. Update Daily Hub (ID: 2148) with 6th Tool
hub_html_raw = """
<style>
/* 0. 초슬림 미니멀 헤더 */
.site-header { padding: 8px 0 !important; background: #ffffff !important; border-bottom: 1px solid #e2e8f0 !important; }
.inside-header { padding: 4px 16px !important; display: flex !important; align-items: center !important; justify-content: space-between !important; }
.site-branding .main-title { margin: 0 !important; font-size: 19px !important; font-weight: 800 !important; line-height: 1.2 !important; }
.site-branding .main-title a { color: #0f172a !important; text-decoration: none !important; }
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
.main-navigation .main-nav ul li:last-child a::before {
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
.separate-containers .site-main { margin-top: 8px !important; }
.separate-containers .inside-article { padding: 0 !important; background: transparent !important; box-shadow: none !important; border: none !important; }
#left-sidebar, #right-sidebar { display: none !important; }
#primary.content-area, .site-content .content-area { width: 100% !important; max-width: 100% !important; float: none !important; }
.grid-container { max-width: 1280px !important; }
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
.daily-title { font-size: 26px; font-weight: 800; color: #0f172a; margin: 0 0 8px 0; letter-spacing: -0.5px; }
.daily-desc { font-size: 14px; color: #64748b; margin: 0 auto; max-width: 580px; line-height: 1.5; }

.daily-card-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-top: 24px;
}
@media (max-width: 900px) {
    .daily-card-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
    .daily-card-grid { grid-template-columns: 1fr; }
}

.daily-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    text-decoration: none !important;
}
.daily-card:hover {
    transform: translateY(-3px);
    border-color: #cbd5e1;
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
}

.daily-card-top { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px; }
.daily-icon-box {
    width: 44px;
    height: 44px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    flex-shrink: 0;
}
.daily-meta { display: flex; flex-direction: column; }
.daily-tag { font-size: 11px; font-weight: 700; margin-bottom: 2px; }
.daily-card-title { font-size: 16px; font-weight: 800; color: #0f172a; margin: 0; line-height: 1.3; }

.daily-card-desc { font-size: 12.5px; color: #64748b; line-height: 1.5; margin: 0 0 14px 0; }

.daily-card-foot {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid #f1f5f9;
    padding-top: 12px;
    margin-top: auto;
}
.daily-badge { font-size: 11px; font-weight: 600; color: #475569; background: #f1f5f9; padding: 2px 7px; border-radius: 4px; }
.daily-link-text { font-size: 12.5px; font-weight: 700; color: #059669; display: flex; align-items: center; gap: 3px; }
</style>

<div class="daily-hub-wrap">
    <div class="daily-header">
        <span class="daily-pill">✨ 매일 쓰는 스마트 유틸리티</span>
        <h2 class="daily-title">일상 꿀툴 모음 (Daily Tools)</h2>
        <p class="daily-desc">로그인·설치 없이 100% 브라우저에서 안전하고 빠르게 해결하는 유용한 계산기 및 편의 도구 모음입니다.</p>
    </div>

    <div class="daily-card-grid">
        <!-- Card 1: 연봉 실수령액 계산기 -->
        <a href="https://barcode128.mycafe24.com/salary-calculator/" class="daily-card">
            <div>
                <div class="daily-card-top">
                    <div class="daily-icon-box" style="background:#ecfdf5; color:#059669;">💰</div>
                    <div class="daily-meta">
                        <span class="daily-tag" style="color:#059669;">2026 최신 4대보험</span>
                        <h3 class="daily-card-title">연봉·월급 실수령액 계산기</h3>
                    </div>
                </div>
                <p class="daily-card-desc">연봉 3천~1억 원 구간별 실제 입금액, 국민연금·건강보험·소득세 공제액과 주휴수당·퇴직금을 실시간 계산합니다.</p>
            </div>
            <div class="daily-card-foot">
                <span class="daily-badge">직장인·알바생</span>
                <span class="daily-link-text">계산하기 ➔</span>
            </div>
        </a>

        <!-- Card 2: 무서버 PDF 도구 -->
        <a href="https://barcode128.mycafe24.com/pdf-tools/" class="daily-card">
            <div>
                <div class="daily-card-top">
                    <div class="daily-icon-box" style="background:#fef2f2; color:#dc2626;">📄</div>
                    <div class="daily-meta">
                        <span class="daily-tag" style="color:#dc2626;">100% 무서버 보안</span>
                        <h3 class="daily-card-title">초고속 PDF 합치기 &amp; 분할</h3>
                    </div>
                </div>
                <p class="daily-card-desc">서버 전송 없이 브라우저 메모리에서 1초 만에 여러 PDF를 하나로 병합하거나 특정 페이지만 즉시 추출합니다.</p>
            </div>
            <div class="daily-card-foot">
                <span class="daily-badge">개인정보 안심</span>
                <span class="daily-link-text" style="color:#dc2626;">도구 열기 ➔</span>
            </div>
        </a>

        <!-- Card 3: 글자수 세기 & 바이트 계산기 -->
        <a href="https://barcode128.mycafe24.com/word-counter/" class="daily-card">
            <div>
                <div class="daily-card-top">
                    <div class="daily-icon-box" style="background:#f0fdf4; color:#16a34a;">✍️</div>
                    <div class="daily-meta">
                        <span class="daily-tag" style="color:#16a34a;">EUC-KR·UTF-8</span>
                        <h3 class="daily-card-title">자소서 글자수 &amp; Byte 세기</h3>
                    </div>
                </div>
                <p class="daily-card-desc">공백 포함/제외 글자수, 공기업·취업포털 기준 Byte(2/3Byte), 맞춤법 검사기 원클릭 연동을 제공합니다.</p>
            </div>
            <div class="daily-card-foot">
                <span class="daily-badge">취준·입시 필수</span>
                <span class="daily-link-text" style="color:#16a34a;">측정하기 ➔</span>
            </div>
        </a>

        <!-- Card 4: 스마트 디데이 카운터 -->
        <a href="https://barcode128.mycafe24.com/dday-calculator/" class="daily-card">
            <div>
                <div class="daily-card-top">
                    <div class="daily-icon-box" style="background:#fff7ed; color:#ea580c;">⏳</div>
                    <div class="daily-meta">
                        <span class="daily-tag" style="color:#ea580c;">시험·커플 기념일</span>
                        <h3 class="daily-card-title">스마트 디데이 &amp; 만 나이</h3>
                    </div>
                </div>
                <p class="daily-card-desc">D-Day 계산, 100일·1주년 기념일 계산, 개정 법률 기준 대한민국 만 나이와 띠·별자리를 한눈에 확인합니다.</p>
            </div>
            <div class="daily-card-foot">
                <span class="daily-badge">기념일 계산</span>
                <span class="daily-link-text" style="color:#ea580c;">카운트 ➔</span>
            </div>
        </a>

        <!-- Card 5: 주택용 전기세 계산기 -->
        <a href="https://barcode128.mycafe24.com/electricity-calculator/" class="daily-card">
            <div>
                <div class="daily-card-top">
                    <div class="daily-icon-box" style="background:#eff6ff; color:#2563eb;">⚡</div>
                    <div class="daily-meta">
                        <span class="daily-tag" style="color:#2563eb;">한전 누진제 요율</span>
                        <h3 class="daily-card-title">주택용 전기세 계산기</h3>
                    </div>
                </div>
                <p class="daily-card-desc">월 사용량(kWh)에 따른 기본요금·전력량요금·기후환경·연료비조정액과 에어컨 가동 시 누진세 폭탄을 1초 만에 시뮬레이션합니다.</p>
            </div>
            <div class="daily-card-foot">
                <span class="daily-badge">가전 누진세 계산</span>
                <span class="daily-link-text" style="color:#2563eb;">계산하기 ➔</span>
            </div>
        </a>

        <!-- Card 6: 스마트 로또 번호 생성기 (신규 추가!) -->
        <a href="https://barcode128.mycafe24.com/lotto-generator/" class="daily-card" style="border: 1.5px solid #fde047; background: #fefce8;">
            <div>
                <div class="daily-card-top">
                    <div class="daily-icon-box" style="background:#fef08a; color:#b45309;">🍀</div>
                    <div class="daily-meta">
                        <span class="daily-tag" style="color:#b45309;">NEW · 인생 역전</span>
                        <h3 class="daily-card-title">스마트 로또 6/45 생성기</h3>
                    </div>
                </div>
                <p class="daily-card-desc">생년월일·이름·커플 궁합·휴대폰 연락처 수비학 파동 분석으로 이번 주 1등 대박 기운을 담은 맞춤 번호를 추출합니다.</p>
            </div>
            <div class="daily-card-foot">
                <span class="daily-badge" style="background:#fef08a; color:#854d0e;">맞춤 수비학</span>
                <span class="daily-link-text" style="color:#b45309;">행운 뽑기 ➔</span>
            </div>
        </a>
    </div>
</div>
"""

hub_res = requests.post(f"{wp_base}/2148", headers=headers, json={"content": clean_html(hub_html_raw)})
print(f"Daily Hub updated with 6th tool (lotto-generator): {hub_res.status_code}")
