import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Getting data from the Nasdaq API

df = pd.read_csv('https://data.nasdaq.com/api/v3/datasets/BCHAIN/MKPRU.csv')
df = df[df['Value'] > 0]
df['Date'] = pd.to_datetime(df['Date'])

df = df.iloc[::-1]  # Reversing the dataframe

plt.plot(df['Date'], np.log(df['Value']))

# Logarithmic function to fit against
def logFunc(x, p1, p2):
    return p1*np.log(x) + p2

ydata = np.log(df['Value'])
xdata = [x+1 for x in range(len(df))]
popt, pcov = curve_fit(logFunc, xdata, ydata, p0=(3.0,-10))


fittedYdata = logFunc(np.array([x+1 for x in range(len(df))]), popt[0], popt[1])

plt.semilogy(df['Date'], df['Value'])
for i in range(-5, 5):
    plt.plot(df['Date'], np.exp(fittedYdata+i))
plt.ylim(bottom=1)

plt.title('BTC Log regression')
plt.xlabel('Date')
plt.ylabel('Price')

plt.show()