# SMA-and-EMA-trading-signals
Calculating the SMA and EMA of a stock and generate trading signals

This python program creates buy and sell signals based on three simple moving averages (SMA) and three exponential moving averages (EMA) and takes into its calculation the price of the stock over time. First, the price data is gathered from the FRED (Federal Reserve Economic Data) and saved as csv to be opened and plotted by the program.
 ![image](https://user-images.githubusercontent.com/68149933/185955155-4393b8a6-3709-49ac-9154-2359ea78bd5a.png)

  For the first program, the user is demanded to input the number of days to be calculated for each SMA. The SMA calculates the mean close price of the stock for the number of days chosen, for example the 50-day SMA is the mean close price for the previous 50 trading days. In the example below, the shorter SMA chosen is the 50-day, the medium SMA is the 100-day and 200-days for the long one, as they are one of the most common values for long term trading.
![image](https://user-images.githubusercontent.com/68149933/185955545-e46188ad-12fd-4ad7-bae2-ed44864ca23c.png)

  The SMAs are then used to trigger either a buy or a sell signal, depending on their behavior. Whenever the short SMA crosses the medium SMA to the upside and they both cross the long SMA, a buy signal is triggered. On the contrary, when the shorter SMA crosses below the medium SMA and longer SMA, the sell signal is triggered.
![image](https://user-images.githubusercontent.com/68149933/185956016-0c3572ab-0a45-47ea-b436-9186a324fb08.png)

  As usual, the buy signal is represented by a green arrow facing up and the sell signal is a red arrow pointing down. Since the SMA is a lagging indicator (i.e., it uses data from the past and therefore is not good at predicting future prices) it works better in a strong trend rather than in a market condition where prices move sideways or when the market is shifting.
  The EMAs work similarly to the SMAs but the most recent prices are more relevant than the older prices. Using EMAs instead of SMAs becomes useful when there is volatility in prices because the EMA will react sooner than the SMA to price changes. Below, the 50-day, 100-day and 200-day EMAs are plotted:
  ![image](https://user-images.githubusercontent.com/68149933/185956807-1bf052b8-e394-4805-b849-c43c8b11d708.png)
  
  Even though both SMA and EMA can be helpful when deciding whether to buy or sell a stock, a trade should not be based solely on those two indicators. They can, however, give an overall idea of the stock trend and trend shifts. 
