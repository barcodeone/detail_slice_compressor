import requests
import base64
import re

auth = base64.b64encode(b'barcode128:5CoX aTTH Qzr8 NJzn zLNP xvZW').decode()
headers = {
    'Authorization': 'Basic ' + auth,
    'Content-Type': 'application/json'
}
wp_base = "https://barcode128.mycafe24.com/wp-json/wp/v2/pages"

TOOL_SLUG = "gif-maker"
TOOL_TITLE = "스마트스토어·쿠팡 상세페이지 동영상 움짤(GIF) 생성기 | 구간·화면 자르기 & 초경량 압축 툴"
IFRAME_URL = "https://barcodeone.github.io/detail_slice_compressor/gif-maker.html"
IFRAME_HEIGHT = "1050px"

raw_content = f"""<!-- wp:html -->
<style>
#left-sidebar, #right-sidebar {{ display: none !important; }}
#primary.content-area, .site-content .content-area {{ width: 100% !important; max-width: 100% !important; float: none !important; }}
.grid-container {{ max-width: 1280px !important; }}
.inside-article {{ padding: 10px 16px !important; }}
.entry-header {{ display: none !important; }}
</style>

<div style="width:100%; max-width:1200px; margin:0 auto; padding-bottom:50px; font-family:'Pretendard', sans-serif;">
    <!-- Iframe Tool Embed -->
    <iframe src="{IFRAME_URL}" style="width:100%; height:{IFRAME_HEIGHT}; border:none; border-radius:20px; box-shadow:0 4px 20px rgba(0,0,0,0.06); margin-bottom:40px; display:block;" scrolling="auto"></iframe>

    <!-- Bottom Recommendation Section -->
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:24px; padding:32px; margin-top:30px;">
        <div style="margin-bottom:24px;">
            <span style="font-size:12px; font-weight:800; color:#4f46e5; text-transform:uppercase; letter-spacing:0.5px;">SELLER RECOMMENDATION</span>
            <h3 style="font-size:20px; font-weight:900; color:#0f172a; margin:4px 0 6px 0;">🎬 흔들림 제로! 상세페이지 동영상 &amp; 움짤 촬영 추천 장비 3종</h3>
            <p style="font-size:13px; color:#64748b; margin:0;">스마트폰으로도 방송국 수준의 부드러운 제품 작동 시연과 언박싱 영상을 연출하는 필수 촬영 장비입니다.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:20px;">
            
            <!-- Item 1: 대한 촬영용 자동 회전판 빅 턴테이블 42cm -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h1Ns14NWkS" target="_blank" referrerpolicy="unsafe-url"><img src="https://image7.coupangcdn.com/image/affiliate/banner/c3ac6d73a640c90d622935faf29fa8d7@2x.jpg" alt="대한 촬영용 자동 회전판 빅 턴테이블 42cm, 1개, DH-BTT42" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#eef2ff; color:#4338ca; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">360도 무소음 회전</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">대한 촬영용 자동 전동 턴테이블 42cm (DH-BTT42)</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">상품을 올려두기만 하면 360도 매끄럽게 회전하여 입체적인 3D 움짤 영상을 손쉽게 촬영 가능.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">로켓배송</span>
                    <a href="https://link.coupang.com/a/h1Ns14NWkS" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 2: 코멧 탁상용 링라이트 + 삼각대 세트 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h1Nv7spZDM" target="_blank" referrerpolicy="unsafe-url"><img src="https://img2a.coupangcdn.com/image/affiliate/banner/5a0060a518c73c9e803aafd6af8d0f5e@2x.jpg" alt="코멧 탁상용 링라이트 + 삼각대 세트, YT-1016, 1세트" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#fef3c7; color:#b45309; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">그림자 제로 조명</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">코멧 탁상용 LED 링라이트 + 삼각대 세트 YT-1016</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">영상 촬영 시 어두운 실내에서도 선명한 화질을 보장하는 3색광 밝기 조절 링라이트 삼각대.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">가성비 1위</span>
                    <a href="https://link.coupang.com/a/h1Nv7spZDM" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

            <!-- Item 3: APEXEL 스마트폰 카메라 망원/광각 렌즈 세트 -->
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:18px; padding:22px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
                <div>
                    <div style="display:flex; justify-content:center; align-items:center; height:240px; margin-bottom:14px; background:#fafafa; border-radius:12px; overflow:hidden;">
                        <a href="https://link.coupang.com/a/h1NzQIVz7Q" target="_blank" referrerpolicy="unsafe-url"><img src="https://image1.coupangcdn.com/image/affiliate/banner/d4dc36bbade6d8e12ff42bcc3e54e3e7@2x.jpg" alt="휴대폰 카메라 렌즈 광각렌즈 스마트폰 망원렌즈 APEXEL HD 2x" width="120" height="240" style="object-fit:contain;"></a>
                    </div>
                    <span style="font-size:11px; font-weight:700; background:#ecfdf5; color:#047857; padding:3px 8px; border-radius:6px; display:inline-block; margin-bottom:8px;">고선명 인물·상품 렌즈</span>
                    <h4 style="font-size:15px; font-weight:800; color:#0f172a; margin:0 0 6px 0; line-height:1.4;">APEXEL 스마트폰 HD 2x 전문가용 인물·상품 카메라 렌즈</h4>
                    <p style="font-size:12.5px; color:#64748b; margin:0; line-height:1.5;">왜곡 없는 선명한 줌 배율과 자연스러운 배경 흐림(아웃포커싱) 효과로 고화질 상품 영상 촬영.</p>
                </div>
                <div style="margin-top:16px; padding-top:12px; border-top:1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-size:11.5px; font-weight:700; color:#0f172a;">전문가 추천</span>
                    <a href="https://link.coupang.com/a/h1NzQIVz7Q" target="_blank" referrerpolicy="unsafe-url" style="padding:7px 14px; background:#0f172a; color:#ffffff; font-size:12px; font-weight:700; border-radius:8px; text-decoration:none;">상품 보기 ➔</a>
                </div>
            </div>

        </div>

        <p style="text-align:center; font-size:11px; color:#94a3b8; margin:24px 0 0 0;">이 포스팅은 쿠팡 파트너스 활동의 일환으로 이에 따른 일정액의 수수료를 제공받습니다.</p>
    </div>
</div>
<!-- /wp:html -->"""

def clean_html(h):
    h = re.sub(r'>\s+<', '><', h.strip())
    h = re.sub(r'[\r\n]+', '', h)
    return h

clean_content = clean_html(raw_content)

chk_res = requests.get(f"{wp_base}?slug={TOOL_SLUG}", headers=headers)
existing_pages = chk_res.json() if chk_res.status_code == 200 else []

if existing_pages:
    page_id = existing_pages[0]["id"]
    res = requests.post(f"{wp_base}/{page_id}", headers=headers, json={
        "title": TOOL_TITLE,
        "content": clean_content
    })
    print(f"[수정 완료] {TOOL_SLUG} (ID: {page_id}) - 상태: {res.status_code}")
else:
    res = requests.post(wp_base, headers=headers, json={
        "title": TOOL_TITLE,
        "content": clean_content,
        "slug": TOOL_SLUG,
        "status": "publish"
    })
    new_id = res.json().get("id")
    print(f"[생성 완료] {TOOL_SLUG} (신규 ID: {new_id}) - 상태: {res.status_code}")
