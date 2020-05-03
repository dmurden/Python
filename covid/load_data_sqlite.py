import csv
import datetime
import sqlite3
conn = sqlite3.connect('covid.db')

mycursor = conn.cursor()

mycursor.execute("DROP TABLE states")
mycursor.execute("DROP TABLE state_counties")
mycursor.execute("DROP TABLE covid_data")

mycursor.execute("CREATE TABLE states (sfips INT PRIMARY KEY, state VARCHAR(5))")
mycursor.execute("CREATE TABLE state_counties (cfips INT PRIMARY KEY, sfips INT, county VARCHAR(255))")
mycursor.execute("CREATE TABLE covid_data (id INT AUTO_INCREMENT PRIMARY KEY, cfips INT, casedate DATE, cases INT)")

with open('covid_confirmed_usafacts.csv', newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]

state = ''
county = ''
for x in data:
    if x[2] == 'State':
        continue
    if x[2] != state:
        state = x[2]
        sql = "INSERT INTO states (sfips, state) VALUES (?, ?)"
        val = (x[3], state)
        mycursor.execute(sql, val)
        conn.commit()
        county = ''
    if x[1] != county:
        county = x[1]
        if x[0] == '0':
            cfips = int(x[3]) * 1000 + 999
        else:
            cfips = x[0]
        print(x[2], x[3], cfips, x[1])
        sql = "INSERT INTO state_counties (cfips, sfips, county) VALUES (?, ?, ?)"
        val = (cfips, x[3], x[1])
        mycursor.execute(sql, val)
        conn.commit()
    for y in range(4,len(data[0])):
        #print(data[0][y])
        sql = "INSERT INTO covid_data (cfips, casedate, cases) VALUES (?, ?, ?)"
        val = (cfips, datetime.datetime.strptime(data[0][y], "%m/%d/%y").date(), x[y])
        mycursor.execute(sql, val)
        #conn.commit()
conn.close()