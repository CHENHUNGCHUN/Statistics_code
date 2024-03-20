from scipy import stats

# H0: mu_d =0 Ha:mu_d != 0
#####################################################臨界值檢定#####################################################
#轉成t統計量 
mu_d=0
d_bar = 0.1517
s_d = 6.4114
s_d_sq = s_d**2
alpha= 0.05 
n=193
v=n-1

t_test_statics=(d_bar-mu_d)/(s_d_sq/n)**(1/2)
left_limit = stats.t.ppf(alpha/2,v)
right_limit = stats.t.ppf(1-alpha/2,v)
print(f'因為t統計量 {t_test_statics} 介於臨界值 {left_limit}~{right_limit} 之間,所以不拒絕H0')
#####################################################p-value檢定#####################################################
#轉成t統計量 
mu_d=0
d_bar = 0.1517
s_d = 6.4114
s_d_sq = s_d**2
alpha= 0.05 
n=193
v=n-1

t_test_statics=(d_bar-mu_d)/(s_d_sq/n)**(1/2)
p_value = 1-stats.t.cdf(t_test_statics,v)
print(f'因為p-value {p_value*2} 大於alpha {alpha},所以不拒絕H0')