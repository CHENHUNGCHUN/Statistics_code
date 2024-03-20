import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('python2011nsc.csv')

'''
H0:資料符從常態分布
H1:資料不服從常態分佈
'''

import scipy 
print(scipy.stats.shapiro(df['Grade'])) #小樣本
print(scipy.stats.normaltest(df['Grade'])) #大樣本

#K-S test
print(scipy.stats.kstest(df['Grade'],cdf='norm'))
print(scipy.stats.kstest(df['Grade'],cdf='norm',args=(1000,1545131)))
#(cdf可以輸入 https://docs.scipy.org/doc/scipy/reference/stats.html#module-scipy.stats 裡面的任意分配)


#畫常態分佈圖(qq plot)
import statsmodels.api as sm
sm.qqplot(df['a2'],line='q')
plt.show()


#畫長條圖(histgram)
plt.hist(df['a1'],density=True)
plt.show()
