import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib as mlp

'''
建議分布(proposal distribution) 就是穩態馬可夫鍊的移轉機率矩陣
'''

'''
rvs:随机变量（就是从这个分布中抽一些样本）
pdf：概率密度函数。
cdf：累计分布函数
sf：残存函数（1-CDF）
ppf：分位点函数（CDF的逆）
isf：逆残存函数（sf的逆）
stats:返回均值，方差，（费舍尔）偏态，（费舍尔）峰度。
moment:分布的非中心矩。
'''


#pmf =>離散的機率分部的x值機率
#pdf =>連續的機率分部的x值機率


def target_dist(likelihood,prior_dist,n,k,theta):
    if theta < 0 or theta > 1:
        return 0
    else:
        return likelihood(n,theta).pmf(k)*prior_dist.pdf(theta)    #後驗機率 = 先驗分布 * likelihood

likelihood = stats.binom
alpha = 20  #for beta模型用
beta  = 20  #for beta模型用
prior = stats.beta(alpha,beta)   #beta分配
n = 100
k = 70

sigma = 0.2
theta = 0.3  #theta 是個機率
accept_num = 0
MC_num = 100000 #模擬5000次

samples= np.zeros(MC_num+1)  #裝機率theta用的
samples[0] = theta 
for i in range(MC_num):
    theta_p = theta + stats.norm(0,sigma).rvs()  #從長態分配(0,0.2)抽取樣本 ,然後更新theta
    rho = min(1,target_dist(likelihood,prior,n,k,theta_p)/target_dist(likelihood,prior,n,k,theta))
    #檢驗是否reject新的theta
    u = np.random.uniform()
    if rho>u:
        accept_num +=1
        theta = theta_p  #如果接受就更新原始theta
    samples[i+1] = theta  #因為是從0開始抓 又因為第一筆是原始theta  所以更新/未更新的theta位置放在下一個

#true posterior distribution
post = stats.beta(k+alpha ,n-k+beta)
thetas = np.linspace(0,1,200)

#assume markov chain stationary after half MC simulation number
n_stationary  = len(samples) //2

#畫圖
mlp.style.use('ggplot')
plt.figure(figsize=(14,8))
plt.hist(prior.rvs(n_stationary),50,histtype='step',density=True,linewidth=1,label='Prior distribution') 
plt.hist(samples[n_stationary:],50,histtype='step',density=True,linewidth=1,label='Target/Posterior distribution') 
plt.plot(thetas,post.pdf(thetas),c='red',linestyle='--',alpha=0.5,label='True posterior distribution')
plt.xlim(0,1)
plt.legend(loc='best')
plt.show()