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
print 'enter mysql user id'
uuser =raw_input()
print "enter mysql password"
upaswd = raw_input()
#establishing connection with mySQL server
con = pymysql.connect(host ='127.0.0.1', user = uuser, passwd= upaswd)
#initializing cursor as per the library documentation
cur = con.cursor()
#using BLE database 
cur.execute("""USE BLE""")
#making an infinite loop
while True:
#discovering the bluetooth available in range
	print "performing inquiery"
	addr = bluetooth.discover_devices()
	print addr
#recording time for time stamp
	timestamp = time.ctime()
	print timestamp
#we use for-loop to get the name of the device
	for address in addr:
		global btname
		btname = bluetooth.lookup_name(address)
		print "name of the bluetooth device discoverd is"
		print btname
		#pushing collected data to data-base
		with con:
			cur.execute("""SELECT sl FROM details""")
			length = cur.fetchall()
			print len(length)
			cur.execute("""SELECT ID FROM details""")
			for k in range(len(length)):
				print k
				ID = cur.fetchone()
				print ID
				for j in ID:
					print j
					#checking if id exists in database or not
					if j == address:
				#if true update details
						print "ID already exists,time and name will be updated"
				#syntax to update details
						cur.execute("""UPDATE details SET timestamp =%s, name = %s WHERE ID =%s""",(timestamp, btname,j))
					else:
				#if id do not exist .add new device
						cur.execute("INSERT INTO details(ID,timestamp,name)VALUES(%s, %s, %s)",(address, timestamp, btname))   
						print "new device is added succesfully"
						
	time.sleep(60)



