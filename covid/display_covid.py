import csv
from matplotlib import pyplot
from statistics import mean

with open('covid_confirmed_usafacts.csv', newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]

infips = input('Enter FIPS or 0 for USA:')

daily = []

if int(infips) > 999:
    for x in data[1:]:
        if x[0] == infips:
            pyplot.title(x[1] + ' in ' + x[2])
            print(x[1] + ' in ' + x[2])
            for y in range(4,len(x)):
                daily.append(int(x[y]))
elif int(infips) != 0:
    for x in data[1:]:
        if x[3] == infips:
            if len(daily) == 0:
                pyplot.title(x[2])
                print(x[2])
                for y in range(4,len(x)):
                    daily.append(int(x[y]))
            else:
                for y in range(4,len(x)):
                    daily[y-4] += int(x[y])
else:
    for x in data[1:]:
        if len(daily) == 0:
            pyplot.title('USA')
            print('USA')
            for y in range(4,len(x)):
                daily.append(int(x[y]))
        else:
            for y in range(4,len(x)):
                daily[y-4] += int(x[y])
print(daily)
dataout = [0]
for y in range(1,len(daily)):
    dataout.append(daily[y] - daily[y-1])
print(dataout)
avgout = [0,0,0,0,0,0]
i = 6
while i < len(dataout):
    avgout.append(mean(dataout[i-6:i]))
    i += 1
pyplot.plot(range(len(dataout)), dataout, 'b-', range(len(avgout)), avgout, 'r-')
pyplot.show()