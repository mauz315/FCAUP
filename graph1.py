# libraries
# libraries and data
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Graph1.csv', ';')

graph1 = plt.plot('Date', 'USD', data=df)

plt.show()