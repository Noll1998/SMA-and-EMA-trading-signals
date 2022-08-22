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

#Visualize the stock price
plt.figure(figsize=(12.5, 4.5))
plt.plot(stock['Adj Close'], label = f'{stock_ticker}')
plt.title(f'{stock_name} Adj. Close Price History')
plt.xlabel(f'{first_date_converted} - {last_date_converted}')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()

#Create shorter SMA
SMAshort = pd.DataFrame()
shorter_SMA = int(input('Size of shorter SMA (days)?'))
SMAshort['Adj Close'] = stock['Adj Close'].rolling(window=shorter_SMA).mean()

#Create medium SMA
SMAmedium = pd.DataFrame()
medium_SMA = int(input('Size of medium SMA (days)?'))
SMAmedium['Adj Close'] = stock['Adj Close'].rolling(window=medium_SMA).mean()

#Create longer SMA
SMAlong= pd.DataFrame()
longer_SMA = int(input('Size of longer SMA (days)?'))
SMAlong['Adj Close'] = stock['Adj Close'].rolling(window=longer_SMA).mean()

#Visualize the stock price with the SMAs
plt.figure(figsize=(12.5, 4.5))
plt.plot(stock['Adj Close'], label = f'{stock_ticker}')
plt.plot(SMAshort['Adj Close'], label = f'SMA{shorter_SMA}')
plt.plot(SMAmedium['Adj Close'], label = f'SMA{medium_SMA}')
plt.plot(SMAlong['Adj Close'], label = f'SMA{longer_SMA}')
plt.title(f'{stock_name} Adj. Close Price History')
plt.xlabel(f'{first_date_converted} - {last_date_converted}')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()

#New dataframe to store the data
data = pd.DataFrame()
data['stock'] = stock['Adj Close']
data['SMAshort'] = SMAshort['Adj Close']
data['SMAmedium'] = SMAmedium['Adj Close']
data['SMAlong'] = SMAlong['Adj Close']

#Buy and Sell signal for the stock
def buy_sell(data):
  sigPriceBuy = []
  sigPriceSell = []
  flag = -1

  for i in range(len(data)):
    if data['SMAshort'][i] > data['SMAmedium'][i] > data['SMAlong'][i]:
      if flag != 1:
        sigPriceBuy.append(data['stock'][i])
        sigPriceSell.append(np.nan)
        flag = 1
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)  
    elif data['SMAshort'][i] < data['SMAmedium'][i] < data['SMAlong'][i]:
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

#Visualize the stock price and the SMAs with the signal
plt.figure(figsize=(12.6, 4.6))
plt.plot(data['stock'], label=f'{stock_ticker}', alpha = 0.35)
plt.plot(data['SMAshort'], label=f'SMA{shorter_SMA}', alpha = 0.35)
plt.plot(data['SMAmedium'], label=f'SMA{medium_SMA}', alpha = 0.35)
plt.plot(data['SMAlong'], label=f'SMA{longer_SMA}', alpha = 0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'Buy', marker = '^', color = 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'Sell', marker = 'v', color = 'red')
plt.title(f'{stock_name} Adj. Close Price History Buy & Sell Signals')
plt.xlabel(f'{first_date_converted} - {last_date_converted}')
plt.ylabel('Adj Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()

