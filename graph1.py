# libraries
# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

df = pd.read_csv('Graph1.csv',';')

print(df)

plt.plot('Date', 'USD', data=df)
plt.show()

