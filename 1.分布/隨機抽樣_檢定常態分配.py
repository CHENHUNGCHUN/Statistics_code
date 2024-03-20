import scipy
import random
import numpy as np
import matplotlib.pyplot as plt 


'''
np.random.rand(n) =>0~1的隨機n個樣本 (圖看起來是均勻分布)
np.random.randn(n) =>抽取自標準常態分佈的n個樣本
np.random.randint(low,high,siz=n) =>取自low~high中的隨機整數樣本   (圖看起來是均勻分布)
scipy.stats.norm.rvs(size=600) #抽600個標準常態分佈的樣本

'''



x= np.random.randn(60000)
plt.hist(x,density=True,bins=30)
plt.show()

import statsmodels.api as sm
sm.qqplot(x,line='q')
plt.show()

print(scipy.stats.kstest(x,cdf='norm'))
print(scipy.stats.kstest(x,cdf='uniform'))
