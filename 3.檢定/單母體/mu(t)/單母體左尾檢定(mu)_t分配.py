from scipy import stats

#這個例子是取自於檢定的題目  H0 : mu >= 0.4 ,Ha :mu < 0.4
#######################################################用p-value檢定#######################################################
#1. 轉成t統計量計算p-value
mu = 0.4
n=10
x_bar = -0.033
s = 1.307
s_sq = s**2
alpha = 0.05
v=n-1
t_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
print('t值',t_test_statistic)
p_value = stats.t.cdf(t_test_statistic,df=v) #loc 跟scale不用設定
print(f'因為p_value {(p_value)}大於alpha {alpha},故不拒絕reject H0')  

#2. 直接用x求p-value

mu = 0.4
n=10
x_bar = -0.033
s = 1.307
s_sq = s**2
alpha = 0.05
v=n-1
p_value = stats.t.cdf(x_bar,df=v,loc=mu,scale=(s_sq/n)**(1/2))
print(f'因為p_value {(p_value)}大於alpha {alpha},故不拒絕reject H0')  
#######################################################用臨界值檢定#######################################################
#1. 轉成t分配計算臨界值
mu = 0.4
n=10
x_bar = -0.033
s = 1.307
s_sq = s**2
alpha = 0.05
v=n-1
t_leftside = stats.t.ppf(alpha,v,0,1)  #臨界值
t_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
print(f'因為t統計量{t_test_statistic} 大於臨界值 {t_leftside},故不拒絕 H0')

#2. 直接用x計算臨界值
mu = 0.4
n=10
x_bar = -0.033
s = 1.307
s_sq = s**2
alpha = 0.05
v=n-1
t_leftside = stats.t.ppf(alpha,v,mu,(s_sq/n)**(1/2))  
x_leftside = mu+t_leftside*((s_sq/n)**(1/2))  
#臨界值 因為ppf是用alpha 代表算出來的東西是左邊的t值 是為負值(書上的z 或t 因為有左右積的問題) 所以x_leftside 是用mu+t_leftside 而不是mu-t_leftside
#不然就是ppf 那邊是要用1-alpha計算 則x_leftside就可以用mu-t_leftside
print(f'因為x_bar {x_bar} 大於臨界值 {x_leftside},故不拒絕 H0')