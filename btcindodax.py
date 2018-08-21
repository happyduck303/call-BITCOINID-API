import pycurl
import json
import time
from StringIO import StringIO

print("Pilihan : ")
print("1. ticker")


pair = input("Pilih Nomor Pair: ")

def masukin(pair):
	link = [
	        "https://indodax.com/api/btc_idr/ticker"
	]
	if pair == 1:
	    return link[0]

	else:
	    print("pair tidak tercantum")

while True:
	buffer = StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, masukin(pair))
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()
	body = buffer.getvalue()
	x = json.loads(body)
	y = x["ticker"]
	print("\n Harga saat ini : "+ y["last"])
	time.sleep(6)
