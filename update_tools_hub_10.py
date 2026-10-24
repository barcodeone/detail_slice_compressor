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
.separate-containers .site-main {
    margin-top: 8px !important;
}
.inside-article {
    padding-top: 8px !important;
}

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
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 9px 14px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    text-decoration: none !important;
    color: #1e293b !important;
    font-size: 13px;
    transition: all 0.15s ease;
}
.hub-quick-link:hover {
    border-color: #6366f1;
    background: #fdfefe;
    transform: translateX(3px);
}
.hub-quick-left {
    display: flex;
    align-items: center;
    gap: 8px;
}
.hub-num-badge {
    background: #eef2ff;
    color: #4f46e5;
    font-weight: 800;
    font-size: 11px;
    padding: 2px 7px;
    border-radius: 4px;
}
.hub-quick-name {
    font-weight: 700;
    color: #0f172a;
}
.hub-quick-desc {
    color: #64748b;
    font-size: 12px;
}
.hub-quick-arrow {
    color: #94a3b8;
    font-weight: 700;
    font-size: 12px;
}
.hub-quick-link:hover .hub-quick-arrow {
    color: #4f46e5;
}

/* 5. 3열 카드 블럭 그리드 */
.tools-card-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    margin-top: 10px;
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
@media (max-width: 640px) {
    .tool-box {
        flex: 1 1 100%;
        max-width: 100%;
    }
    .hub-quick-desc { display: none; }
}
</style>

<div class="hub-wrap">
    <!-- Header -->
    <div class="hub-header">
        <span class="hub-pill">⚡ 100% 무료 · 무설치 · 클라이언트 사이드</span>
        <h1 class="hub-title">이커머스 셀러 필수 업무 도구 모음</h1>
        <p class="hub-subtitle">스마트스토어, 쿠팡 등 오픈마켓 판매자의 업무 시간을 획기적으로 줄여주는 10대 핵심 유틸리티입니다.</p>
        <div style="display:flex; justify-content:center; gap:8px; margin-top:14px;">
            <span style="padding:6px 14px; font-size:12px; font-weight:700; color:#475569; background:#ffffff; border:1px solid #cbd5e1; border-radius:999px; display:inline-flex; align-items:center; gap:4px; box-shadow:0 1px 3px rgba(0,0,0,0.04);">
                ⭐ 즐겨찾기 등록 (Ctrl + D)
            </span>
            <a href="https://barcode128.mycafe24.com/tools/" style="padding:6px 14px; font-size:12px; font-weight:700; color:#2563eb; background:#eff6ff; border:1px solid #bfdbfe; border-radius:999px; text-decoration:none; display:inline-flex; align-items:center; gap:4px; box-shadow:0 1px 3px rgba(37,99,235,0.08);">
                🔗 tools 링크 공유
            </a>
        </div>
    </div>

    <!-- Quick List (1줄 빠른 링크) -->
    <div class="hub-quick-box">
        <div class="hub-quick-title">📌 빠른 바로가기 (1~10번 전체 목록)</div>
        <ul class="hub-quick-list">
            <li class="hub-quick-item">
                <a href="/detail-slice-compressor/" class="hub-quick-link">
                    <div class="hub-quick-left">
                        <span class="hub-num-badge">01</span>
                        <span class="hub-quick-name">상세페이지 분할 &amp; WebP 압축기</span>
                        <span class="hub-quick-desc">– 긴 상세페이지 자동 슬라이스 분할 및 초경량 WebP/JPG 일괄 압축</span>
                    </div>
                    <span class="hub-quick-arrow">바로가기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/thumbnail-square/" class="hub-quick-link">
                    <div class="hub-quick-left">
                        <span class="hub-num-badge">02</span>
                        <span class="hub-quick-name">1:1 정방형 썸네일 &amp; 스마트 누끼기</span>
                        <span class="hub-quick-desc">– 여백 자동 패딩, 블러/그림자/배경색 채우기 및 배경 제거</span>
                    </div>
                    <span class="hub-quick-arrow">바로가기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/barcode-generator/" class="hub-quick-link">
                    <div class="hub-quick-left">
                        <span class="hub-num-badge">03</span>
                        <span class="hub-quick-name">Code 128 바코드 &amp; QR 일괄 생성기</span>
                        <span class="hub-quick-desc">– 오픈마켓 물류·송장 라벨 인쇄용 Code 128 바코드 및 QR코드 생성</span>
                    </div>
                    <span class="hub-quick-arrow">바로가기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/margin-calculator/" class="hub-quick-link">
                    <div class="hub-quick-left">
                        <span class="hub-num-badge">04</span>
                        <span class="hub-quick-name">오픈마켓 판매 마진율 &amp; 역마진 계산기</span>
                        <span class="hub-quick-desc">– 수수료, 부가세, 택배비, 포장비 원클릭 반영 순이익 및 판매가 역산</span>
                    </div>
                    <span class="hub-quick-arrow">바로가기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/ocr-keyword-extractor/" class="hub-quick-link">
                    <div class="hub-quick-left">
                        <span class="hub-num-badge">05</span>
                        <span class="hub-quick-name">상세페이지 OCR 추출 &amp; AI 태그 추천</span>
                        <span class="hub-quick-desc">– 이미지 속 텍스트 1초 복사 및 상위노출 황금 키워드 태그 자동 추출</span>
                    </div>
                    <span class="hub-quick-arrow">바로가기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/title-combiner/" class="hub-quick-link">
                    <div class="hub-quick-left">
                        <span class="hub-num-badge">06</span>
                        <span class="hub-quick-name">50자 상품명 조합기 &amp; 금지단어 필터</span>
                        <span class="hub-quick-desc">– 검색 상위 노출 50자 상품명 무제한 조합 및 상표권/과대광고 금지어 검수</span>
                    </div>
                    <span class="hub-quick-arrow">바로가기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/vat-calculator/" class="hub-quick-link">
                    <div class="hub-quick-left">
                        <span class="hub-num-badge">07</span>
                        <span class="hub-quick-name">오픈마켓 부가세(VAT) &amp; 실납부세액 계산기</span>
                        <span class="hub-quick-desc">– 공급가액 10% 분리, 일반/간이 세액 산출, 매입공제 및 신용카드 세액공제(1.3%) 시뮬레이터</span>
                    </div>
                    <span class="hub-quick-arrow">바로가기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/watermark/" class="hub-quick-link">
                    <div class="hub-quick-left">
                        <span class="hub-num-badge">08</span>
                        <span class="hub-quick-name">이미지 워터마크 자동 일괄 삽입기</span>
                        <span class="hub-quick-desc">– 상세페이지·썸네일 불펌 방지 텍스트 및 투명 로고 일괄 각인 &amp; ZIP 다운로드</span>
                    </div>
                    <span class="hub-quick-arrow">바로가기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/channel-compare/" class="hub-quick-link">
                    <div class="hub-quick-left">
                        <span class="hub-num-badge">09</span>
                        <span class="hub-quick-name">스마트스토어 vs 쿠팡 수수료 &amp; 마진 비교기</span>
                        <span class="hub-quick-desc">– 수수료율 자유 수정, 양방향 판매가 역산, 원가/수수료/마진 금액 &amp; % 동시 비교</span>
                    </div>
                    <span class="hub-quick-arrow">바로가기 ➔</span>
                </a>
            </li>
            <li class="hub-quick-item">
                <a href="/gif-maker/" class="hub-quick-link">
                    <div class="hub-quick-left">
                        <span class="hub-num-badge">10</span>
                        <span class="hub-quick-name">동영상 ➔ 초경량 고화질 GIF 움짤 생성기</span>
                        <span class="hub-quick-desc">– 스마트폰 촬영 영상 시간 구간·상품 화면 크롭 잘라내기 &amp; 스마트스토어 규격 변환</span>
                    </div>
                    <span class="hub-quick-arrow">바로가기 ➔</span>
                </a>
            </li>
        </ul>
    </div>

    <!-- Card Blocks (3열 카드 블럭) -->
    <div class="tools-card-grid">

        <!-- 1 -->
        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#eef2ff;">✂️</div>
                    <span class="tool-badge-pill" style="background:#e0e7ff; color:#4338ca;">이미지 분할</span>
                </div>
                <h3 class="tool-box-title">상세페이지 분할 &amp; 초경량 압축</h3>
                <p class="tool-box-desc">초고해상도 긴 상세페이지를 스마트스토어(860px)·쿠팡(780px) 권장 규격으로 자동 분할하고, 화질 저하 없이 WebP/JPG로 압축 패키징합니다.</p>
            </div>
            <a href="/detail-slice-compressor/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

        <!-- 2 -->
        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#f0fdf4;">🖼️</div>
                    <span class="tool-badge-pill" style="background:#dcfce7; color:#15803d;">썸네일 규격</span>
                </div>
                <h3 class="tool-box-title">1:1 정방형 썸네일 &amp; 스마트 누끼</h3>
                <p class="tool-box-desc">가로세로 비율이 제각각인 원본 상품 사진을 1:1 정사각형 1000px 규격으로 맞추고, 여백 패딩(화이트/블러/그림자) 및 배경을 자동 제거합니다.</p>
            </div>
            <a href="/thumbnail-square/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

        <!-- 3 -->
        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#f8fafc;">🏷️</div>
                    <span class="tool-badge-pill" style="background:#e2e8f0; color:#334155;">물류·라벨</span>
                </div>
                <h3 class="tool-box-title">Code 128 바코드 &amp; QR 일괄 생성</h3>
                <p class="tool-box-desc">엑셀에서 품번을 붙여넣으면 유포감열 롤라벨(50×30mm) 규격의 Code 128 물류 바코드와 QR코드를 한 번에 일괄 생성 및 인쇄합니다.</p>
            </div>
            <a href="/barcode-generator/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

        <!-- 4 -->
        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#fefce8;">💰</div>
                    <span class="tool-badge-pill" style="background:#fef08a; color:#854d0e;">손익 분석</span>
                </div>
                <h3 class="tool-box-title">오픈마켓 마진율 &amp; 역마진 계산기</h3>
                <p class="tool-box-desc">판매가와 사입원가만 넣으면 오픈마켓 수수료, 부가세, 택배비, 포장비를 공제한 순이익과 마진율을 즉시 확인하고 목표 마진 판매가를 역산합니다.</p>
            </div>
            <a href="/margin-calculator/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

        <!-- 5 -->
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

        <!-- 6 -->
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

        <!-- 7: 부가세 계산기 -->
        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#dbeafe;">🧾</div>
                    <span class="tool-badge-pill" style="background:#bfdbfe; color:#1e3a8a;">세무·정산</span>
                </div>
                <h3 class="tool-box-title">오픈마켓 부가세 &amp; 실납부세액 계산기</h3>
                <p class="tool-box-desc">공급가액 10% 1초 분리, 일반/간이과세자 세액 산출, 사입·수수료 매입세액 및 신용카드 세액공제(1.3%) 시뮬레이터를 제공합니다.</p>
            </div>
            <a href="/vat-calculator/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

        <!-- 8: 워터마크 자동 삽입기 -->
        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#cffafe;">🛡️</div>
                    <span class="tool-badge-pill" style="background:#a5f3fc; color:#0e7490;">저작권 보호</span>
                </div>
                <h3 class="tool-box-title">이미지 워터마크 자동 일괄 삽입기</h3>
                <p class="tool-box-desc">상세페이지와 썸네일에 텍스트 및 투명 로고를 다중 위치 또는 격자 타일링으로 일괄 각인하고 ZIP으로 다운로드합니다.</p>
            </div>
            <a href="/watermark/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

        <!-- 9: 스마트스토어 vs 쿠팡 수수료 마진 비교기 -->
        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#fef3c7;">⚖️</div>
                    <span class="tool-badge-pill" style="background:#fde68a; color:#92400e;">채널 비교</span>
                </div>
                <h3 class="tool-box-title">스마트스토어 vs 쿠팡 수수료·마진 비교</h3>
                <p class="tool-box-desc">수수료율 자유 수정, 양방향 판매가 역산, 원가/수수료/마진을 금액과 %로 한눈에 대조하여 가장 이득인 입점 채널을 판별합니다.</p>
            </div>
            <a href="/channel-compare/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

        <!-- 10: 동영상 to 초경량 GIF 움짤 생성기 -->
        <div class="tool-box">
            <div class="tool-box-top">
                <div class="tool-icon-row">
                    <div class="tool-emoji" style="background:#fce7f3;">🎬</div>
                    <span class="tool-badge-pill" style="background:#fbcfe8; color:#9d174d;">전환율 극대화</span>
                </div>
                <h3 class="tool-box-title">동영상 ➔ 초경량 GIF 움짤 생성기</h3>
                <p class="tool-box-desc">스마트폰 촬영 영상을 원하는 시간 구간 &amp; 상품 화면만 드래그로 잘라내어, 네이버·쿠팡 규격의 고화질 움짤로 1초 만에 변환합니다.</p>
            </div>
            <a href="/gif-maker/" class="tool-go-btn">도구 실행하기 ➔</a>
        </div>

    </div>

    <!-- 검색엔진 최적화(SEO) 가이드 및 FAQ 아코디언 -->
    <div style="margin-top:50px; background:#ffffff; border:1px solid #e2e8f0; border-radius:24px; padding:36px; box-shadow:0 4px 16px rgba(0,0,0,0.02);">
        <div style="margin-bottom:24px; border-bottom:1px solid #f1f5f9; padding-bottom:16px;">
            <span style="font-size:12px; font-weight:800; color:#2563eb; text-transform:uppercase; letter-spacing:0.5px;">SELLER GUIDE &amp; FAQ</span>
            <h2 style="font-size:22px; font-weight:900; color:#0f172a; margin:6px 0 8px 0; line-height:1.35;">📦 이커머스 셀러 필수 업무 도구 100% 활용 가이드</h2>
            <p style="font-size:13.5px; color:#64748b; margin:0; line-height:1.6;">스마트스토어, 쿠팡, 11번가, G마켓 등 오픈마켓 판매자들을 위한 무설치 무료 업무 자동화 솔루션 안내입니다.</p>
        </div>

        <div style="color:#334155; font-size:14.5px; line-height:1.75;">
            <h3 style="font-size:16.5px; font-weight:800; color:#0f172a; margin:22px 0 8px 0;">⚡ 1. 서버 전송 없는 100% 안전한 클라이언트 사이드 연산</h3>
            <p style="margin:0 0 14px 0;">본 도구 모음의 모든 기능(상세페이지 분할, 썸네일 누끼, 바코드 생성, 마진 계산 등)은 사용자의 웹브라우저 메모리 안에서만 처리됩니다. 업로드한 상품 이미지나 매출 데이터가 외부 서버로 전송되거나 저장되지 않으므로, 유출 걱정 없이 안전하게 이용하실 수 있습니다.</p>

            <h3 style="font-size:16.5px; font-weight:800; color:#0f172a; margin:22px 0 8px 0;">🚀 2. 상품 등록 시간 80% 단축과 마진 극대화</h3>
            <p style="margin:0 0 14px 0;">포토샵 없이도 긴 상세페이지를 슬라이스 단위로 자동 분할하고 WebP 압축하여 로딩 속도를 최적화합니다. 또한 복잡한 마켓 수수료와 부가세, 배송비를 1초 만에 자동 계산하여 역마진을 방지합니다.</p>

            <h3 style="font-size:16.5px; font-weight:800; color:#0f172a; margin:26px 0 12px 0;">❓ 자주 묻는 질문 (FAQ)</h3>
            <div style="display:flex; flex-direction:column; gap:10px;">
                <details style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:14px 18px; cursor:pointer;" open>
                    <summary style="font-size:14px; font-weight:800; color:#0f172a; outline:none;">Q. 이용료나 설치 프로그램이 필요한가요?</summary>
                    <p style="font-size:13px; color:#475569; margin:8px 0 0 0; line-height:1.6;">별도의 회원가입, 로그인, 프로그램 설치 없이 웹브라우저에서 100% 무료로 즉시 실행하실 수 있습니다.</p>
                </details>
                <details style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:14px 18px; cursor:pointer;">
                    <summary style="font-size:14px; font-weight:800; color:#0f172a; outline:none;">Q. 생성된 바코드나 이미지 규격이 네이버·쿠팡에 호환되나요?</summary>
                    <p style="font-size:13px; color:#475569; margin:8px 0 0 0; line-height:1.6;">네, 스마트스토어 1000x1000 썸네일 규격과 표준 Code 128 바코드, 고품질 WebP/JPG 규격을 완벽히 준수합니다.</p>
                </details>
            </div>
        </div>
    </div>
</div>
"""

html_clean = re.sub(r'>\s+<', '><', html_raw.strip())
html_clean = re.sub(r'[\r\n]+', '', html_clean)

url = "https://barcode128.mycafe24.com/wp-json/wp/v2/pages/2112"
payload = {
    "title": "이커머스 셀러 필수 무료 업무 도구 모음 (10대 솔루션) | Barcode128",
    "content": html_clean
}

res = requests.post(url, headers=headers, json=payload)
print("Tools Hub 10-tools Update Status:", res.status_code)
