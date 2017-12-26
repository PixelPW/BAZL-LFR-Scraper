# BAZL Luftfahrzeugregister Scraper

Creats JSON file for a dump1090 aircraft database. Only for aircrafts registered in Switzerland.
## Prerequisites
* Node.js
* Download current lfr.csv file from here: https://www.bazl.admin.ch/bazl/de/home/fachleute/luftfahrzeuge/luftfahrzeugregister.html

## Installation
Execute the following commands:
```
curl -X POST -H "Content-Type: application/json" -d '{"page_result_limit":5000,"current_page_number":1,"sort_list":"registration","totalItems":64,"query":{"registration":"","icaoCode":""},"language":"en","tab":"advanced"}' -k https://www.bazlwork.admin.ch/bazl-backend/lfr > lfr.all.json
```
```
node getall.js
```
