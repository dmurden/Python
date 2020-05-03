import csv
import datetime
import sqlite3
conn = sqlite3.connect('covid.db')

mycursor = conn.cursor()

infips = input('Enter FIPS or 0 for USA:')

if int(infips) > 999:
    mycursor.execute('SELECT * FROM state_counties WHERE cfips=?', [infips])
    data = mycursor.fetchone()
    if data == None:
        print('Bad boy!')
    else:
        stateid = int(data[1])
        mycursor.execute('SELECT * FROM states WHERE sfips=?', [stateid])
        sdata = mycursor.fetchone()
        with open(sdata[1]+'_'+data[2]+'_covid.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([sdata[1],data[2],infips])
            spamwriter.writerow(['Date', 'Cases', 'Daily'])
            pretotal = 0
            for row in mycursor.execute('SELECT * FROM covid_data WHERE cfips=? ORDER BY casedate', [infips]):
                daily = row[3] - pretotal
                pretotal = row[3]
                spamwriter.writerow([row[2], row[3], daily])
                print([row[2], row[3], daily])
elif int(infips) != 0:
    mycursor.execute('SELECT * FROM states WHERE sfips=?', [infips])
    data = mycursor.fetchone()
    if data == None:
        print('Bad boy!')
    else:
        with open(data[1]+'_covid.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([data[1],'',infips])
            spamwriter.writerow(['Date', 'Cases', 'Daily'])
            pretotal = 0
            for row in mycursor.execute('SELECT sfips, casedate, sum(cases) FROM covid_data, state_counties WHERE sfips=? \
                and covid_data.cfips = state_counties.cfips GROUP BY sfips, casedate ORDER BY casedate', [infips]):
                daily = row[2] - pretotal
                pretotal = row[2]
                spamwriter.writerow([row[1], row[2], daily])
                print([row[1], row[2], daily])
else:
    with open('USA_covid.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['USA','',infips])
        spamwriter.writerow(['Date', 'Cases', 'Daily'])
        pretotal = 0
        for data in mycursor.execute('SELECT casedate, sum(cases) FROM covid_data GROUP BY casedate ORDER BY casedate'):
            daily = data[1] - pretotal
            pretotal = data[1]
            spamwriter.writerow([data[0], data[1], daily])
            print([data[0], data[1], daily])

#sql = "INSERT INTO states (sfips, state) VALUES (?, ?)"
#sql = "INSERT INTO state_counties (cfips, sfips, county) VALUES (?, ?, ?)"
#sql = "INSERT INTO covid_data (cfips, casedate, cases) VALUES (?, ?, ?)"
conn.close()