from  scipy import stats


#這個例子是取自於檢定的題目  H0 : mu >= 0.03 ,Ha :mu < 0.03
#######################################################用p-value檢定#######################################################
#1. 常態分配計算p-value
mu = 0.03
n=193
x_bar = -0.076
s = 6.6786
s_sq = s**2
alpha = 0.05
print(stats.norm.cdf(x_bar,mu,(s_sq/n)**(1/2)))
print('因為p-value大於alpha,故沒有證據去reject H0')

#2. 轉成標準常態分配計算p-value
mu = 0.03
n=193
x_bar = -0.076
s = 6.6786
s_sq = s**2
z_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
alpha = 0.05
print(stats.norm.cdf(z_test_statistic,0,1))
print('因為p-value大於alpha,故沒有證據去reject H0')

#######################################################用臨界值檢定#######################################################
#1. 轉成標準常態分配計算臨界值
mu = 0.03
n=193
x_bar = -0.076
s = 6.6786
s_sq = s**2
alpha = 0.05
z_leftside = stats.norm.ppf(1-alpha,0,1)  #臨界值
z_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
print(f'因為Z統計量{z_test_statistic} 大於臨界值 {z_leftside},故不reject H0')

#2. 直接用常態分配計算臨界值
mu = 0.03
n=193
x_bar = -0.076
s = 6.6786
s_sq = s**2
alpha = 0.05
z_leftside = stats.norm.ppf(1-alpha,0,1)  #臨界值
x_leftside = mu-z_leftside*((s_sq/n)**(1/2))  #臨界值 
print(f'因為x_bar {x_bar} 大於臨界值 {x_leftside},故不reject H0')

