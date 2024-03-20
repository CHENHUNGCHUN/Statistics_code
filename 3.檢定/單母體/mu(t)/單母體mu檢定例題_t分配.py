from scipy import stats

'''
此例題為台灣通貨膨脹率的例題
主要是檢定台灣的通貨膨脹率的平均值是否大於一 以及是否小於0
'''

#這個例子是取自於檢定的題目  H0 : mu <= 1 ,Ha :mu > 1  (右尾檢定)
#######################################################用p-value檢定#######################################################
#1. 轉成t統計量計算p-value
mu = 1
n=10
x_bar = 0.492
s = 1.273
s_sq = s**2
alpha = 0.01
v=n-1
t_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
print('t值',t_test_statistic)
p_value = stats.t.cdf(t_test_statistic,df=v) #loc 跟scale不用設定
print(f'因為p_value {(p_value)}大於alpha {alpha},故不拒絕reject H0')  

#2. 直接用x求p-value
mu = 1
n=10
x_bar = 0.492
s = 1.273
s_sq = s**2
alpha = 0.01
v=n-1
p_value = stats.t.cdf(x_bar,df=v,loc=mu,scale=(s_sq/n)**(1/2))
print(f'因為p_value {(p_value)}大於alpha {alpha},故不拒絕reject H0')  
#######################################################用臨界值檢定#######################################################
#1. 轉成t分配計算臨界值
mu = 1
n=10
x_bar = 0.492
s = 1.273
s_sq = s**2
alpha = 0.01
v=n-1
t_rightside = stats.t.ppf(1-alpha,v,0,1)  #臨界值
t_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
print(f'因為t統計量{t_test_statistic} 小於臨界值 {t_rightside},故不拒絕 H0')

#2. 直接用x計算臨界值
mu = 1
n=10
x_bar = 0.492
s = 1.273
s_sq = s**2
alpha = 0.01
v=n-1
t_rightside = stats.t.ppf(1-alpha,v,mu,(s_sq/n)**(1/2))  
x_leftside = mu+t_rightside*((s_sq/n)**(1/2))  
#臨界值 因為ppf是用1-alpha 代表算出來的東西是右邊的t值 是為正值(書上的z 或t 因為有左右積的問題 所以公式寫起來跟寫python正負號可能不一楊) x_leftside 是用mu+t_leftside
print(f'因為x_bar {x_bar} 小於臨界值 {x_leftside},故不拒絕 H0')


print("#"*30 ,'第二題')

#這個例子是取自於檢定的題目  H0 : mu = 0 ,Ha :mu != 0  (右尾檢定)
#######################################################用p-value檢定#######################################################
#1. 轉成t值求p-value
mu = 0
n=10
x_bar = 0.492
s = 1.273
s_sq = s**2
alpha = 0.05
v=n-1
t_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
p_value = stats.t.cdf(t_test_statistic,df=v)
print('t值',t_test_statistic)
print(f'因為p_value*2 {(p_value)*2}大於alpha {alpha},故不拒絕 H0')  


#2. 直接用x求p-value
mu = 0
n=10
x_bar = 0.492
s = 1.273
s_sq = s**2
alpha = 0.05
v=n-1
z_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
alpha = 0.05
p_value = stats.t.cdf(x_bar,df=v,loc=mu,scale=(s_sq/n)**(1/2))
print(f'因為p-value*2 {(p_value)*2}大於alpha {alpha},故不拒絕 H0')


#######################################################用臨界值檢定#######################################################
#1. 轉t分配計算臨界值
mu = 0
n=10
x_bar = 0.492
s = 1.273
s_sq = s**2
alpha = 0.05
v=n-1
t_Rightside = stats.t.ppf(1-alpha/2,v,0,1)  #臨界值
t_leftside = stats.t.ppf(alpha/2,v,0,1)
t_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
print(f'因為t統計量{t_test_statistic} 介於臨界值{t_leftside}~{t_Rightside},故不拒絕 H0')

#2. 直接用x計算臨界值
mu = 0
n=10
x_bar = 0.492
s = 1.273
s_sq = s**2
alpha = 0.05
v=n-1
t_Rightside = stats.t.ppf(1-alpha/2,v,0,1)  #t右邊的統計量
t_leftside = stats.t.ppf(alpha/2,v,0,1) #t左邊的統計量
x_leftside = mu+t_leftside*((s_sq/n)**(1/2))  #臨界值 
x_rightside = mu+t_Rightside*((s_sq/n)**(1/2)) #臨界值 
print(f'因為x_bar {x_bar}介於臨界值{x_leftside}~{x_rightside},故不拒絕 H0')  

