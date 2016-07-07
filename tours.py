import json
import sys
from urllib2 import Request, urlopen

urlTours = "http://bardarbunga.info/www/tours_v2.json"

saveAttr = ""

if len(sys.argv)>1:
	saveAttr = sys.argv[1]

if saveAttr == "save":
	dataTours = json.loads(urlopen(urlTours).read())
	with open('toursBW.json', 'w') as f:
		json.dump(dataTours, f)

else:

	with open('toursBW.json', 'r') as f:
		dataJSON = json.load(f)

	for a in dataJSON[1]:
		print a,
		print dataJSON[1][a]

	

	for i in range(1000):
		idata = dataJSON[i]

		#if idata["nights"] > 10 and idata["min_price"] < 30000 and idata["city"]["value"] == "Saint Petersburg":
		if idata["city"]["value"] == "Saint Petersburg":

			print idata["city"]["value"],
			print idata["nights"],
			print idata["season"]["from"],
			print idata["season"]["name"],
			print idata["month"],
			print idata["min_price"],
			print idata["date"],
			print idata["country"],
			print idata["country_code"]
			print idata["link_1_adults"]
			print idata["link_2_adults"]
			
			