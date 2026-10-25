import requests
import base64
import json

auth = base64.b64encode(b'barcode128:5CoX aTTH Qzr8 NJzn zLNP xvZW').decode()
headers = {
    'Authorization': 'Basic ' + auth,
    'Content-Type': 'application/json'
}
wp_base = 'https://barcode128.mycafe24.com/wp-json/wp/v2'

# 1. 위젯에 넣을 실시간 하이브리드 카운터 스크립트
counter_script = """
<script>
(function() {
    function getTodayKey() {
        const now = new Date(Date.now() + 9 * 3600 * 1000);
        return now.toISOString().slice(0, 10).replace(/-/g, '');
    }

    async function updateVisitorBadge() {
        const todayStr = getTodayKey();
        const lastVisit = localStorage.getItem('bc128_uv_date');
        const isNewVisitToday = (lastVisit !== todayStr);

        const todayKey = 'bc128_td_' + todayStr;
        const totalKey = 'bc128_tot_uv';

        const todayUrl = isNewVisitToday
            ? 'https://countapi.mileshilliard.com/api/v1/hit/' + todayKey
            : 'https://countapi.mileshilliard.com/api/v1/get/' + todayKey;

        const totalUrl = isNewVisitToday
            ? 'https://countapi.mileshilliard.com/api/v1/hit/' + totalKey
            : 'https://countapi.mileshilliard.com/api/v1/get/' + totalKey;

        try {
            const [rToday, rTotal] = await Promise.all([
                fetch(todayUrl).then(r => r.ok ? r.json() : { value: 1 }).catch(() => ({ value: 1 })),
                fetch(totalUrl).then(r => r.ok ? r.json() : { value: 1 }).catch(() => ({ value: 1 }))
            ]);

            if (isNewVisitToday) {
                localStorage.setItem('bc128_uv_date', todayStr);
            }

            const todayCount = (rToday && typeof rToday.value === 'number') ? rToday.value : 1;
            const rawTotal = (rTotal && typeof rTotal.value === 'number') ? rTotal.value : 1;
            const finalTotal = 800 + rawTotal;

            const text = '오늘 ' + todayCount.toLocaleString() + ' | 누적 ' + finalTotal.toLocaleString();

            const badgeLink = document.querySelector('.main-navigation .main-nav ul li:nth-child(3) a');
            if (badgeLink) {
                badgeLink.textContent = text;
            }
        } catch (e) {
            console.warn('Visitor counter sync error:', e);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', updateVisitorBadge);
    } else {
        updateVisitorBadge();
    }
})();
</script>
""".strip()

# 2. 기존 footer-bar 에 등록된 custom_html 위젯이 있는지 확인
widgets = requests.get(f'{wp_base}/widgets', headers=headers).json()
for w in widgets:
    if w.get('sidebar') == 'footer-bar' and w.get('id_base') == 'custom_html':
        print(f"Deleting existing footer widget: {w['id']}")
        requests.delete(f"{wp_base}/widgets/{w['id']}?force=true", headers=headers)

# 3. 신규 위젯 등록
payload = {
    'sidebar': 'footer-bar',
    'id_base': 'custom_html',
    'instance': {
        'raw': {
            'title': '',
            'content': counter_script
        }
    }
}
r_widget = requests.post(f'{wp_base}/widgets', headers=headers, json=payload)
print("Create Counter Widget Status:", r_widget.status_code)
if r_widget.status_code == 201:
    print("Widget ID:", r_widget.json()['id'])

# 4. 상단 메뉴 2205의 기본 표시 텍스트도 초기값에 맞춤 ("오늘 1 | 누적 801")
r_menu = requests.post(f'{wp_base}/menu-items/2205', headers=headers, json={
    'title': '오늘 1 | 누적 801'
})
print("Update Menu Item 2205 Default Text Status:", r_menu.status_code)

# 5. NinjaFirewall 다시 활성화
r_fw = requests.post(f'{wp_base}/plugins/ninjafirewall/ninjafirewall', headers=headers, json={'status': 'active'})
print("Reactivate NinjaFirewall Status:", r_fw.status_code)

print("Hybrid Visitor Counter Setup Complete!")
