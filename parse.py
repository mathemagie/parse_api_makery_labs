#! /usr/bin/python

import json

json_file='labs.json'

json_data=open(json_file)
data = json.load(json_data)
json_data.close()

total = len(data['features'])

for i in range(1,total):
	print data['features'][i]['geometry']['coordinates']
