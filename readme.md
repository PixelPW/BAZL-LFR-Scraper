# BAZL Luftfahrzeugregister Scraper

## Prerequisites
Node.js

## Installation
Execute the following commands:
```
curl -X POST -H "Content-Type: application/json" -d '{"page_result_limit":5000,"current_page_number":1,"sort_list":"registration","totalItems":64,"query":{"registration":"","icaoCode":""},"language":"en","tab":"advanced"}' -k https://www.bazlwork.admin.ch/bazl-backend/lfr > lfr.all.json
```
```
node getall.js
```
