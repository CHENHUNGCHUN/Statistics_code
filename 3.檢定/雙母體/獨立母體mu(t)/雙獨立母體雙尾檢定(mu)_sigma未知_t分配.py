from scipy import stats
import matplotlib.pyplot as plt
import numpy as np




#H0:mu1-mu2 >= 7.95        Ha:mu1-mu2 < 7.95
#####################################################臨界值檢定#####################################################
#1.轉成t統計量  (兩母體的sigma 不相同)
mu1_mu2=7.95
n1=10
n2=12
x_bar_1 = 0.6183
x_bar_2 = -1.4365
s_1 = 7.8683
s_2 = 7.9993
s_1_sq = s_1**2
s_2_sq = s_2**2
v=((s_1_sq/n1+s_2_sq/n2)**2)/((1/(n1-1))*(s_1_sq/n1)**2+(1/(n2-1))*(s_2_sq/n2)**2)
alpha= 0.05 

t_test_stastic=((x_bar_1-x_bar_2)-mu1_mu2) / (s_1_sq/n1+s_2_sq/n2)**(1/2)
left_limit = stats.t.ppf(alpha,v)
print(f'因為t統計量 {t_test_stastic} 小於臨界值 {left_limit},所以拒絕H0')

#1-2.轉成t統計量  (兩母體的sigma 相同)
mu1_mu2=7.95
n1=10
n2=12
x_bar_1 = 0.6183
x_bar_2 = -1.4365
s_1 = 7.8683
s_2 = 7.9993
s_1_sq = s_1**2
s_2_sq = s_2**2
v=n1+n2-2
alpha= 0.05 

t_test_stastic=((x_bar_1-x_bar_2)-mu1_mu2) / ((((n1-1)*s_1_sq+(n2-1)*s_2_sq)/(n1+n2-2))*(1/n1+1/n2))**(1/2)
left_limit = stats.t.ppf(alpha,v)
print(f'因為t統計量 {t_test_stastic} 大於臨界值 {left_limit},所以不拒絕H0')

#####################################################p-value檢定#####################################################
#1.轉成t統計量  (兩母體的sigma 不相同)
mu1_mu2=7.95
n1=10
n2=12
x_bar_1 = 0.6183
x_bar_2 = -1.4365
s_1 = 7.8683
s_2 = 7.9993
s_1_sq = s_1**2
s_2_sq = s_2**2
v=((s_1_sq/n1+s_2_sq/n2)**2)/((1/(n1-1))*(s_1_sq/n1)**2+(1/(n2-1))*(s_2_sq/n2)**2)
alpha= 0.05 

t_test_stastic=((x_bar_1-x_bar_2)-mu1_mu2) / (s_1_sq/n1+s_2_sq/n2)**(1/2)
p_value = stats.t.cdf(t_test_stastic,v)
print(f'因為p_value統計量 {p_value} 小於alpha {alpha},所以拒絕H0')

#1-2.轉成t統計量  (兩母體的sigma 相同)
mu1_mu2=7.95
n1=10
n2=12
x_bar_1 = 0.6183
x_bar_2 = -1.4365
s_1 = 7.8683
s_2 = 7.9993
s_1_sq = s_1**2
s_2_sq = s_2**2
v=n1+n2-2
alpha= 0.05 

t_test_stastic=((x_bar_1-x_bar_2)-mu1_mu2) / ((((n1-1)*s_1_sq+(n2-1)*s_2_sq)/(n1+n2-2))*(1/n1+1/n2))**(1/2)
p_value = stats.t.cdf(t_test_stastic,v)
print(f'因為p_value統計量 {p_value} 小於alpha {alpha},所以拒絕H0')



