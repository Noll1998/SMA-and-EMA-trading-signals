import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

plt.style.use('fivethirtyeight')

stock = pd.read_csv('GOOGL.csv')
stock_name = "Google Alphabet"
stock_ticker = "GOOGL"

first_date = stock.iloc[0, 0]
last_row = len(stock.index)
last_date = stock.iloc[last_row - 1, 0]

first_date_converted = datetime.strptime(first_date, '%Y-%m-%d').strftime('%d. %b, %Y')
last_date_converted = datetime.strptime(last_date, '%Y-%m-%d').strftime('%d. %b, %Y')


#Create EMAs
EMAshort = pd.DataFrame()
short_EMA = int(input('Size of shorter EMA (days)?'))
EMAshort['Adj Close'] = stock['Adj Close'].ewm(span=short_EMA).mean()

EMAmedium = pd.DataFrame()
medium_EMA = int(input('Size of medium SMA (days)?'))
EMAmedium['Adj Close'] = stock['Adj Close'].ewm(span=medium_EMA).mean()

EMAlong= pd.DataFrame()
long_EMA = int(input('Size of longer SMA (days)?'))
EMAlong['Adj Close'] = stock['Adj Close'].ewm(span=long_EMA).mean()


#New dataframe to store the data
data = pd.DataFrame()
data['stock'] = stock['Adj Close']
data['EMAshort'] = EMAshort['Adj Close']
data['EMAmedium'] = EMAmedium['Adj Close']
data['EMAlong'] = EMAlong['Adj Close']

#Buy and Sell signal for the stock
def buy_sell(data):
  sigPriceBuy = []
  sigPriceSell = []
  flag = -1

  for i in range(len(data)):
    if data['EMAshort'][i] > data['EMAmedium'][i] > data['EMAlong'][i]:
      if flag != 1:
        sigPriceBuy.append(data['stock'][i])
        sigPriceSell.append(np.nan)
        flag = 1
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)  
    elif data['EMAshort'][i] < data['EMAmedium'][i] < data['EMAlong'][i]:
      if flag != 0:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(data['stock'][i])
        flag = 0
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    else:
      sigPriceBuy.append(np.nan)
      sigPriceSell.append(np.nan)

  return(sigPriceBuy, sigPriceSell)

#Store the signal data
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

#Visualize the stock price and the EMAs with the signal
plt.figure(figsize=(12.6, 4.6))
plt.plot(data['stock'], label=f'{stock_ticker}', alpha = 0.35)
plt.plot(data['EMAshort'], label=f'EMA{short_EMA}', alpha = 0.35)
plt.plot(data['EMAmedium'], label=f'EMA{medium_EMA}', alpha = 0.35)
plt.plot(data['EMAlong'], label=f'EMA{long_EMA}', alpha = 0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'Buy', marker = '^', color = 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'Sell', marker = 'v', color = 'red')
plt.title(f'{stock_name} Adj. Close Price History Buy & Sell Signals')
plt.xlabel(f'{first_date_converted} - {last_date_converted}')
plt.ylabel('Adj Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()


