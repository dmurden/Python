import csv
from matplotlib import pyplot
from statistics import mean
import numpy as np

def best_fit_slope_and_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))
    b = mean(ys) - m*mean(xs)
    return m, b

def dsp_graph(infips):
    daysavg = 14
    daily = []
    #pyplot.figure(figsize=[9.6,7.2])
    pyplot.figure(figsize=[13.8,7.2])
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
    dataout = []
    for y in range(1,len(daily)):
        if daily[y] != 0:
            dataout.append(daily[y] - daily[y-1])
    ys = np.array(dataout, dtype=np.float64)
    xs = np.array(list(range(0, len(dataout))), dtype=np.float64)
    m, b = best_fit_slope_and_intercept(xs,ys)
    #print(m,b)
    regression_line = []
    for x in xs:
        regression_line.append((m*x)+b)

    avgout = []        
    for i in range(daysavg-1):
        avgout.append(0)
    i = daysavg - 1
    while i < len(dataout):
        avgout.append(mean(dataout[i-(daysavg-1):i]))
        i += 1

    pyplot.plot(range(len(dataout)), dataout, 'b-', \
        range(len(avgout)), avgout, 'r-', \
        range(len(regression_line)), regression_line, 'y-')
    pyplot.text(60, .025, r'Slope: =' + str(m))

    pyplot.grid(True)
    #pyplot.show()

with open('covid_confirmed_usafacts.csv', newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]

#infips = input('Enter FIPS or 0 for USA:')

dsp_graph("12")
dsp_graph("12009")
dsp_graph("12081")
dsp_graph("12127")
dsp_graph("18")
dsp_graph("18043")
dsp_graph("18061")
dsp_graph("21")
dsp_graph("21111")
#dsp_graph("28")
#dsp_graph("28143")
dsp_graph("29")
dsp_graph("29031")
dsp_graph("29183")
dsp_graph("29189")
dsp_graph("29510")
dsp_graph("47")
dsp_graph("47155")
#dsp_graph("47157")
dsp_graph("0")

pyplot.show()