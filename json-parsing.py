import requests
r = requests.get('https://indodax.com/api/btc_idr/ticker')
print r.json()

