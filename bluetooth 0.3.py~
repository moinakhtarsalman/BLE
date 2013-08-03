#this is the 0.01v of bluetooth.py
#created by frugal-labs
#moin

#invoke requierd lib's
#1)MySQL library
import pymysql
#2)pybluez library
import bluetooth
#3)extra part of bluez library
import bluetooth._bluetooth
import time
#collecting user details for sever login
#print 'enter mysql user id'
#uuser =raw_input()
#print "enter mysql password"
#upaswd = raw_input()
#establishing connection with mySQL server
con = pymysql.connect(host ='127.0.0.1', user ='root', passwd='frugal')
#initializing cursor as per the library documentation
cur = con.cursor()
#using BLE database 
cur.execute("""USE BLE""")
#making an infinite loop
while True:

	print "---performing inquiery---"
#.....discovering the bluetooth available in range
	addr = bluetooth.discover_devices()
	print"----device found---"
	print addr
#.....recording time for time stamp
	timestamp = time.ctime()
	print timestamp
#....we use for-loop to get the name of the device
	for address in addr:
		global btname
		btname = bluetooth.lookup_name(address)
		print "----name of the bluetooth device discoverd is---"
		print btname
		#pushing collected data to data-base
		with con:
			cur.execute("""SELECT ID FROM details""")
			ID = cur.fetchall()
			#print ID
			for j in ID:
				#print j
				for k in j:
					#print k
					if k == address:
				#if true update details
						print "---ID already exists---"
						global x
#.........................................SET x to TRUE if address matches to pre existing device address
						x = True	
#..........................................syntax to update details
						cur.execute("""UPDATE details SET timestamp =%s, name = %s WHERE ID =%s""",(timestamp, btname,j))
						print"---time and name updated succes fully---"
#......................CHECK if X is not TRUE i.e if x is not true then discovered device is NEW
			if x == False:
#......................if id do not exist .add new device
				cur.execute("INSERT INTO details(ID,timestamp,name)VALUES(%s, %s, %s)",(address, timestamp, btname))   
				print "---new device is added succesfully---"
#.....................set X to false again
				x = False
#...........creating a delay of 60 sec	
	time.sleep(60)
#...........back to while loop and procedure is repeated
