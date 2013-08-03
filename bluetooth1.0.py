#this is the 0.01v of bluetooth.py
#created by frugal-labs
#moin

import pymysql
import bluetooth
import bluetooth._bluetooth
import time
con = pymysql.connect(host ='127.0.0.1', user ='root', passwd='frugal')
cur = con.cursor()
cur.execute("""USE BLE""")
while True:
	global x
	x = False
	addr = bluetooth.discover_devices()
	timestamp = time.ctime()
	for address in addr:
		global btname
		btname = bluetooth.lookup_name(address)
		with con:
			cur.execute("""SELECT ID FROM details""")
			ID = cur.fetchall()
			for j in ID:
				for k in j:
					if k == address:
						x = True	
						cur.execute("""UPDATE details SET timestamp =%s, name = %s WHERE ID =%s""",(timestamp, btname,j))
			if x == False:
				cur.execute("INSERT INTO details(ID,timestamp,name)VALUES(%s, %s, %s)",(address, timestamp, btname))   
	time.sleep(60)

