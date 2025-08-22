import sys, requests, json, sqlite3, os, datetime

def exec_query(database, queryName):
    print(f"Starting executing {queryName}")
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    with open(f"./queries/{queryName}.sql", "r", encoding="utf-8") as f:
        sql_query = f.read()

    cursor.executescript(sql_query)
    conn.commit()
    conn.close()
    print(f"Finished executing {queryName}")

def ingest_to_sqlite(data):
    # Read the Excel file
    
    
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('./data.db')
    cursor = conn.cursor()
    
    # Create table dynamically based on DataFrame columns
    columns = list(data.keys())
    columns_list = ', '.join([f'"{col}" TEXT' for col in columns])
    #print(columns_list)
    create_table_query = f'CREATE TABLE IF NOT EXISTS estates_new ({columns_list});'
    cursor.execute(create_table_query)
    
    # Insert data into the table
    #print(data)
    values = ','.join(f"'{str(data[val])}'" for val in columns)
    #print(values)
    insert = f'''INSERT INTO estates_new({','.join(col for col in columns)}) VALUES({values})'''
    #print(insert)
    cursor.execute(insert)

    # Commit and close connection
    conn.commit()
    conn.close()
    
def get_image(url, addr) :
    img_data = requests.get(url).content
    with open(addr, 'wb') as handler:
        handler.write(img_data)

def get_date_from_db():
    conn = sqlite3.connect('./data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT max(date) FROM estates")
    results = cursor.fetchall()
    conn.close()
    return results[0][0]

def main():
    
    # Truncate the table before inserting new data
    exec_query('./data.db', 'TruncateTable')

    today = str(datetime.date.today())
    if get_date_from_db() == today:
        print(f"Data for {today} already exists in the database.")
        conn = sqlite3.connect('./data.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM estates WHERE date = {today}")
        conn.commit()
        conn.close()


    headers = {
            'Content-Type': 'application/json'
            ,'Sec-Fetch-Site':'same-site'
            #, 'query':"{'municipality':190}"
            }


    url = 'https://api.boliga.dk/api/v2/search/results?pageSize=100&zipCodes=3500'

    response = requests.get(url,headers = headers)
    

    if response.status_code == 200 :
        
        
       
        for house in response.json()['results'] :
            #print(response.json()['premiumResults'][0])

            image_list = ''
            if house['images'] is not None and len(house['images']) > 0 :

                for image in house['images'] :
                    street = str(house['street']).replace('.','')
                    if not os.path.isdir(f'./images/{street}'):
                        print((f'mkdir ./images/{street}'))
                        os.mkdir(f'./images/{street}')
                    
                    addr = f'./images/{street}/{image['id']}.jpg'
                    url = image['url']
                    if not os.path.isfile(addr) :
                        print(f'write i')
                        get_image(url, addr)
                    
                    image_list += str(image['id']) + ';'     


            data = {'id':house['id']
                    ,'priceChangePercentTotal':house['priceChangePercentTotal']
                    ,'energyClass':house['energyClass']
                    ,'price':house['price']
                    ,'buildYear':house['buildYear']
                    ,'street':house['street']
                    ,'zipCode':house['zipCode']  
                    ,'agentDisplayName':house['agentDisplayName']  
                    ,'isActive':house['isActive']
                    ,'propertyType':house['propertyType']  
                    ,'squaremeterPrice':house['squaremeterPrice']
                    ,'daysForSale':house['daysForSale']
                    ,'images':image_list[:-1]      
                    }


            

            # Ingest the new data into the SQLite database
            ingest_to_sqlite(data)

    else :
        print(response)

    
    # Keep track of the maximum date for each estate
    exec_query('./data.db', 'MaxDate')

    # Insert new estates into the database
    exec_query('./data.db', 'insertNewEstates')

    # Update the days for sale for each estate
    exec_query('./data.db', 'updateDaysForSale')

if __name__ == "__main__":
    main() 