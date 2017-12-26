import urllib, json
import csv

# BAZL lrf.csv file, download here: https://www.bazl.admin.ch/bazl/de/home/fachleute/luftfahrzeuge/luftfahrzeugregister.html
lfrdata = 'lfr.csv'

jdata = {}
i=0

with open(lfrdata, 'rb') as csvfile:
    lfrreader = csv.reader(csvfile, delimiter =";")
    next(csvfile)
    row_count = sum(1 for row in lfrreader)

with open(lfrdata, 'rb') as csvfile:
    lfrreader = csv.reader(csvfile, delimiter =";")
    next(csvfile)
    for row in lfrreader:
        reg = row[0]
        url = "https://www.bazlwork.admin.ch/bazl-backend/lfr/" +reg

        response = urllib.urlopen(url)
        data = json.loads(response.read())

        hex = data['details']['aircraftAddresses']['hex']
        type = data['icaoCode']

        hex = hex[-4:]
        hex = hex.upper()

        jdata.update({hex:{'r':reg,'t':type}})
        i += 1
        prog=100*i/row_count
        progress = str(prog)+"%"
        print progress

# Writing JSON data
with open('4B.json', 'w') as f:
    json.dump(jdata, f, separators=(',', ':'))
