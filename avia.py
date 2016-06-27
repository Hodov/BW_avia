import json, sys

import serial
import json
import requests
import socket
import time

origin = ""
destination = ""

from urllib2 import Request, urlopen
headers = {"X-Access-Token": "a89067a692eb59360f4e2a4cf38adcd3"}

print sys.argv
if len(sys.argv)>1:
	origin = sys.argv[1]

if len(sys.argv)>2:
	destination = sys.argv[2]


cur = "currency=rub&"
ori="origin="+origin+"&"
des="destination="+destination+"&"
end="period_type=year&page=1&limit=30&show_to_affiliates=true&sorting=price&trip_class=0"

urlTickets = "http://api.travelpayouts.com/v2/prices/latest?"
urlTickets = urlTickets + cur
if origin == "0":
	origin = ""
if origin != "":
	urlTickets = urlTickets + ori
if destination != "":
	urlTickets = urlTickets + des

urlTickets = urlTickets + end

request = Request(urlTickets, headers=headers)
response_body = urlopen(request).read()

urlCities = "http://api.travelpayouts.com/data/cities.json"
data2 = json.loads(urlopen(urlCities).read())




parse = json.loads(response_body)
data = parse["data"]

for i in data:
	print i["origin"],
	print i["destination"],
	for a in data2:
		if a["code"]==i["destination"]:
			print a["name"],
	print i["value"],
	print i["depart_date"],
	print i["return_date"],
	print i["number_of_changes"]







