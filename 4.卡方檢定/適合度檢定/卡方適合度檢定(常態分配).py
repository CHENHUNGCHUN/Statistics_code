
#H0 : 學生的統計學分數符合常態分布   Ha:學生的統計學分數不符合常態分布

'''
分數區間:
小於 73 、  73-78 、 78-82 、 82-87 、 大於87
'''
import numpy as np
import statistics
from scipy.stats import norm

o=[10,21,36,27,6] #對應分數區間實際觀察到的分數
n = 100
mu = 80;sigma = 5

y = norm.rvs(mu,sigma,n)
ybar = np.mean(y) # 79.80473063965647
sy = statistics.stdev(y) # 4.9212040915471205
alpha = 0.01

e=[]  #算出來的理論分數    理論分數