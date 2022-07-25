import pandas as pd
import matplotlib.pyplot as plt
# https://matplotlib.org/stable/gallery/pyplots/boxplot_demo_pyplot.html
# boxplot set x axis
# hide boxplot xaxis labels
API_DATA = {'pagination': {'limit': 30, 'offset': 0, 'count': 18, 'total': 18},
            'data':
                [
                {'open': 139.9, 'high': 141.91, 'low': 139.77, 'close': 141.66, 'volume': 89047400.0, 'adj_high': None,
                 'adj_low': None, 'adj_close': 141.66, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-24T00:00:00+0000'},
                {'open': 136.82, 'high': 138.59, 'low': 135.63, 'close': 138.27, 'volume': 72330300.0, 'adj_high': None,
                 'adj_low': None, 'adj_close': 138.27, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-23T00:00:00+0000'},
                {'open': 134.79, 'high': 137.755, 'low': 133.91, 'close': 135.35, 'volume': 73165480.0,
                 'adj_high': None,
                 'adj_low': None, 'adj_close': 135.35, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-22T00:00:00+0000'},
                {'open': 133.42, 'high': 137.06, 'low': 133.32, 'close': 135.87, 'volume': 80785400.0, 'adj_high': None,
                 'adj_low': None, 'adj_close': 135.87, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-21T00:00:00+0000'},
                {'open': 130.07, 'high': 133.08, 'low': 129.81, 'close': 131.56, 'volume': 134118500.0,
                 'adj_high': None,
                 'adj_low': None, 'adj_close': 131.56, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-17T00:00:00+0000'},
                {'open': 132.08, 'high': 132.39, 'low': 129.07, 'close': 130.06, 'volume': 107961508.0,
                 'adj_high': None,
                 'adj_low': None, 'adj_close': 130.06, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-16T00:00:00+0000'},
                {'open': 134.29, 'high': 137.34, 'low': 132.16, 'close': 135.43, 'volume': 91352700.0, 'adj_high': None,
                 'adj_low': None, 'adj_close': 135.43, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-15T00:00:00+0000'},
                {'open': 133.13, 'high': 133.89, 'low': 131.48, 'close': 132.76, 'volume': 84545000.0, 'adj_high': None,
                 'adj_low': None, 'adj_close': 132.76, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-14T00:00:00+0000'},
                {'open': 132.87, 'high': 135.2, 'low': 131.4401, 'close': 131.88, 'volume': 121893720.0,
                 'adj_high': None,
                 'adj_low': None, 'adj_close': 131.88, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-13T00:00:00+0000'},
                {'open': 140.28, 'high': 140.76, 'low': 137.06, 'close': 137.13, 'volume': 91437900.0, 'adj_high': None,
                 'adj_low': None, 'adj_close': 137.13, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-10T00:00:00+0000'},
                {'open': 147.08, 'high': 147.95, 'low': 142.53, 'close': 142.64, 'volume': 69367400.0, 'adj_high': None,
                 'adj_low': None, 'adj_close': 142.64, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-09T00:00:00+0000'},
                {'open': 148.58, 'high': 149.87, 'low': 147.46, 'close': 147.96, 'volume': 53895900.0, 'adj_high': None,
                 'adj_low': None, 'adj_close': 147.96, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-08T00:00:00+0000'},
                {'open': 144.35, 'high': 149.0, 'low': 144.1, 'close': 148.71, 'volume': 67713600.0, 'adj_high': None,
                 'adj_low': None, 'adj_close': 148.71, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-07T00:00:00+0000'},
                {'open': 147.03, 'high': 148.5689, 'low': 144.9, 'close': 146.14, 'volume': 70931362.0,
                 'adj_high': None,
                 'adj_low': None, 'adj_close': 146.14, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-06T00:00:00+0000'},
                {'open': 146.9, 'high': 147.97, 'low': 144.46, 'close': 145.38, 'volume': 88471400.0, 'adj_high': None,
                 'adj_low': None, 'adj_close': 145.38, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-03T00:00:00+0000'},
                {'open': 147.83, 'high': 151.27, 'low': 146.86, 'close': 151.21, 'volume': 72232000.0, 'adj_high': None,
                 'adj_low': None, 'adj_close': 151.21, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-02T00:00:00+0000'},
                {'open': 149.9, 'high': 151.74, 'low': 147.68, 'close': 148.71, 'volume': 74143400.0, 'adj_high': None,
                 'adj_low': None, 'adj_close': 148.71, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-01T00:00:00+0000'},
                {'open': 149.07, 'high': 150.66, 'low': 146.84, 'close': 148.84, 'volume': 93971235.0, 'adj_high': None,
                 'adj_low': None, 'adj_close': 148.84, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
                 'dividend': 0.0,
                 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-05-31T00:00:00+0000'}
            ]}
daily_average = []
high_y = []
low_y = []
open_y = []
close_y = []
date_x = []
for item in reversed(API_DATA["data"]):
    daily_average_oc = (item["open"] + item["close"])/2
    daily_average.append(daily_average_oc)
    high_y.append(item["high"])
    low_y.append(item["low"])
    open_y.append(item["open"])
    close_y.append(item["close"])
    date_x.append(item["date"][0:10])

fig, ax = plt.subplots()
# plt.tight_layout()
font = {'family':'serif','color':'darkred','size':20}
# set x,y label position matplotlib
ax.set_xlabel("Date",fontdict=font, loc="left")
ax.set_ylabel("$$$",fontdict=font)


import numpy as np
# ax.boxplot([[140,150],[135,145]], positions=[1,2])
# ax.boxplot([130,142], positions=[3])

for i in range(len(date_x)):
    data = [high_y[i], low_y[i]]
    box_i = ax.boxplot(data,positions=[i])

#Plot high/low as box chart,plot/floating column/? (top and bottom line indicator)
# https://developers.google.com/chart/image/docs/gallery/chart_gall?csw=1
ax.plot(date_x, high_y,'g',label="High")
# ax.text("High")
ax.plot(date_x, low_y,'r')
# ax.text("Low")

# https://stackoverflow.com/questions/11373610/save-matplotlib-file-to-a-directory
ax.set_title('STONKS!???',fontdict=font)
ax.set_xticklabels(date_x)
plt.setp(ax.get_xticklabels(), rotation=25, horizontalalignment='right')
plt.legend(loc='lower right')
fig.savefig('stonks.png',bbox_inches='tight')