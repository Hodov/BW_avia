import json, sys
import serial
import json
import requests
import socket
import time

origin = ""
destination = ""

originList = ["MOW","LED","HEL","TLL","RIX"]

from urllib2 import Request, urlopen
headers = {"X-Access-Token": "a89067a692eb59360f4e2a4cf38adcd3"}


with open('config.json', 'r') as f:
	dataJSON = json.load(f)

for originItem in originList:

	origin = originItem
	print origin

	cur = "currency=rub&"
	ori="origin="+origin+"&"
	end="period_type=year&page=1&limit=100&show_to_affiliates=true&sorting=price&trip_class=0"

	urlTickets = "http://api.travelpayouts.com/v2/prices/latest?"
	urlTickets = urlTickets + cur
	urlTickets = urlTickets + ori
	urlTickets = urlTickets + end

	request = Request(urlTickets, headers=headers)
	response_body = urlopen(request).read()

	parse = json.loads(response_body)
	data = parse["data"]

	for i in data:
		metrica = "BW." + i["origin"] + "." + i["destination"]
		name=i["origin"] + i["destination"]
		dataJSON["alerts"].append({'name': name, 'format': 'short', 'method': 'last_value', 'no_data': 'normal', 'history_size': '1day', 'query': metrica, 'rules': ['critical: < historical / 1.2', 'warning: < historical / 1.1']})


with open('configNew.json', 'w') as f:
     json.dump(dataJSON, f)





