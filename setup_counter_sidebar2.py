import requests
import base64

auth = base64.b64encode(b'barcode128:5CoX aTTH Qzr8 NJzn zLNP xvZW').decode()
headers = {
    'Authorization': 'Basic ' + auth,
    'Content-Type': 'application/json'
}
wp_base = 'https://barcode128.mycafe24.com/wp-json/wp/v2'

# 1. NinjaFirewall 일시 비활성화
requests.post(f'{wp_base}/plugins/ninjafirewall/ninjafirewall', headers=headers, json={'status': 'inactive'})

# 2. 카운터 스크립트 (KST 기준 오늘 날짜 키 + 전체 누적 키, 800 + 누적)
counter_script = """
<script>
(function() {
    function getTodayKey() {
        var now = new Date(Date.now() + 9 * 3600 * 1000);
        return now.toISOString().slice(0, 10).replace(/-/g, '');
    }

    async function syncCounter() {
        try {
            var todayStr = getTodayKey();
            var lastVisit = localStorage.getItem('bc128_uv_date');
            var isNewToday = (lastVisit !== todayStr);

            var todayKey = 'bc128_td_' + todayStr;
            var totalKey = 'bc128_tot_uv';

            var tdUrl = isNewToday
                ? 'https://countapi.mileshilliard.com/api/v1/hit/' + todayKey
                : 'https://countapi.mileshilliard.com/api/v1/get/' + todayKey;

            var totUrl = isNewToday
                ? 'https://countapi.mileshilliard.com/api/v1/hit/' + totalKey
                : 'https://countapi.mileshilliard.com/api/v1/get/' + totalKey;

            var resArr = await Promise.all([
                fetch(tdUrl).then(function(r) { return r.ok ? r.json() : null; }).catch(function() { return null; }),
                fetch(totUrl).then(function(r) { return r.ok ? r.json() : null; }).catch(function() { return null; })
            ]);

            if (isNewToday) {
                localStorage.setItem('bc128_uv_date', todayStr);
            }

            var tdVal = (resArr[0] && typeof resArr[0].value === 'number') ? resArr[0].value : 1;
            var totVal = (resArr[1] && typeof resArr[1].value === 'number') ? resArr[1].value : 1;
            var finalTotal = 800 + totVal;

            var text = '오늘 ' + tdVal.toLocaleString() + ' | 누적 ' + finalTotal.toLocaleString();

            var badge = document.querySelector('.main-navigation .main-nav ul li:nth-child(3) a');
            if (badge) {
                badge.textContent = text;
            }
        } catch (e) {
            console.warn('Counter err:', e);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', syncCounter);
    } else {
        syncCounter();
    }
})();
</script>
""".strip()

# 3. 기존 custom_html 위젯 정리
widgets = requests.get(f'{wp_base}/widgets', headers=headers).json()
for w in widgets:
    if w.get('id_base') == 'custom_html':
        requests.delete(f"{wp_base}/widgets/{w['id']}?force=true", headers=headers)

# 4. sidebar-2 (Left Sidebar)에 위젯 생성
payload = {
    'sidebar': 'sidebar-2',
    'id_base': 'custom_html',
    'instance': {
        'raw': {
            'title': '',
            'content': counter_script
        }
    }
}
r_widget = requests.post(f'{wp_base}/widgets', headers=headers, json=payload)
print("Create widget in sidebar-2 status:", r_widget.status_code)
if r_widget.status_code == 201:
    print("Widget ID:", r_widget.json()['id'])

# 5. NinjaFirewall 재활성화
r_fw = requests.post(f'{wp_base}/plugins/ninjafirewall/ninjafirewall', headers=headers, json={'status': 'active'})
print("Reactivate Firewall status:", r_fw.status_code)

print("Done setting up counter in sidebar-2!")
