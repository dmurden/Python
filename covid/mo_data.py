import csv
from datetime import date
from datetime import timedelta

covidday = date(2020, 3, 10)
#print(covidday.strftime("%m-%d-%Y"))

while covidday <= date.today():
    if covidday < date(2020, 3, 22):
        with open('C:/Users\duke_/projects/Covid/csse_covid_19_data/csse_covid_19_daily_reports/' + covidday.strftime("%m-%d-%Y") + '.csv', newline='') as csvfile:
            covidreader = csv.reader(csvfile)
            crftot = 0
            for row in covidreader:
                if row[0] == "Missouri":
                    #print(row[1] + ', ' + row[7])
                    crftot += int(row[3])
            print(covidday.strftime("%m-%d-%Y") + ', ' + str(crftot))
    else:
        with open('C:/Users\duke_/projects/Covid/csse_covid_19_data/csse_covid_19_daily_reports/' + covidday.strftime("%m-%d-%Y") + '.csv', newline='') as csvfile:
            covidreader = csv.reader(csvfile)
            crftot = 0
            for row in covidreader:
                if row[2] == "Missouri":
                    #print(row[1] + ', ' + row[7])
                    crftot += int(row[7])
            print(covidday.strftime("%m-%d-%Y") + ', ' + str(crftot))
    covidday += timedelta(days=1)
