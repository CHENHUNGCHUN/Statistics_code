from scipy import stats


# H0: P1-P2 = 0.05  Ha:P1-P2 != 0.05
#####################################################臨界值檢定#####################################################
#1.轉成z值
P1_P2=0.05
p1_hat = 0.65
p2_hat = 0.6
n1=1200
n2=2000
alpha = 0.01


z_test_stastic = ((p1_hat-p2_hat)-P1_P2) / ((p1_hat*(1-p1_hat)/n1)+(p2_hat*(1-p2_hat)/n2)) **(1/2)
right_limit = stats.norm.ppf(1-alpha/2,0,1)
left_limit = stats.norm.ppf(alpha/2,0,1)
print(f'因為z統計量 {z_test_stastic} 介於臨界值區間 {left_limit}~{right_limit},所以不拒絕H0')

#2.不轉成z值
P1_P2=0.05
p1_hat = 0.65
p2_hat = 0.6
n1=1200
n2=2000
alpha = 0.01

x=p1_hat-p2_hat
right_limit = stats.norm.ppf(1-alpha/2,P1_P2,((p1_hat*(1-p1_hat)/n1)+(p2_hat*(1-p2_hat)/n2)) **(1/2))
left_limit = stats.norm.ppf(alpha/2,P1_P2,((p1_hat*(1-p1_hat)/n1)+(p2_hat*(1-p2_hat)/n2)) **(1/2))
print(f'因為x {x} 介於臨界值區間 {left_limit}~{right_limit},所以拒絕H0')

#####################################################p-value檢定#####################################################
#1.轉成z值
P1_P2=0.05
p1_hat = 0.65
p2_hat = 0.6
n1=1200
n2=2000
alpha = 0.01

z_test_stastic = ((p1_hat-p2_hat)-P1_P2) / ((p1_hat*(1-p1_hat)/n1)+(p2_hat*(1-p2_hat)/n2)) **(1/2)
p_value = 1-stats.norm.cdf(z_test_stastic)
print(f'因為p-value {p_value*2} 大於alpha {alpha},所以不拒絕H0')

#2.不轉成z值
P1_P2=0.05
p1_hat = 0.65
p2_hat = 0.6
n1=1200
n2=2000
alpha = 0.01

x=p1_hat-p2_hat
p_value = 1-stats.norm.cdf(x,P1_P2,((p1_hat*(1-p1_hat)/n1)+(p2_hat*(1-p2_hat)/n2)) **(1/2))
print(f'因為p-value {p_value*2} 大於alpha {alpha},所以不拒絕H0')
