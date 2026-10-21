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
.separate-containers .site-main {
    margin-top: 8px !important;
}
.inside-article {
    padding-top: 8px !important;
}
#left-sidebar, #right-sidebar { display: none !important; }
#primary.content-area, .site-content .content-area { width: 100% !important; max-width: 100% !important; float: none !important; }
.grid-container { max-width: 1280px !important; }
.entry-header { display: none !important; }
"""

def clean_html(h):
    h = re.sub(r'>\s+<', '><', h.strip())
    h = re.sub(r'[\r\n]+', '', h)
    return h

daily_pages = [
    {
        "slug": "salary-calculator",
        "title": "2026 연봉 실수령액 & 알바 주휴수당·퇴직금·실업급여 종합 계산기 | Barcode128",
        "iframe_url": "https://barcodeone.github.io/detail_slice_compressor/salary-calculator.html",
        "height": "1000px",
        "theme_tag": "직장인 & 알바생 스마트 데스크 추천템",
        "theme_desc": "업무 집중력과 손목 건강을 지켜주는 인기 데스크 셋업 필수 아이템입니다."
    },
    {
        "slug": "pdf-tools",
        "title": "초고속 PDF 합치기 & 페이지 분할기 (100% 무서버 개인정보 안전 툴) | Barcode128",
        "iframe_url": "https://barcodeone.github.io/detail_slice_compressor/pdf-tools.html",
        "height": "950px",
        "theme_tag": "스마트 오피스 & 문서 작업 추천 장비",
        "theme_desc": "대용량 서류 작업과 디지털 문서 업무의 효율을 극대화하는 생산성 장비입니다."
    },
    {
        "slug": "word-counter",
        "title": "자소서 글자수 세기 & 바이트(Byte) 계산기 (공백제외·EUC-KR·UTF-8) | Barcode128",
        "iframe_url": "https://barcodeone.github.io/detail_slice_compressor/word-counter.html",
        "height": "980px",
        "theme_tag": "취준생 자소서 & 학업 집중 추천템",
        "theme_desc": "장시간 문서 작성과 자기소개서 집필 시 손목 피로를 줄여주는 인기 인체공학 아이템입니다."
    },
    {
        "slug": "dday-calculator",
        "title": "스마트 디데이(D-Day) & 기념일·만나이 종합 계산기 | Barcode128",
        "iframe_url": "https://barcodeone.github.io/detail_slice_compressor/dday-calculator.html",
        "height": "950px",
        "theme_tag": "기념일 선물 & 라이프스타일 추천템",
        "theme_desc": "소중한 기념일과 특별한 순간을 더욱 기억에 남게 만들어주는 인기 라이프 기프트입니다."
    }
]

for p in daily_pages:
    slug = p["slug"]
    title = p["title"]
    iframe_url = p["iframe_url"]
    h = p["height"]
    theme_tag = p["theme_tag"]
    theme_desc = p["theme_desc"]

    raw_html = f"""<!-- wp:html -->
<style>
{SLIM_HEADER_CSS}
</style>

<div style="width:100%; max-width:1200px; margin:0 auto; padding-bottom:50px; font-family:'Pretendard', sans-serif;">
    <iframe src="{iframe_url}" style="width:100%; height:{h}; border:none; border-radius:20px; box-shadow:0 4px 20px rgba(0,0,0,0.06); margin-bottom:40px; display:block;" scrolling="auto"></iframe>

    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:24px; padding:32px; margin-top:30px;">
        <div style="margin-bottom:24px;">
            <span style="font-size:12px; font-weight:800; color:#4f46e5; text-transform:uppercase; letter-spacing:0.5px;">RECOMMENDATION</span>
            <h3 style="font-size:20px; font-weight:900; color:#0f172a; margin:4px 0 6px 0;">✨ {theme_tag} 3종</h3>
            <p style="font-size:13px; color:#64748b; margin:0;">{theme_desc}</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px;">
            <!-- Item 1 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h0uENEs7HM" target="_blank" referrerpolicy="unsafe-url"><img src="https://image7.coupangcdn.com/image/affiliate/banner/d3985e2aa9acdeaebc0258ff2cccb210@2x.jpg" alt="로지텍 무소음 무선 마우스, M331" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#eef2ff; color:#4338ca; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">조용한 클릭</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">로지텍 무소음 무선 마우스 M331 Silent</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">도서관, 사무실, 카페 어디서든 정숙한 클릭으로 소음 스트레스 없는 베스트셀러 마우스.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">로켓배송</span>
                    <a href="https://link.coupang.com/a/h0uENEs7HM" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 2 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h0uOKcDDt6" target="_blank" referrerpolicy="unsafe-url"><img src="https://img3a.coupangcdn.com/image/affiliate/banner/ba9d13b4f950386ec6c1f41768510c26@2x.jpg" alt="ValleyCraft 360도 회전 노트북 거치대" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#fef3c7; color:#b45309; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">거북목 방지</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">ValleyCraft 360도 회전 알루미늄 노트북 거치대</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">자유로운 각도와 높이 조절로 장시간 모니터 시야를 편안하게 지켜주는 풀메탈 거치대.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">만족도 1위</span>
                    <a href="https://link.coupang.com/a/h0uOKcDDt6" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 3 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h0uJyr16d2" target="_blank" referrerpolicy="unsafe-url"><img src="https://image7.coupangcdn.com/image/affiliate/banner/e96fbb37ea94982ecbf6292184130156@2x.jpg" alt="Airwit 와이드 모니터 LED 클립 조명 스탠드" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#ecfdf5; color:#047857; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">시력 보호 조명</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">Airwit 듀얼헤드 플리커프리 와이드 모니터 조명 (80cm)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">모니터 화면 반사 없이 책상 전체를 은은하고 밝게 비춰 눈의 피로를 최소화하는 와이드 램프.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">로켓배송</span>
                    <a href="https://link.coupang.com/a/h0uJyr16d2" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>
        </div>

        <p style="text-align:center; font-size:11px; color:#94a3b8; margin:24px 0 0 0;">이 포스팅은 쿠팡 파트너스 활동의 일환으로 이에 따른 일정액의 수수료를 제공받습니다.</p>
    </div>
</div>
<!-- /wp:html -->"""

    chk_res = requests.get(f"{wp_base}?slug={slug}", headers=headers)
    found = chk_res.json() if chk_res.status_code == 200 else []

    if found:
        pid = found[0]["id"]
        res = requests.post(f"{wp_base}/{pid}", headers=headers, json={"title": title, "content": clean_html(raw_html)})
        print(f"[수정 완료] {slug} (ID: {pid}) - 상태: {res.status_code}")
    else:
        res = requests.post(wp_base, headers=headers, json={"title": title, "content": clean_html(raw_html), "slug": slug, "status": "publish"})
        print(f"[생성 완료] {slug} (신규 ID: {res.json().get('id')}) - 상태: {res.status_code}")

print("\n4개 일상 도구 워드프레스 페이지 발행 완료!")
