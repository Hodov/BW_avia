import json, sys

import serial
import json
import requests
import socket
import time

sendStatBool = True

msg=""
timeString = str(int(time.time()))

def collectMsg(key1, key2, val):	
	tempStr = "BW." + key1 + "." + key2 + " " + str(val) + " " + timeString + "\n"
	return tempStr

def sendMetrics(message):
	graphiteURL="localhost"
	graphitePort=2003
	try:
		conn = socket.create_connection((graphiteURL, graphitePort))
		conn.send(message)
		conn.close()
	except socket.error:
		print("Socket error")

originList = ["MOW","LED","HEL","TLL","RIX"]

origin = ""
destination = ""


from urllib2 import Request, urlopen
headers = {"X-Access-Token": "a89067a692eb59360f4e2a4cf38adcd3"}

for a in originList:

	origin = a
	print a
	
	cur = "currency=rub&"
	ori = "origin=" + origin + "&"
	des = "destination=" + destination + "&"
	end = "period_type=year&page=1&limit=100&show_to_affiliates=true&sorting=price&trip_class=0"

	urlTickets = "http://api.travelpayouts.com/v2/prices/latest?"
	urlTickets = urlTickets + cur
	urlTickets = urlTickets + ori
	if destination!="":
		urlTickets = urlTickets + des
	urlTickets = urlTickets + end

	request = Request(urlTickets, headers=headers)
	response_body = urlopen(request).read()

	parse = json.loads(response_body)
	data = parse["data"]


	for i in data:
		msg = msg + collectMsg(i["origin"],i["destination"],i["value"])


	if sendStatBool:
		sendMetrics(msg)

	msg = ""

print "Send data"
print time.strftime('%x %X')





