# libraries
# libraries and data
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from datetime import datetime

df = pd.read_csv('Graph1.csv', ';')
df.Date = pd.to_datetime(df.Date, dayfirst=True)
df.reset_index(drop=True, inplace=True)
df.set_index("Date", inplace=True)

fig, ax = plt.subplots()
plt.figure(figsize=(8, 6))
df.plot()
lims = [min(df.index), max(df.index), 0, 14]
plt.axis(lims)
fmt = '${x:,.0f}' # formato se borra
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
# ax.spines['top'].set_visible(False)
# plt.savefig('graph1.png')
plt.show()
