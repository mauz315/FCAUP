import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
import matplotlib.animation as animation
from datetime import datetime, timedelta

df = pd.read_csv('data4.csv', ';')
df.Date = pd.to_datetime(df.Date, dayfirst=True)

df.reset_index(drop=True, inplace=True)
df.set_index("Date", inplace=True)

supDate = max(df.index)
lowDate = min(df.index)
df = df[:119]

fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(111)
ax1.plot(df, 'r')

fmt = '${x:,.1f}'  # formato se borra
tick = mtick.StrMethodFormatter(fmt)
ax1.yaxis.set_major_formatter(tick)

ax1.set_ylim(2, 40)
ax1.set_xlim(lowDate - timedelta(days=30), supDate)

monthyearFmt = mdates.DateFormatter('%b-%y')
ax1.xaxis.set_major_formatter(monthyearFmt)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

fig1.savefig('graph4_base_2.png')
fig1.show()
