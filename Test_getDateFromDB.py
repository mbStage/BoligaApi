import sqlite3
import datetime

def get_date_from_db():
    conn = sqlite3.connect('./data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT max(date) FROM estates")
    results = cursor.fetchall()
    conn.close()
    return results[0][0]

print(get_date_from_db() == str(datetime.date.today()))
