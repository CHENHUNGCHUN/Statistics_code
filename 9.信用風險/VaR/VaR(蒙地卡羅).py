import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt
import pandas_datareader
import scipy.stats as stats
from matplotlib import cm
from mpl_toolkits import mplot3d
import yfinance as yfin
import seaborn as sns

#需要假設報酬率服從常態分佈


#拉股價
tickers = ['GOOGL','AAPL','NFLX','AMZN','META']
ticker_num = len(tickers)
price_data = []
yfin.pdr_override()
for stock in tickers:
    prices = pandas_datareader.data.get_data_yahoo(stock, start='2015-11-30', end='2020-11-30')['Adj Close']
    price_data.append(prices)
    df_stock = pd.concat(price_data,axis=1)
df_stock.columns=tickers
print(df_stock)

#計算累積的log return 
logretrun = np.log(df_stock/df_stock.shift(1))[1:]
logretrun = logretrun+1
logretrun = logretrun.cumprod() #計算累積報酬率
logretrun.columns=tickers

#畫累積的log return 
plt.style.use('ggplot')
for i ,col in enumerate(logretrun.columns):
    logretrun[col].plot()
plt.title('Cumulative returns')
plt.xlabel('Date')
plt.ylabel('Return')
plt.xticks(rotation=30)
plt.legend(logretrun.columns)
plt.show()

#計算投組報酬率跟投組價格
lastest_return = logretrun.iloc[-1,:] #最後一天的累積報酬率
lastest_price = df_stock.iloc[-1,:]  #最後一天的股價
sigma = lastest_return.std()
stock_weight=[0.2,0.3,0.1,0.15,0.25]

except_return = lastest_return.dot(stock_weight)
print(f'expect return of portfolio {except_return}')

price = lastest_price.dot(stock_weight)
print(f'weight price of portfolio {price}')

#蒙地卡羅模擬1440個報酬率(假設投組報酬率服從常態分佈)
#Remark!!!!!!!!!!我覺得去模擬股價走勢再去用模擬出來的股價用歷史法的方法 比較合理
MC_num=500
confidence_level=0.95
time_step=1440  #將一天拆分為 "分鐘"  60*24
for i in range(MC_num):
    daily_return= np.random.normal(loc=except_return/time_step ,scale=sigma/np.sqrt(time_step) ,size=time_step)
    plt.plot(daily_return)
plt.axhline(np.percentile(daily_return,(1-confidence_level)*100),color='r',linestyle='dashed')
plt.axhline(np.percentile(daily_return,(confidence_level)*100),color='g',linestyle='dashed')
plt.axhline(np.mean(daily_return),color='b',linestyle='solid')
plt.xlabel('Time')
plt.ylabel('Return')
plt.show()

#將模擬出來的報酬率轉成hist看分布
sns.distplot(daily_return,kde=True,color = 'lightblue')
plt.axvline(np.percentile(daily_return,(1-confidence_level)*100),color='red',linestyle='dashed',linewidth=2)
plt.title('Return distribution')
plt.xlabel('Return')
plt.ylabel('Frequency')
plt.show()

#計算VaR值
initial_investment=1000000
VaR=initial_investment*(np.percentile(daily_return,(1-confidence_level)*100))
print(f'VaR :{VaR}')