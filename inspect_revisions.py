import requests
import base64
import json

auth = base64.b64encode(b'barcode128:5CoX aTTH Qzr8 NJzn zLNP xvZW').decode()
headers = {
    'Authorization': 'Basic ' + auth,
    'Content-Type': 'application/json'
}
wp_base = 'https://barcode128.mycafe24.com/wp-json/wp/v2/pages'

pages = requests.get(f'{wp_base}?per_page=100', headers=headers).json()
for p in pages:
    pid = p['id']
    slug = p['slug']
    if slug == 'sample-page':
        continue
    revs_res = requests.get(f'{wp_base}/{pid}/revisions?context=edit', headers=headers)
    revs = revs_res.json() if revs_res.status_code == 200 else []
    print(f"Page {pid} ({slug}): {len(revs)} revs")
    for r in revs[:3]:
        raw_len = len(r.get('content', {}).get('raw', ''))
        print(f"   rev {r['id']} | date {r['date']} | len {raw_len}")
