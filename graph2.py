import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
import matplotlib.animation as animation
from datetime import datetime

df = pd.read_csv('data2.csv', ';')
df.Date = pd.to_datetime(df.Date, dayfirst=True)
df.reset_index(drop=True, inplace=True)
df.set_index("Date", inplace=True)

fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(111)
line, = ax1.plot(df)

fmt = '${x:,.1f}'  # formato se borra
tick = mtick.StrMethodFormatter(fmt)
ax1.yaxis.set_major_formatter(tick)

ax1.set_ylim(2.7, 4)
ax1.set_xlim(min(df.index), max(df.index))

monthyearFmt = mdates.DateFormatter('%b-%y')
ax1.xaxis.set_major_formatter(monthyearFmt)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
# fig.savefig('graph2_1.png')
# x = df.index
# y = df.USD

# def update(x, y, line):
#    line.set_data(x, y)
#    line.axes.axis([min(x), max(x), 2, 4])
#    return line,

# ani = animation.FuncAnimation(fig1, update, len(df.index), fargs=[df.index, df.USD, line],
#                              interval=25, blit=True)
# ani.save('test.gif')

fig1.show()
