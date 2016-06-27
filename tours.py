


import json
from urllib2 import Request, urlopen

urlTours = "http://bardarbunga.info/www/tours_v2.json"
dataTours = json.loads(urlopen(urlTours).read())

for i in dataTours:
	print i["season"]["name"],
	print i["country"],
	print i["country_code"],
	print i["city"]["value"],
	print i["city"]["value"]