import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

T = (datetime.date(2020,9,30)-datetime.date(2020,9,1)).days / 252
MC_num = 6000 #模擬出6000種股價最後價格
S0 = 857.293
v= 0.2076  #股票的年波動率
r = 0.019  #無風險利率
ST_list=[]
payoff_list=[]
K=900

for i in range(MC_num):
    ST = S0*np.exp((r-0.5*(v**2))*T + v*np.sqrt(T)*(np.random.normal(0,1)))
    ST_list.append(ST)
    payoff_list.append(max(0,ST-K))



plt.plot(ST_list,'o')
plt.hlines(900,xmin=0,xmax=MC_num,color ='r',linestyles='--',label='strike price')
plt.text(MC_num+2,S0,'initial price')
plt.hlines(S0,xmin=0,xmax=MC_num,color ='g',linestyles='--',label='initial price')
plt.text(MC_num+2,900,'stirke price')
plt.xlabel('Number of Simulations')
plt.ylabel('asset price')
plt.show()
print(f'30天候的平均價格為{np.mean(ST_list)}')

discount_factor = np.exp(-r*T)

option_price = discount_factor *(sum(payoff_list) / float(MC_num))   #平均價格 再折現(discount_factor)
print(option_price)