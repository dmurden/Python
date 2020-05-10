import csv
from matplotlib import pyplot
from statistics import mean

with open('covid_confirmed_usafacts.csv', newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]

infips = input('Enter FIPS or 0 for USA:')

daysavg = 7
daily = []

if int(infips) > 999:
    for x in data[1:]:
        if x[0] == infips:
            pyplot.title(x[1] + ' in ' + x[2])
            for y in range(4,len(x)):
                daily.append(int(x[y]))
elif int(infips) != 0:
    for x in data[1:]:
        if x[3] == infips:
            if len(daily) == 0:
                pyplot.title(x[2])
                for y in range(4,len(x)):
                    daily.append(int(x[y]))
            else:
                for y in range(4,len(x)):
                    daily[y-4] += int(x[y])
else:
    for x in data[1:]:
        if len(daily) == 0:
            pyplot.title('USA')
            for y in range(4,len(x)):
                daily.append(int(x[y]))
        else:
            for y in range(4,len(x)):
                daily[y-4] += int(x[y])
dataout = [0]
for y in range(1,len(daily)):
    if daily[y] != 0:
        dataout.append(daily[y] - daily[y-1])
avgout = []        
for i in range(daysavg-1):
    avgout.append(0)
i = daysavg - 1
while i < len(dataout):
    avgout.append(mean(dataout[i-(daysavg-1):i]))
    i += 1
pyplot.plot(range(len(dataout)), dataout, 'b-', range(len(avgout)), avgout, 'r-')
pyplot.show()