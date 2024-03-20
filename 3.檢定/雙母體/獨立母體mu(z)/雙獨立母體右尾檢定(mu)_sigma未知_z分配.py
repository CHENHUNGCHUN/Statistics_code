from scipy import stats

'''
其實未知sigma 只能用t分配;但是因為大樣本 所以可以用z分配 (n很大的時候t會很接近z)
'''
#H0 :mu1-mu2 <= 0  Ha:mu1-mu2 > 0 
#####################################################臨界值檢定#####################################################
#1.轉成Z統計量
mu1_mu2=0
n1=100
n2=120
x_bar_1 = 0.6121
x_bar_2 = -0.0439
s_1 = 6.5654
s_2 = 7.5295
s_1_sq = s_1**2
s_2_sq = s_2**2
alpha= 0.05 

z_test_stastic=((x_bar_1-x_bar_2) - mu1_mu2) / (s_1_sq/n1+s_2_sq/n2)**(1/2)
right_limit = stats.norm.ppf(1-alpha,0,1)
print(f'臨界值為 {right_limit}')
print(f'z 統計量 {z_test_stastic}')
print(f'因為z統計量 {z_test_stastic} 小於臨界值 {right_limit},所以不拒絕H0')

#2.直接算
mu1_mu2=0
n1=100
n2=120
x_bar_1 = 0.6121
x_bar_2 = -0.0439
s_1 = 6.5654
s_2 = 7.5295
s_1_sq = s_1**2
s_2_sq = s_2**2
alpha= 0.05 
right_limit = stats.norm.ppf(1-alpha,mu1_mu2,(s_1_sq/n1+s_2_sq/n2)**(1/2))
x =x_bar_1-x_bar_2
print(f'因為x {x} 小於臨界值 {right_limit},所以不拒絕H0')
#####################################################p-value檢定#####################################################
#1.轉成z分配計算p-value
mu1_mu2=0
n1=100
n2=120
x_bar_1 = 0.6121
x_bar_2 = -0.0439
s_1 = 6.5654
s_2 = 7.5295
s_1_sq = s_1**2
s_2_sq = s_2**2
alpha= 0.05 
z_test_stastic=((x_bar_1-x_bar_2) - mu1_mu2) / (s_1_sq/n1+s_2_sq/n2)**(1/2)
p_value = 1-stats.norm.cdf(z_test_stastic,0,1) #因為是右尾 所以要1-p_value (cdf是從左邊積到右)
print(f'因為p-value {p_value} 大於alpha  {alpha},所以不拒絕H0')


#2.不轉成z分配計算p-value
mu1_mu2=0
n1=100
n2=120
x_bar_1 = 0.6121
x_bar_2 = -0.0439
s_1 = 6.5654
s_2 = 7.5295
s_1_sq = s_1**2
s_2_sq = s_2**2
alpha= 0.05 

x =x_bar_1-x_bar_2
p_value = 1-stats.norm.cdf(x,mu1_mu2,(s_1_sq/n1+s_2_sq/n2)**(1/2))  #因為是右尾 所以要1-p_value (cdf是從左邊積到右)
print(f'因為p-value {p_value} 大於alpha  {alpha},所以不拒絕H0')