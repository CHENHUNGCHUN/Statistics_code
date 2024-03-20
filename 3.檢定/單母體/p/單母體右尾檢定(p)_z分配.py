from scipy import stats

#這個例子是取自於檢定的題目  H0 : P <= 0.45 ,Ha :P < 0.45 
#######################################################用p-value檢定#######################################################
#1. 轉成z統計量計算p-value
P = 0.45 
n=4567
p_hat = 0.4745
q_hat = 1-p_hat
alpha = 0.05
z_test_statistic = (p_hat-P) / ((P*(1-P))/n)**(1/2)
print('z值',z_test_statistic)
p_value = stats.norm.cdf(z_test_statistic,0,1) #loc 跟scale不用設定
print(f'因為p_value {(1-p_value)}小於alpha {alpha},故拒絕 H0')  

#2. 直接用x求p-value
P = 0.45 
n=4567
p_hat = 0.4745
q_hat = 1-p_hat
alpha = 0.05
p_value = stats.norm.cdf(p_hat,P,((P*(1-P))/n)**(1/2))
print(f'因為p_value {(1-p_value)}小於alpha {alpha},故拒絕 H0')  
#######################################################用臨界值檢定#######################################################
#1. 轉成z分配計算臨界值
P = 0.45 
n=4567
p_hat = 0.4745
q_hat = 1-p_hat
alpha = 0.05
z_righttside = stats.norm.ppf(1-alpha,0,1)  #臨界值
z_test_statistic = (p_hat-P) / ((P*(1-P))/n)**(1/2)
print(f'因為z統計量{z_test_statistic} 大於臨界值 {z_righttside},故拒絕 H0')

#2. 直接用x計算臨界值
P = 0.45 
n=4567
p_hat = 0.4745
q_hat = 1-p_hat
alpha = 0.05
z_rightside = stats.t.ppf(1-alpha,P,((P*(1-P))/n)**(1/2))  
x_rightside = P+z_rightside*((P*(1-P))/n)**(1/2)
#臨界值 因為ppf是用alpha 代表算出來的東西是左邊的t值 是為負值(書上的z 或t 因為有左右積的問題) 所以x_leftside 是用mu+t_leftside 而不是mu-t_leftside
#不然就是ppf 那邊是要用1-alpha計算 則x_leftside就可以用mu-t_leftside
print(f'因為p_hat {p_hat} 小於臨界值 {x_rightside},故不拒絕 H0')
