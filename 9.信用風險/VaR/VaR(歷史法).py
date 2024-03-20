import pandas as pd
import pandas_datareader
import matplotlib.pyplot as plt
import scipy.stats as stats
import tabulate
import yfinance as yfin
import numpy as np

#不需要假設報酬率服從常態分佈

yfin.pdr_override()
price = pandas_datareader.data.get_data_yahoo('AAPL', start='2015-11-30', end='2020-11-30')[['Adj Close']]

returns = np.log(price/price.shift(1))
returns= returns.dropna()

#計算風險值 因為直接用股價過去的報酬率當作分配,所以直接排序後用分位數就可以直接算出來VaR值
returns.sort_values('Adj Close',ascending=True,inplace=True)

HistVaR_90 = returns.quantile(0.1,interpolation='lower')[0]  #interpolation 主要是調整如果剛好不能整除的時候 要選哪一個數 lower 代表是直接取比較小的   midpoint 就是兩個數加起來平均
HistVaR_95 = returns.quantile(0.05,interpolation='lower')[0]
HistVaR_99 = returns.quantile(0.01,interpolation='lower')[0]
#print(HistVaR_90)
print(tabulate.tabulate([['90%',HistVaR_90],['95%',HistVaR_95],['99%',HistVaR_99]],headers=['confidence level','VaR']))


#參數法以及歷史法比較

#參數法
mu = np.mean(returns['Adj Close'])
std = np.std(returns['Adj Close'])
ParaVar_90 = stats.norm.ppf(1-0.9,mu,std)
ParaVar_95 = stats.norm.ppf(1-0.95,mu,std)
ParaVar_99 = stats.norm.ppf(1-0.99,mu,std)
print(tabulate.tabulate([['90%',ParaVar_90],['95%',ParaVar_95],['99%',ParaVar_99]],headers=['confidence level','VaR']))

#比較圖

plt.style.use('ggplot')
fig,ax = plt.subplots(1,1,figsize=(12,6))
x=np.linspace(mu-5*std,mu+5*std,500)
ax.hist(returns['Adj Close'],bins=100,density=True,histtype='stepfilled',alpha=0.5)
ax.axvline(HistVaR_95,ymin=0,ymax=0.2,color='g',ls=':',alpha=0.7,label="0.95% historical VaR")
ax.axvline(ParaVar_95,ymin=0,ymax=0.2,color='r',ls=':',alpha=0.7,label="0.95% Parametic VaR")
ax.plot(x,stats.norm.pdf(x,mu,std))
ax.legend()
ax.set_title('Return distribution')
ax.set_xlabel('Return')
ax.set_ylabel('Frequncy')
plt.show()