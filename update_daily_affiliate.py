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

# 1. Page 2143: Salary Calculator
salary_html = f"""<!-- wp:html -->
<style>{SLIM_HEADER_CSS}</style>
<div style="width:100%; max-width:1200px; margin:0 auto; padding-bottom:50px; font-family:'Pretendard', sans-serif;">
    <iframe src="https://barcodeone.github.io/detail_slice_compressor/salary-calculator.html" style="width:100%; height:1000px; border:none; border-radius:20px; box-shadow:0 4px 20px rgba(0,0,0,0.06); margin-bottom:40px; display:block;" scrolling="auto"></iframe>

    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:24px; padding:32px; margin-top:30px;">
        <div style="margin-bottom:24px;">
            <span style="font-size:12px; font-weight:800; color:#4f46e5; text-transform:uppercase; letter-spacing:0.5px;">RECOMMENDATION</span>
            <h3 style="font-size:20px; font-weight:900; color:#0f172a; margin:4px 0 6px 0;">💼 직장인 &amp; 알바생 건강·피로회복 필수 추천템 3종</h3>
            <p style="font-size:13px; color:#64748b; margin:0;">장시간 근무 시 손목 건강과 피로 회복을 돕는 직장인·수험생 인기 베스트셀러입니다.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px;">
            <!-- Item 1: 루베리코 메모리폼 마우스 키보드 손목 쿠션 패드 세트 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h2eu4UOvDg" target="_blank" referrerpolicy="unsafe-url"><img src="https://image11.coupangcdn.com/image/affiliate/banner/2e0c72c4d21564f9e0c9422aa3411fe4@2x.jpg" alt="루베리코 메모리폼 마우스 키보드 손목 쿠션 패드 세트, 1세트, 블랙" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#eef2ff; color:#4338ca; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">손목 터널 증후군 예방</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">루베리코 메모리폼 키보드·마우스 손목 쿠션 패드 세트</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">고밀도 메모리폼으로 장시간 타이핑과 마우스 작업 시 손목 꺾임을 방지하고 압력을 완화.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">로켓배송</span>
                    <a href="https://link.coupang.com/a/h2eu4UOvDg" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 2: 대용량 텀블러 차량용 1.18L 보온 보냉 빨대 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h2eAKnjhU4" target="_blank" referrerpolicy="unsafe-url"><img src="https://image13.coupangcdn.com/image/affiliate/banner/0e5efdc6620e856bfe5deba1a85de06a@2x.jpg" alt="대용량 텀블러 차량용 1.18L 보온 보냉 빨대, 1개, 1200ml, 크림베이지" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#fef3c7; color:#b45309; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">하루 물 섭취 완벽</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">대용량 보온보냉 빨대 텀블러 1.18L (차량 컵홀더 호환)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">사무실과 차량 어디서든 얼음이 하루 종일 유지되는 대용량 스트로우 스테인리스 텀블러.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">만족도 1위</span>
                    <a href="https://link.coupang.com/a/h2eAKnjhU4" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 3: 아임비타 멀티비타민 데일리, 60정 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h2eDfRcTTN" target="_blank" referrerpolicy="unsafe-url"><img src="https://img2c.coupangcdn.com/image/affiliate/banner/30ed99b8dd896509d0bce8fbc939eb50@2x.jpg" alt="아임비타 멀티비타민 데일리, 60정, 1개" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#ecfdf5; color:#047857; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">고함량 활력 충전</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">종근당건강 아임비타 멀티비타민 데일리 (60정/2달분)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">비타민B군 4,000% 고함량 배합으로 야근과 학업에 지친 직장인·수험생 필수 에너지 비타민.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">로켓배송</span>
                    <a href="https://link.coupang.com/a/h2eDfRcTTN" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>
        </div>
        <p style="text-align:center; font-size:11px; color:#94a3b8; margin:24px 0 0 0;">이 포스팅은 쿠팡 파트너스 활동의 일환으로 이에 따른 일정액의 수수료를 제공받습니다.</p>
    </div>
</div>
<!-- /wp:html -->"""

# 2. Page 2144: PDF Tools
pdf_html = f"""<!-- wp:html -->
<style>{SLIM_HEADER_CSS}</style>
<div style="width:100%; max-width:1200px; margin:0 auto; padding-bottom:50px; font-family:'Pretendard', sans-serif;">
    <iframe src="https://barcodeone.github.io/detail_slice_compressor/pdf-tools.html" style="width:100%; height:950px; border:none; border-radius:20px; box-shadow:0 4px 20px rgba(0,0,0,0.06); margin-bottom:40px; display:block;" scrolling="auto"></iframe>

    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:24px; padding:32px; margin-top:30px;">
        <div style="margin-bottom:24px;">
            <span style="font-size:12px; font-weight:800; color:#4f46e5; text-transform:uppercase; letter-spacing:0.5px;">RECOMMENDATION</span>
            <h3 style="font-size:20px; font-weight:900; color:#0f172a; margin:4px 0 6px 0;">📄 스마트 오피스 서류 정리 &amp; 디지털 백업 추천 장비 3종</h3>
            <p style="font-size:13px; color:#64748b; margin:0;">대용량 문서 보관, 스캔 및 서류 정리를 가장 빠르고 깔끔하게 해결하는 사무 필수 아이템입니다.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px;">
            <!-- Item 1: 초고속 2TB USB 3.0 대용량 플래시 메모리 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h2eJ6ZwOU8" target="_blank" referrerpolicy="unsafe-url"><img src="https://image7.coupangcdn.com/image/affiliate/banner/5d8150632c69874cb38c8a26618af281@2x.jpg" alt="초고속 대용량 USB 메모리 플래시 메모리" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#eef2ff; color:#4338ca; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">초고속 대용량 백업</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">USB 3.0 초고속 대용량 메탈 플래시 드라이브 (512GB)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">중요 PDF 문서, 고화질 사진 및 대용량 업무 파일을 번개처럼 빠른 속도로 안전하게 백업.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">가성비 최고</span>
                    <a href="https://link.coupang.com/a/h2eJ6ZwOU8" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 2: 컴스 휴대용 무선 스캐너 핸디형, BD217 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h2eMcIcHe0" target="_blank" referrerpolicy="unsafe-url"><img src="https://img1a.coupangcdn.com/image/affiliate/banner/b29a71a91f678e47f939e538531d3dce@2x.jpg" alt="컴스 휴대용 무선 스캐너 핸디형, BD217" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#fef3c7; color:#b45309; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">문서 원클릭 PDF 스캔</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">컴스 핸디형 무선 휴대용 스캐너 (A4 문서/도서 스캔)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">두꺼운 책이나 서류 위를 슥 긁기만 하면 고해상도 PDF/JPG로 즉시 저장되는 휴대용 무선 스캐너.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">로켓배송</span>
                    <a href="https://link.coupang.com/a/h2eMcIcHe0" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 3: 대용량 25포켓 아코디언 파일 정리함 서류꽂이 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h2eOdoCHdI" target="_blank" referrerpolicy="unsafe-url"><img src="https://img3c.coupangcdn.com/image/affiliate/banner/b5b68154eb24e2d926702182b8c58b94@2x.jpg" alt="대용량 25포켓 아코디언 파일 정리함 서류꽂이, 25단, 투명 레인보우" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#ecfdf5; color:#047857; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">서류 1초 분류 정리</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">대용량 25포켓 인덱스 아코디언 서류 파일함 (25단)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">계약서, 영수증, 등본 등 어지러운 A4 서류를 25개 컬러 인덱스로 완벽하게 분류 보관.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">만족도 1위</span>
                    <a href="https://link.coupang.com/a/h2eOdoCHdI" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>
        </div>
        <p style="text-align:center; font-size:11px; color:#94a3b8; margin:24px 0 0 0;">이 포스팅은 쿠팡 파트너스 활동의 일환으로 이에 따른 일정액의 수수료를 제공받습니다.</p>
    </div>
</div>
<!-- /wp:html -->"""

# 3. Page 2145: Word Counter
word_html = f"""<!-- wp:html -->
<style>{SLIM_HEADER_CSS}</style>
<div style="width:100%; max-width:1200px; margin:0 auto; padding-bottom:50px; font-family:'Pretendard', sans-serif;">
    <iframe src="https://barcodeone.github.io/detail_slice_compressor/word-counter.html" style="width:100%; height:980px; border:none; border-radius:20px; box-shadow:0 4px 20px rgba(0,0,0,0.06); margin-bottom:40px; display:block;" scrolling="auto"></iframe>

    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:24px; padding:32px; margin-top:30px;">
        <div style="margin-bottom:24px;">
            <span style="font-size:12px; font-weight:800; color:#4f46e5; text-transform:uppercase; letter-spacing:0.5px;">RECOMMENDATION</span>
            <h3 style="font-size:20px; font-weight:900; color:#0f172a; margin:4px 0 6px 0;">✍️ 취준생 자소서 집필 &amp; 작가 타이핑 몰입 장비 3종</h3>
            <p style="font-size:13px; color:#64748b; margin:0;">장시간 자기소개서와 블로그 글 작성 시 피로를 덜어주고 작업 능률을 200% 올려주는 타이핑 장비입니다.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px;">
            <!-- Item 1: 지클릭커 풀윤활 무소음 기계식 키보드 WK107 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h2eQciV09I" target="_blank" referrerpolicy="unsafe-url"><img src="https://image11.coupangcdn.com/image/affiliate/banner/7a47e7fca2daa922efb576d7173628d4@2x.jpg" alt="지클릭커 풀윤활 무소음 기계식 키보드 WK107" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#eef2ff; color:#4338ca; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">도각도각 무소음 타건</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">지클릭커 WK107 풀윤활 무소음 무선 블루투스 기계식 키보드</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">카페나 독서실에서도 조용하게! 공장 풀윤활 몽돌 특주축으로 깃털처럼 가벼운 손목 피로 제로 타건감.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">로켓배송</span>
                    <a href="https://link.coupang.com/a/h2eQciV09I" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 2: 홈플래닛 탁상용 태블릿PC 스탠드 거치대 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h2eS2m3QmO" target="_blank" referrerpolicy="unsafe-url"><img src="https://img1a.coupangcdn.com/image/affiliate/banner/c9ca5410894d8fa90fa0169d170c91cc@2x.jpg" alt="홈플래닛 탁상용 태블릿PC 스탠드 거치대" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#fef3c7; color:#b45309; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">자료 대조 최적 시야각</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">홈플래닛 알루미늄 탁상용 태블릿·스마트폰 스탠드 거치대</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">자소서 작성 시 태블릿이나 폰으로 이력서·채용공고를 띄워두고 한눈에 대조할 수 있는 튼튼한 거치대.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">가성비 1위</span>
                    <a href="https://link.coupang.com/a/h2eS2m3QmO" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 3: 킵스온 고탄력 통기성 압박조절 손목보호대 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h2eVkSRdHo" target="_blank" referrerpolicy="unsafe-url"><img src="https://img4c.coupangcdn.com/image/affiliate/banner/04be154799b41c9b2cdd70acdfd91928@2x.jpg" alt="킵스온 고탄력 통기성 압박조절 손목보호대, 블랙, 1세트" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#ecfdf5; color:#047857; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">타이핑 손목 통증 해소</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">킵스온 고탄력 통기성 압박조절 손목보호대 (좌우 세트)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">매일 수천 자를 타이핑할 때 시큰거리는 손목 인대를 편안하게 지지해주는 초경량 메쉬 보호대.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">로켓배송</span>
                    <a href="https://link.coupang.com/a/h2eVkSRdHo" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>
        </div>
        <p style="text-align:center; font-size:11px; color:#94a3b8; margin:24px 0 0 0;">이 포스팅은 쿠팡 파트너스 활동의 일환으로 이에 따른 일정액의 수수료를 제공받습니다.</p>
    </div>
</div>
<!-- /wp:html -->"""

# 4. Page 2146: D-Day Calculator
dday_html = f"""<!-- wp:html -->
<style>{SLIM_HEADER_CSS}</style>
<div style="width:100%; max-width:1200px; margin:0 auto; padding-bottom:50px; font-family:'Pretendard', sans-serif;">
    <iframe src="https://barcodeone.github.io/detail_slice_compressor/dday-calculator.html" style="width:100%; height:950px; border:none; border-radius:20px; box-shadow:0 4px 20px rgba(0,0,0,0.06); margin-bottom:40px; display:block;" scrolling="auto"></iframe>

    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:24px; padding:32px; margin-top:30px;">
        <div style="margin-bottom:24px;">
            <span style="font-size:12px; font-weight:800; color:#4f46e5; text-transform:uppercase; letter-spacing:0.5px;">RECOMMENDATION</span>
            <h3 style="font-size:20px; font-weight:900; color:#0f172a; margin:4px 0 6px 0;">💖 소중한 D-Day &amp; 기념일·여행 추천 아이템 3종</h3>
            <p style="font-size:13px; color:#64748b; margin:0;">기억하고 싶은 기념일 선물부터 시험 D-Day 집중 타이머, 설레는 여행 압축팩까지 맞춤 추천합니다.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px;">
            <!-- Item 1: 커스텀 무드등 주문제작 아크릴 조명 UV프린팅 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h2eX8MKCoS" target="_blank" referrerpolicy="unsafe-url"><img src="https://image15.coupangcdn.com/image/affiliate/banner/93ba65f1e9cd3679e426ecf885c743d2@2x.jpg" alt="커스텀 무드등 주문제작 아크릴 조명 UV프린팅" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#eef2ff; color:#4338ca; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">기념일 감동 선물 1위</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">커스텀 주문제작 사진 아크릴 LED 무드등 액자 조명</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">100일/1주년 커플 사진, 가족 기념사진을 은은한 LED 무드등으로 영원히 간직하는 맞춤 감성 선물.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">주문제작</span>
                    <a href="https://link.coupang.com/a/h2eX8MKCoS" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 2: 오더블유씨 스터디 타이머 OT1647T -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h2e189tPIO" target="_blank" referrerpolicy="unsafe-url"><img src="https://img3c.coupangcdn.com/image/affiliate/banner/cda458ce457f7ac6481f381b85d8dff7@2x.jpg" alt="오더블유씨 스터디 타이머 OT1647T" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#fef3c7; color:#b45309; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">시험 D-Day 집중력 향상</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">오더블유씨(OWC) 수험생 시험 전용 디지털 스터디 타이머</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">수능, 공무원, 자격증 시험을 위한 카운트다운 D-Day 및 무음 진동 알람 스톱워치.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">로켓배송</span>
                    <a href="https://link.coupang.com/a/h2e189tPIO" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 3: 태르아 부피순삭 여행용 압축 파우치 4종 세트 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h2e6XkdUfQ" target="_blank" referrerpolicy="unsafe-url"><img src="https://img1c.coupangcdn.com/image/affiliate/banner/1724c8da5a9f4e01ce70cb80cc61ac7f@2x.jpg" alt="태르아 부피순삭 여행용 압축 파우치 4종 세트" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#ecfdf5; color:#047857; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">여행 짐 부피 50% 절약</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">태르아 부피순삭 이중지퍼 여행용 옷 압축 파우치 (4종 세트)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">청소기 없이 지퍼만 잠그면 두꺼운 겨울옷과 여행 짐 부피를 절반으로 압축해 주는 캐리어 필수품.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">로켓배송</span>
                    <a href="https://link.coupang.com/a/h2e6XkdUfQ" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>
        </div>
        <p style="text-align:center; font-size:11px; color:#94a3b8; margin:24px 0 0 0;">이 포스팅은 쿠팡 파트너스 활동의 일환으로 이에 따른 일정액의 수수료를 제공받습니다.</p>
    </div>
</div>
<!-- /wp:html -->"""

updates = [
    (2143, "salary-calculator", "2026 연봉 실수령액 & 알바 주휴수당·퇴직금·실업급여 종합 계산기 | Barcode128", salary_html),
    (2144, "pdf-tools", "초고속 PDF 합치기 & 페이지 분할기 (100% 무서버 개인정보 안전 툴) | Barcode128", pdf_html),
    (2145, "word-counter", "자소서 글자수 세기 & 바이트(Byte) 계산기 (공백제외·EUC-KR·UTF-8) | Barcode128", word_html),
    (2146, "dday-calculator", "스마트 디데이(D-Day) & 기념일·만나이 종합 계산기 | Barcode128", dday_html)
]

for pid, slug, title, h in updates:
    res = requests.post(f"{wp_base}/{pid}", headers=headers, json={"title": title, "content": clean_html(h)})
    print(f"Page {pid} ({slug}) Coupang 3-item Update Status: {res.status_code}")

print("\n4개 일상 도구 쿠팡 배너 12종 100% 매칭 완료!")
