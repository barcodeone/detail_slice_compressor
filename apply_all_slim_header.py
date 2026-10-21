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
"""

tool_pages = [
    2086, 2091, 2104, 2105, 2106, 2107, 2119, 2120, 2121, 2128
]

def clean_html(h):
    h = re.sub(r'>\s+<', '><', h.strip())
    h = re.sub(r'[\r\n]+', '', h)
    return h

for pid in tool_pages:
    # Get page content in edit context
    r = requests.get(f"{wp_base}/{pid}?context=edit", headers=headers)
    if r.status_code != 200:
        print(f"Error fetching {pid}: {r.status_code}")
        continue
    data = r.json()
    title = data["title"]["raw"]
    content = data["content"]["raw"]

    if "/* 0. [옵션 A] 초슬림 미니멀 헤더 최적화 */" not in content:
        content = content.replace("<style>", f"<style>\n{SLIM_HEADER_CSS}\n", 1)
        res = requests.post(f"{wp_base}/{pid}", headers=headers, json={
            "title": title,
            "content": clean_html(content)
        })
        print(f"Page {pid} ({data['slug']}) Slim Header Applied: {res.status_code}")
    else:
        print(f"Page {pid} already has slim header.")

print("All tool pages successfully updated with Slim Header (Option A)!")
