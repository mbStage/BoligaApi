import sys, requests, json, sqlite3

headers = {
        'Content-Type': 'application/json'
        ,'Sec-Fetch-Site':'same-site'
        #, 'query':"{'municipality':190}"
        }

#url = 'https://api.boliga.dk/api/v2/search/results?pageSize=50&zipCodes=3500'
url = 'https://api.boliga.dk/api/v2/search/results?pageSize=50&zipCodes=3500'

#https://api.boliga.dk/api/v2/search/results?pageSize=50&zipCodes=3500&searchTab=0&sort=daysForSale-a&includeds=1&includeotw=1

response = requests.get(url,headers = headers)  

if response.status_code == 200 :
    for i in response.json()['results'][0]: 
        print(i)
else :
    print(response)

print(response.json()['results'][0])

