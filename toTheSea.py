import json, sys
import datetime

#originList = ["MOW","LED","HEL","TLL","RIX"]
originList = ["MOW","LED"]
destinationList = ["SIP","TIV","BCN","BOJ","RMI","CMN","AGA","ALC","PMI","SKG","HER","JTR","LCA","PFO","AYT","IBZ","LIS","DXB","ATH","IZM","CHQ","PMO","CEQ","VLC","HKT","BKK","CMB","GOI","SGN","MNL","KUL","JKT","DPS","SYX","TGD","SPU","CAG"]
#destinationList = ["SEL"]

numberOfFlightsInOneDirection = 3
countNumberOfFlights = 0

origin = ""
destination = ""

from urllib2 import Request, urlopen
headers = {"X-Access-Token": "a89067a692eb59360f4e2a4cf38adcd3"}

print sys.argv
if len(sys.argv)>1:
	fromDate = sys.argv[1]

if len(sys.argv)>2:
	toDate = sys.argv[2]

if len(sys.argv)>3:
	value = sys.argv[3]

if len(sys.argv)>4:
	durationMin = sys.argv[4]

if len(sys.argv)>5:
	durationMax = sys.argv[5]

urlCities = "http://api.travelpayouts.com/data/cities.json"
data2 = json.loads(urlopen(urlCities).read())

for o in originList:
	for d in destinationList:
		origin = o
		destination = d

		cur = "currency=rub&"
		ori="origin="+origin+"&"
		des="destination="+destination+"&"
		end="period_type=year&page=1&limit=300&show_to_affiliates=true&sorting=price&trip_class=0"

		urlTickets = "http://api.travelpayouts.com/v2/prices/latest?"
		urlTickets = urlTickets + cur
		urlTickets = urlTickets + ori
		urlTickets = urlTickets + des
		urlTickets = urlTickets + end

		request = Request(urlTickets, headers=headers)
		response_body = urlopen(request).read()

		parse = json.loads(response_body)
		data = parse["data"]

		countNumberOfFlights = 0

		for i in data:
			bool1 = int((datetime.datetime.strptime(i["return_date"], "%Y-%m-%d") - datetime.datetime.strptime(i["depart_date"], "%Y-%m-%d")).days) >= int(durationMin)
			bool2 = int((datetime.datetime.strptime(i["return_date"], "%Y-%m-%d") - datetime.datetime.strptime(i["depart_date"], "%Y-%m-%d")).days) <= int(durationMax)
			boole = bool1 and bool2

			if countNumberOfFlights < numberOfFlightsInOneDirection and fromDate<=i["depart_date"] and toDate>=i["return_date"] and int(value) >= int(i["value"]) and boole and i["number_of_changes"]>=0:

				countNumberOfFlights += 1

				print i["origin"],
				print i["destination"],
				for a in data2:
					if a["code"]==i["destination"]:
						print a["name"],
				print i["value"],
				print i["depart_date"],
				print i["return_date"],
				print i["number_of_changes"]







