import requests
import base64
import re

auth = base64.b64encode(b'barcode128:5CoX aTTH Qzr8 NJzn zLNP xvZW').decode()
headers = {
    'Authorization': 'Basic ' + auth,
    'Content-Type': 'application/json'
}

html_raw = """
<style>
/* 1. 사이드바 숨김 및 와이드 컨테이너 */
#left-sidebar, #right-sidebar { display: none !important; }
#primary.content-area, .site-content .content-area { width: 100% !important; max-width: 100% !important; float: none !important; }
.grid-container { max-width: 1200px !important; }
.entry-header { display: none !important; }
.inside-article { padding: 10px 16px !important; }

/* 2. 워드프레스 자동 생성 빈 P 태그 완전 차단 */
.hub-wrap p:empty, .hub-quick-list p, .tools-card-grid > p { display: none !important; margin: 0 !important; padding: 0 !important; }

/* 3. 전체 폰트 & 컨테이너 */
.hub-wrap {
    font-family: -apple-system, BlinkMacSystemFont, "Pretendard", "Segoe UI", Roboto, sans-serif;
    color: #1e293b;
    margin: 0 auto;
    max-width: 1140px;
}
.hub-header { text-align: center; padding: 24px 10px 20px 10px; }
.hub-pill { display: inline-block; padding: 5px 12px; background: #eef2ff; color: #4f46e5; font-size: 12px; font-weight: 700; border-radius: 999px; margin-bottom: 10px; }
.hub-title { font-size: 28px; font-weight: 900; color: #0f172a; margin: 0 0 8px 0; letter-spacing: -0.5px; }
.hub-subtitle { font-size: 14px; color: #64748b; margin: 0; line-height: 1.5; }

/* 4. 빠른 텍스트 1줄 리스트 */
.hub-quick-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 16px 20px;
    margin-bottom: 32px;
}
.hub-quick-title {
    font-size: 14px;
    font-weight: 800;
    color: #334155;
    margin-bottom: 10px;
}
.hub-quick-list {
    list-style: none !important;
    padding: 0 !important;
    margin: 0 !important;
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.hub-quick-item {
    margin: 0 !important;
    padding: 0 !important;
}
.hub-quick-link {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 9px 14px !important;
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 8px !important;
    text-decoration: none !important;
    transition: all 0.15s ease !important;
}
.hub-quick-link:hover {
    background: #f1f5f9 !important;
    border-color: #cbd5e1 !important;
    transform: translateX(4px) !important;
}
.hub-link-left {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 13.5px;
    color: #0f172a;
}
.hub-link-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 20px;
    height: 20px;
    background: #e2e8f0;
    color: #475569;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 800;
}
.hub-link-desc {
    color: #64748b;
    font-size: 12.5px;
}
.hub-link-btn {
    font-size: 12px;
    font-weight: 700;
    color: #4f46e5;
    white-space: nowrap;
}

/* 5. 도구 블럭 카드 3열 그리드 */
.grid-title {
    font-size: 18px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 14px;
}
.tools-card-grid {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 20px !important;
    margin-bottom: 40px !important;
}
.tool-box {
    flex: 1 1 calc(33.333% - 14px);
    min-width: 290px;
    max-width: calc(33.333% - 14px);
    box-sizing: border-box;
    background: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-radius: 16px;
    padding: 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.2s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}
.tool-box:hover {
    border-color: #6366f1;
    box-shadow: 0 10px 20px -5px rgba(99, 102, 241, 0.15);
    transform: translateY(-3px);
}
.tool-box-top { margin-bottom: 16px; }
.tool-icon-row { display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; }
.tool-emoji {
    width: 42px;
    height: 42px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}
.tool-badge-pill {
    font-size: 11px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 6px;
    background: #f1f5f9;
    color: #475569;
}
.tool-box-title { font-size: 16px; font-weight: 800; color: #0f172a; margin: 0 0 8px 0; line-height: 1.4; }
.tool-box-desc { font-size: 12.5px; color: #64748b; margin: 0; line-height: 1.6; }
.tool-go-btn {
    display: block;
    width: 100%;
    padding: 10px 0;
    text-align: center;
    background: #0f172a;
    color: #ffffff !important;
    text-decoration: none !important;
    font-size: 13px;
    font-weight: 700;
    border-radius: 8px;
    transition: all 0.2s ease;
    margin-top: 14px;
}
.tool-box:hover .tool-go-btn { background: #4f46e5; }

@media (max-width: 960px) {
    .tool-box {
        flex: 1 1 calc(50% - 10px);
        max-width: calc(50% - 10px);
    }
}
@media (max-width: 600px) {
    .tool-box {
        flex: 1 1 100%;
        max-width: 100%;
    }
    .hub-link-desc { display: none; }
}
</style>

<div class="hub-wrap">
    <div class="hub-header">
        <div class="hub-pill">⚡ 100% 무료 · 무설치 · 브라우저 즉시 실행</div>
        <h1 class="hub-title">이커머스 셀러 필수 무료 업무 도구 모음</h1>
        <p class="hub-subtitle">스마트스토어, 쿠팡, 11번가 온라인 쇼핑몰 운영에 필요한 핵심 실무 도구를 클릭 한 번으로 바로 사용하세요.</p>
    </div>

    <!-- 1. 텍스트 1줄씩 제목 & 링크 목록 -->
    <div class="hub-quick-box">
        <div class="hub-quick-title">📋 빠른 1줄 바로가기 목록</div>
        <ul class="hub-quick-list">
            <li class="hub-quick-item">
                <a href="/detail-slice-compressor/" class="hub-quick-link">
                    <span class="hub-link-left">
                        <span class="hub-link-badge">1</span>
                        <strong>✂️ 상세페이지 초고속 분할 &amp; 초경량 WebP 압축기</strong>
                        <span class="hub-link-desc">— 860px/780px 자동 분할 및 압축 ZIP 다운로드</span>
                    </span>
                    <span class="hub-link-btn">열기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/thumbnail-square/" class="hub-quick-link">
                    <span class="hub-link-left">
                        <span class="hub-link-badge">2</span>
                        <strong>🖼️ 1:1 정방형 썸네일 패딩 &amp; 스마트 누끼 변환기</strong>
                        <span class="hub-link-desc">— 1000×1000px 규격 여백 채움 및 순백색 누끼 생성</span>
                    </span>
                    <span class="hub-link-btn">열기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/barcode-generator/" class="hub-quick-link">
                    <span class="hub-link-left">
                        <span class="hub-link-badge">3</span>
                        <strong>🔢 Code 128 바코드 &amp; QR코드 일괄 생성기</strong>
                        <span class="hub-link-desc">— 로켓그로스 롤라벨(5×3, 4×2)·A4 인쇄</span>
                    </span>
                    <span class="hub-link-btn">열기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/margin-calculator/" class="hub-quick-link">
                    <span class="hub-link-left">
                        <span class="hub-link-badge">4</span>
                        <strong>🧮 스마트스토어·쿠팡 마진율 &amp; 역마진 계산기</strong>
                        <span class="hub-link-desc">— 수수료·부가세 감안 실순수익 분석 및 손실 방지</span>
                    </span>
                    <span class="hub-link-btn">열기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/ocr-keyword-extractor/" class="hub-quick-link">
                    <span class="hub-link-left">
                        <span class="hub-link-badge">5</span>
                        <strong>🔍 상세페이지 이미지 OCR 텍스트 추출 &amp; AI 태그</strong>
                        <span class="hub-link-desc">— 이미지 글자 광학인식 및 쇼핑몰 검색 태그 1초 완성</span>
                    </span>
                    <span class="hub-link-btn">열기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/title-combiner/" class="hub-quick-link">
                    <span class="hub-link-left">
                        <span class="hub-link-badge">6</span>
                        <strong>🏷️ 50자 상품명 조합기 &amp; 금지단어 필터기</strong>
                        <span class="hub-link-desc">— SEO 상위노출 50자 상품명 조합 및 상표권 검수</span>
                    </span>
                    <span class="hub-link-btn">열기 ➔</span>
                </a>
            </li>
        </ul>
    </div>

    <!-- 2. 블럭/카드 그리드 (가로 3열 정렬) -->
    <div class="grid-title">📦 도구별 상세 안내 및 실행</div>
    <div class="tools-card-grid">

        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#eef2ff;">✂️</div>
                    <span class="tool-badge-pill" style="background:#e0e7ff; color:#3730a3;">이미지 가공</span>
                </div>
                <h3 class="tool-box-title">상세페이지 분할 &amp; 초경량 압축기</h3>
                <p class="tool-box-desc">세로 10,000px 이상의 대형 상세페이지를 스마트스토어(860px)·쿠팡(780px) 규격으로 균등 분할하고 WebP 압축 후 ZIP으로 다운로드합니다.</p>
            </div>
            <a href="/detail-slice-compressor/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#fdf2f8;">🖼️</div>
                    <span class="tool-badge-pill" style="background:#fce7f3; color:#9d174d;">썸네일</span>
                </div>
                <h3 class="tool-box-title">1:1 정방형 썸네일 &amp; 스마트 누끼</h3>
                <p class="tool-box-desc">직사각형 제품 사진을 1000×1000px 정방형 비율에 맞춰 여백을 깔끔하게 채우고 오픈마켓 규격 순백색 배경 누끼를 자동 생성합니다.</p>
            </div>
            <a href="/thumbnail-square/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#ecfdf5;">🔢</div>
                    <span class="tool-badge-pill" style="background:#d1fae5; color:#065f46;">재고·물류</span>
                </div>
                <h3 class="tool-box-title">Code 128 바코드 &amp; QR 일괄 생성기</h3>
                <p class="tool-box-desc">쿠팡 로켓배송 입고 및 물류창고 바코드와 웹링크 QR코드를 일괄 생성하고 롤라벨(5×3, 4×2) 또는 A4 라벨지로 즉시 인쇄합니다.</p>
            </div>
            <a href="/barcode-generator/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#fefce8;">🧮</div>
                    <span class="tool-badge-pill" style="background:#fef08a; color:#854d0e;">수익 분석</span>
                </div>
                <h3 class="tool-box-title">마진율 &amp; 수수료·역마진 계산기</h3>
                <p class="tool-box-desc">오픈마켓 카테고리별 수수료, 배송비, 부가세를 자동 반영하여 실질 순수익을 분석하고 역마진 손실을 사전에 예방합니다.</p>
            </div>
            <a href="/margin-calculator/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#faf5ff;">🔍</div>
                    <span class="tool-badge-pill" style="background:#f3e8ff; color:#6b21a8;">OCR 분석</span>
                </div>
                <h3 class="tool-box-title">상세페이지 OCR 추출 &amp; AI 태그</h3>
                <p class="tool-box-desc">이미지 속 텍스트를 초고속 광학 인식으로 추출해 바로 복사하고, 상품 등록에 필요한 황금 검색 키워드 태그를 자동으로 추천합니다.</p>
            </div>
            <a href="/ocr-keyword-extractor/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#eff6ff;">🏷️</div>
                    <span class="tool-badge-pill" style="background:#dbeafe; color:#1e40af;">SEO 최적화</span>
                </div>
                <h3 class="tool-box-title">50자 상품명 조합기 &amp; 금지어 필터</h3>
                <p class="tool-box-desc">검색 상위 노출에 최적화된 50자 상품명을 무제한 조합하고, 상표권 침해 및 표시광고법 위반 금지단어를 실시간 검수합니다.</p>
            </div>
            <a href="/title-combiner/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

    </div>
</div>
"""

# HTML 내 모든 개행 및 공백 압축 (wpautop 완벽 우회)
html_clean = re.sub(r'>\s+<', '><', html_raw.strip())
html_clean = re.sub(r'[\r\n]+', '', html_clean)

url = "https://barcode128.mycafe24.com/wp-json/wp/v2/pages/2112"
payload = {
    "title": "이커머스 셀러 필수 무료 업무 도구 모음 (6대 솔루션) | Barcode128",
    "content": html_clean
}

res = requests.post(url, headers=headers, json=payload)
print("Response status:", res.status_code)
if res.status_code == 200:
    print("완벽하게 컴팩트 1줄 리스트 및 3열 카드 반영 완료!")
else:
    print("오류:", res.text)
