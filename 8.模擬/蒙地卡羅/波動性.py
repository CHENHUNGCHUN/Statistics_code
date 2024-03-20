import pandas_datareader
import numpy as np

sp500 = pandas_datareader.data.DataReader(['sp500'],'fred',start='12-28-2010',end='12-28-2020')
log_return = np.log(sp500/sp500.shift(1))  #日報酬率
volitilty = np.var(log_return)   #日變異數
std = np.std(log_return)  #日標準差
print(volitilty[0])

#annualize daily standard deviation
#目前因為是日的標準差, 所以如果要變成年標準差,需要日標準差* 265的開根號
std_y = std*265**(1/2)
print(std_y[0])
