import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt
import pandas_datareader
import scipy.stats as stats
from matplotlib import cm
from mpl_toolkits import mplot3d
import yfinance as yfin

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
print(df_stock)

#計算log return
logretrun = np.log(df_stock/df_stock.shift(1))[1:]
logretrun.columns=tickers
print(logretrun)


#畫log return 跟常態分配的圖
plt.style.use('ggplot')
mu,std = stats.norm.fit(logretrun['GOOGL'])   #擬合常態分布  (不是很確定為什麼要這樣)
logretrun['GOOGL'].hist(bins=60,density=True,histtype='stepfilled',alpha=0.5)   #Googl報酬率
x= np.linspace(mu-5*std ,mu+5*std ,500)
plt.plot(x,stats.norm.pdf(x,mu,std))     #擬合過的常態分布圖
plt.title('log return distribution for GOOGL')
plt.xlabel('Return')
plt.ylabel('Density')
plt.show()

#畫其他四檔股票的log return 及擬合過的常態分配的圖
rows=2
cols=2
fig , axs = plt.subplots(rows,cols,figsize=(12,6))
ticker_n = 1
for i in range(rows):
    for j in range(cols):
       mu,std = stats.norm.fit(logretrun[tickers[ticker_n]]) 
       x = np.linspace(mu-5*std,mu+5*std,500)
       axs[i,j].hist(logretrun[tickers[ticker_n]],bins=60,density=True,histtype='stepfilled',alpha=0.5)
       axs[i,j].plot(x,stats.norm.pdf(x,mu,std))
       axs[i,j].set_title(f'log return distribution for {tickers[ticker_n]}')
       axs[i,j].set_xlabel('Return')
       axs[i,j].set_ylabel('Density')
       ticker_n +=1
plt.tight_layout()
plt.show()
       
#計算投組的平均值以及標準差
cov_logreturns = logretrun.cov()
mean_logreturns = logretrun.mean()
print(f'平均值{mean_logreturns}')
print(f'共變異矩陣{cov_logreturns}')

stock_weight = np.array([0.2,0.3,0.1,0.15,0.25]) #先隨意變假設權重,因為後面要用轉置所以轉成array
protfolio_mean_log = mean_logreturns.dot(stock_weight)
protfolio_vol_log = np.sqrt(np.dot(stock_weight.T,np.dot(cov_logreturns,stock_weight)))
print(f'The mean and volitility of the portfolio are :{protfolio_mean_log:.6f} and {protfolio_vol_log:.6f}')


#算風險值VaR    mu-Z*std
confidence_level=0.99
initial_investment=1000000

n=1 #一天
VaR_norm = initial_investment*(protfolio_mean_log-abs(stats.norm.ppf(1-confidence_level)) * protfolio_vol_log ) *np.sqrt(n)
VaR_lognrom = initial_investment*(1-np.exp(protfolio_mean_log - protfolio_vol_log*abs(stats.norm.ppf(1-confidence_level))))*np.sqrt(n)
print(VaR_norm,VaR_lognrom)

#視覺化不同信心水準下的VaR值
confidence_level_list = np.arange(0.9,0.99,0.001)
initial_investment=1000000
n=1#一天
VaR_norm_list = []
VaR_lognrom_list = []
for confidence_level in confidence_level_list:
    VaR_norm = initial_investment*(abs(stats.norm.ppf(1-confidence_level)) * protfolio_vol_log-protfolio_mean_log ) *np.sqrt(n)
    VaR_norm_list.append(VaR_norm)
    
    VaR_lognrom = initial_investment*(1-np.exp(protfolio_mean_log - protfolio_vol_log*abs(stats.norm.ppf(1-confidence_level))))*np.sqrt(n)  
    VaR_lognrom_list.append(VaR_lognrom)
    
plt.plot(confidence_level_list,VaR_norm_list,label = 'Normal VaR')
plt.plot(confidence_level_list,VaR_lognrom_list,label = 'Lognormal VaR')
plt.legend()
plt.xlabel='confidence_level'
plt.ylabel='1day -VaR'
plt.show()


#視覺化不同信心水準 以及不同持有天數下的VaR值
holding_period_list = np.arange(1,91,1)
confidence_level_list = np.arange(0.9,0.99,0.001)
initial_investment=1000000

fig = plt.figure()
ax = plt.axes(projection='3d')
xdata = confidence_level_list
ydata = holding_period_list
x3d,y3d = np.meshgrid(xdata,ydata)
z3d = initial_investment*(abs(stats.norm.ppf(1-x3d)) * protfolio_vol_log-protfolio_mean_log ) *np.sqrt(y3d)
ax.plot_wireframe(x3d,y3d,z3d,rstride=4,cstride=4,linewidth=1,color='black')
ax.plot_surface(x3d,y3d,z3d,rstride=4,cstride=4,alpha=0.4,cmap=plt.cm.summer)
ax.set_xlabel('\nConfidence level')
ax.set_ylabel('\nHolding Period')
ax.set_zlabel('\nVaR')
plt.tight_layout()
plt.show()






