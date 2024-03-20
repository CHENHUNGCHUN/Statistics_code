from scipy import stats

# H0: sigma1 <= sigma2  Ha:sigma1 > sigma2 
#####################################################臨界值檢定#####################################################
n1 = 20
n2 = 15
s1 = 10.72380
s2 = 6.708203
s1_sq = s1**2
s2_sq = s2**2
alpha = 0.05
v1=n1-1
v2=n2-1

f_test_stastic = s1_sq/s2_sq
left_limit = stats.f.ppf(1-alpha,v1,v2)
print(f'因為F統計量 {f_test_stastic} 大於臨界值區間 {left_limit},所以拒絕H0')


#####################################################p-value檢定#####################################################
n1 = 20
n2 = 15
s1 = 10.72380
s2 = 6.708203
s1_sq = s1**2
s2_sq = s2**2
alpha = 0.05
v1=n1-1
v2=n2-1

f_test_stastic = s1_sq/s2_sq
p_value = 1-stats.f.cdf(f_test_stastic,v1,v2)
print(f'因為p-value {p_value} 小於alpha {alpha},所以拒絕H0')