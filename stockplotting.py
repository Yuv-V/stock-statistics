from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import datetime
import csv
import numpy as np
import matplotlib.ticker as ticker
import statistics

print("Running")

colnames = ['date', 'open', 'high', 'low', 'close', 'volume']
data= pd.read_csv('C:\\Users\\Yuv\\python_work\\stockdata.csv', names=colnames)

dates = data.date.tolist()
opens = data.open.tolist()
highs = data.high.tolist()
lows = data.low.tolist()
closes = data.close.tolist()
volumes = data.volume.tolist()

newdates = dates[1:]
newopens = opens[1:]
newcloses = closes[1:]
newhighs = highs[1:]
newlows = lows[1:]
newvolumes = volumes[1:]

print(newdates)
print(newopens)


x_values = [datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in newdates]
print(x_values)
y_values = newcloses
print(y_values)

ax = plt.gca()

print("The average of the closing prices (Rounded) is: " + str(round(statistics.median(newcloses), 2)))
print("The average of the opening prices (Rounded) is: " + str(round(statistics.median(newopens), 2)))
print("The average of the low prices (Rounded) is: " + str(round(statistics.median(newlows), 2)))
print("The average of the high prices (Rounded) is: " + str(round(statistics.median(newhighs), 2)))

from matplotlib.dates import date2num
from matplotlib.pyplot import figure
import datetime
figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

x_values = [datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in newdates]

x = x_values[::10]
a =  newopens[::10]
b = newcloses[::10]
c = newhighs[::10]
for item in x, a:
    print(item)

ax = plt.gca()

ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

plt.title("Best Buy Stock Prices")
plt.xlabel("Date")
plt.ylabel("Price")
x = date2num(x)

ax = plt.subplot(111)

ax.bar(x, a, color = 'b', width=3, label='Open Prices')
ax.bar(x-3, b, color = 'g', width=3, label='Close Prices')
ax.bar(x+3, c, color = 'r', width=3, label='High Prices')
ax.legend(loc="upper right")
ax.xaxis_date()
ax.autoscale(tight=False)
ax.set_ylim(ymin=50)

    
    
plt.show()

