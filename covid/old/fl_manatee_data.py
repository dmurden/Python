import csv
from datetime import date
from datetime import timedelta

covidday = date(2020, 3, 22)
cmpstate = "Florida"
cmpcounty = "Manatee"

while covidday <= date.today():
    if covidday < date(2020, 3, 22):
        with open('C:/Users/duke_/projects/Covid/csse_covid_19_data/csse_covid_19_daily_reports/' + covidday.strftime("%m-%d-%Y") + '.csv', newline='') as csvfile:
            covidreader = csv.reader(csvfile)
            crftot = 0
            for row in covidreader:
                if row[0] == cmpstate:
                    crftot += int(row[3])
            print(covidday.strftime("%m-%d-%Y") + ', ' + str(crftot))
    else: #covidday < date(2020, 4, 12):
        with open('C:/Users/duke_/projects/Covid/csse_covid_19_data/csse_covid_19_daily_reports/' + covidday.strftime("%m-%d-%Y") + '.csv', newline='') as csvfile:
            covidreader = csv.reader(csvfile)
            crftot = 0
            for row in covidreader:
                if row[2] == cmpstate and row[1] == cmpcounty:
                    crftot += int(row[7])
            print(covidday.strftime("%m-%d-%Y") + ', ' + str(crftot))
    #else:
        #with open('C:/Users/duke_/projects/Covid/csse_covid_19_data/csse_covid_19_daily_reports/' + covidday.strftime("%m-%d-%Y") + '.csv', newline='') as csvfile:
            #covidreader = csv.reader(csvfile)
            #crftot = 0
            #for row in covidreader:
                #if row[0] == cmpstate and :
                    #crftot += int(row[5])
            #print(covidday.strftime("%m-%d-%Y") + ', ' + str(crftot))
    covidday += timedelta(days=1)
