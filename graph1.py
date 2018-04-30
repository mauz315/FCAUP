import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from datetime import datetime

df = pd.read_csv('data1.csv', ';')
df.Date = pd.to_datetime(df.Date, dayfirst=True)
df.reset_index(drop=True, inplace=True)
df.set_index("Date", inplace=True)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.plot(df)
fmt = '${x:,.0f}'  # formato se borra
tick = mtick.StrMethodFormatter(fmt)
ax.set_ylim(0, 14)
ax.set_xlim(min(df.index), max(df.index))
ax.yaxis.set_major_formatter(tick)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.savefig('graph1.png')
fig.show()
