import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from scipy.stats import norm
import random
import pandas_datareader
import yfinance as yfin

'''
維納過程模擬股價 => "漂移項"與"波動項"之和為報酬率
r = (mu - (sigam * 1/2)) + Z_test_stastic* stdev
其中Z_test_stastic 是代表符合常態分配的隨機亂數
所以股價的波動 等於是 前一天的價格 * exp((mu - (sigam * 1/2)) + Z_test_stastic* stdev)

'''

mpl.style.use('ggplot')
yfin.pdr_override()
ticker = 'AAPL'
stock = pd.DataFrame()
stock['ticker'] = pandas_datareader.data.get_data_yahoo(ticker, start='2010-10-24', end='2019-12-31')['Adj Close']
print(stock)

stock.plot(figsize=(15,8),legend=None,c='r')
plt.title('Stock price for AAPL')
plt.xlabel('Time')
plt.ylabel('Price')
plt.show()

#計算日報酬率
log_return = np.log(1+stock.pct_change())
ax=sns.histplot(log_return.iloc[1:])
ax.set_xlabel('Daliy log return')
ax.set_ylabel('Frequency')
ax.set_yticks([10,20,30,40])
plt.show()          

#模型參數
u = log_return.mean()
var = log_return.var()
drift = u - (0.5*var)
stdev = log_return.std()

#開始模擬股價走勢
days=60 #模擬60天
MC_trials = 20000 #模擬2000次(條)
Z = norm.ppf(np.random.rand(days,MC_trials))  #隨機抽樣 60(row)*2000(columns)的矩陣   等於抽60*2000個alpha值出來 然後平均數為0 標準差為1的標準常態分配
daily_returns = np.exp(drift.values + stdev.values*Z)   #不是很確定為什麼要用.values 才能運作
print(daily_returns)

price_paths = np.zeros_like(daily_returns)
price_paths[0,:] = stock.iloc[-1]   #price_paths的第一個row 是stock.iloc[-1]
for i in range(1,60):
    price_paths[i,:] = price_paths[i-1]*daily_returns[i,:]
print(price_paths)

#畫圖
rows=1
cols=2
fig,(ax1,ax2) = plt.subplots(rows,cols,figsize=(14,5),gridspec_kw={'width_ratios':[3,1]})
ax1.plot(price_paths,lw=0.5)
ax1.set_yticks([40,70,100,130])
ax1.set_title('(a)',loc='left')
ax2=sns.distplot(price_paths[-1,:],rug=True,rug_kws={'color':'green','alpha':0.5,'height':0.06,'lw':0.5},vertical=True,label='(b)')
ax2.set_yticks([40,70,100,130])
ax2.set_title('(b)',loc='left')
plt.show()