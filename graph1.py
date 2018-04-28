# libraries
# libraries and data
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('Graph1.csv', ';', parse_dates=True)
df.reset_index(drop=True, inplace=True)
df.set_index("Date", inplace=True)

print(df)

fig, ax = plt.subplots()
ax.plot(df)
ax.set_xticks(df.index)
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax.xaxis.set_minor_formatter(mdates.DateFormatter("%Y-%m"))

fig.show()
