from scipy import stats


# H0: P1-P2 >= 0  Ha:P1-P2 < 0
#####################################################臨界值檢定#####################################################
#1.轉成z值
P1_P2=0
p1_hat = 0.46
p2_hat = 0.49
n1=500
n2=600
alpha = 0.05
p_pooled = (n1*p1_hat+n2*p2_hat) /(n1+n2)

z_test_stastic = ((p1_hat-p2_hat)-P1_P2) / ((p_pooled*(1-p_pooled))*(1/n1+1/n2)) **(1/2)
right_limit = stats.norm.ppf(alpha,0,1)
print(f'因為z統計量 {z_test_stastic} 大於臨界值 {right_limit},所以不拒絕H0')

#2.不轉成z值
P1_P2=0
p1_hat = 0.46
p2_hat = 0.49
n1=500
n2=600
alpha = 0.05
p_pooled = (n1*p1_hat+n2*p2_hat) /(n1+n2)

x=p1_hat-p2_hat
right_limit = stats.norm.ppf(alpha,P1_P2,((p_pooled*(1-p_pooled))*(1/n1+1/n2))**(1/2))
print(f'因為x {x} 大於臨界值 {right_limit},所以不拒絕H0')

#####################################################p-value檢定#####################################################
#1.轉成z值
P1_P2=0
p1_hat = 0.46
p2_hat = 0.49
n1=500
n2=600
alpha = 0.05
p_pooled = (n1*p1_hat+n2*p2_hat) /(n1+n2)

z_test_stastic = ((p1_hat-p2_hat)-P1_P2) / ((p_pooled*(1-p_pooled))*(1/n1+1/n2)) **(1/2)
p_value = stats.norm.cdf(z_test_stastic)
print(f'因為p-value {p_value} 大於alpha {alpha},所以不拒絕H0')

#2.不轉成z值
P1_P2=0
p1_hat = 0.46
p2_hat = 0.49
n1=500
n2=600
alpha = 0.05
p_pooled = (n1*p1_hat+n2*p2_hat) /(n1+n2)

x=p1_hat-p2_hat
p_value = stats.norm.cdf(x,P1_P2,((p_pooled*(1-p_pooled))*(1/n1+1/n2)) **(1/2))
print(f'因為p-value {p_value} 大於alpha {alpha},所以不拒絕H0')
