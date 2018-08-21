#!/usr/bin/python



import pycurl
import json
import time
from StringIO import StringIO

print("-==PAIR==-")
print("1. BTG/IDR")
print("2. BTC/IDR")
print("3. BCH/IDR")
print("4. NXT/IDR")
print("5. XRP/IDR")
print("6. LTC/IDR")

pair = input("Pilih Nomor Pair: ")

def masukin(pair):
	link = [
	        "https://vip.bitcoin.co.id/api/btg_idr/ticker",
	        "https://vip.bitcoin.co.id/api/btc_idr/ticker",
	        "https://vip.bitcoin.co.id/api/bch_idr/ticker",
                "https://vip.bitcoin.co.id/api/nxt_idr/ticker",
                "https://vip.bitcoin.co.id/api/xrp_idr/ticker",
		"https://vip.bitcoin.co.id/api/ltc_idr/ticker"
	]
	if pair == 1:
	    return link[0]
	elif pair == 2:
	    return link[1]
	elif pair == 3:
	    return link[2]
	elif pair == 4:
	    return link[3]
	elif pair == 5:
	    return link[4]
	elif pair == 6:
            return link[5]
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
	print("\n\033[1;31m Harga saat ini :\033[1;m " + "\033[1;34m" + y["last"] + "\033[1;m")
	time.sleep(6)
