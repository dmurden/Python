import csv
import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="192.168.1.20",
  user="dmurdenadm",
  passwd="Rga05dba!",
  database="covid"
)
mycursor = mydb.cursor()

mycursor.execute("DROP TABLE states")
mycursor.execute("DROP TABLE state_counties")
mycursor.execute("DROP TABLE covid_data")

mycursor.execute("CREATE TABLE states (sfips INT PRIMARY KEY, state VARCHAR(5))")
mycursor.execute("CREATE TABLE state_counties (cfips INT PRIMARY KEY, sfips INT, county VARCHAR(255))")
mycursor.execute("CREATE TABLE covid_data (id INT AUTO_INCREMENT PRIMARY KEY, cfips INT, casedate DATE, cases INT)")

with open('C:/Users/duke_/projects/python/covid/covid_confirmed_usafacts.csv', newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]

state = ''
county = ''
for x in data:
    if x[2] == 'State':
        continue
    if x[2] != state:
        state = x[2]
        sql = "INSERT INTO states (sfips, state) VALUES (%s, %s)"
        val = (x[3], state)
        mycursor.execute(sql, val)
        mydb.commit()
        county = ''
    if x[1] != county:
        county = x[1]
        if x[0] == '0':
            cfips = int(x[3]) * 1000 + 999
        else:
            cfips = x[0]
        print(x[2], x[3], cfips, x[1])
        sql = "INSERT INTO state_counties (cfips, sfips, county) VALUES (%s, %s, %s)"
        val = (cfips, x[3], x[2])
        mycursor.execute(sql, val)
        mydb.commit()
    for y in range(4,len(data[0])):
        #print(data[0][y])
        sql = "INSERT INTO covid_data (cfips, casedate, cases) VALUES (%s, %s, %s)"
        val = (cfips, datetime.datetime.strptime(data[0][y], "%m/%d/%y").date(), x[y])
        mycursor.execute(sql, val)
        #mydb.commit()
