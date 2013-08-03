#this is the 0.01v of bluetooth.py
#created by frugal-labs
#moin

import pymysql
import bluetooth
import bluetooth._bluetooth
import time
con = pymysql.connect(host ='just48.justhost.com', user ='frugalla_tmp', passwd='password2013')
cur = con.cursor()
cur.execute("""USE frugalla_BLE""")
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
						cur.execute("""UPDATE details SET TIMESTAMP =%s, NAME = %s WHERE ID =%s""",(timestamp, btname,j))
			if x == False:
				cur.execute("INSERT INTO details(ID,TIMESTAMP,NAME)VALUES(%s, %s, %s)",(address, timestamp, btname))   
	time.sleep(60)

