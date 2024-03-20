from  scipy import stats

'''
題目 1.:
大學生身高分配的標準差為30.6公分,現在從該大學隨機抽出120位學生,平均身高為170公分
試於alpha=0.1之下檢視學生平均身高是否至少166公分以上?
'''
#這個例子是取自於檢定的題目  H0 : mu <= 166 ,Ha :mu > 166
#######################################################用p-value檢定#######################################################
#1. 常態分配計算p-value
mu = 166
n=120
x_bar = 170
s = 30.6
s_sq = s**2
alpha = 0.1
p_value = stats.norm.cdf(x_bar,mu,(s_sq/n)**(1/2))  
print(f'因為p_value {1-p_value}小於alpha {alpha},故reject H0') #因為是右尾檢定(cdf是從左邊積到右邊) ,所以記得要用1-p_value 

#2. 轉成標準常態分配計算p-value
mu = 166
n=120
x_bar = 170
s = 30.6
s_sq = s**2
z_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
alpha = 0.1
p_value = stats.norm.cdf(z_test_statistic,0,1) 
print(f'因為p-value {1-p_value}小於alpha {alpha},故reject H0') #因為是右尾檢定(cdf是從左邊積到右邊) ,所以記得要用1-p_value 
 
#######################################################用臨界值檢定#######################################################
#1. 轉成標準常態分配計算臨界值
mu = 166
n=120
x_bar = 170
s = 30.6
s_sq = s**2
alpha = 0.1
z_leftside = stats.norm.ppf(1-alpha,0,1)  #臨界值
z_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
print(f'因為Z統計量{z_test_statistic} 大於臨界值 {z_leftside},故reject H0')

#2. 直接用常態分配計算臨界值
mu = 166
n=120
x_bar = 170
s = 30.6
s_sq = s**2
alpha = 0.1
z_leftside = stats.norm.ppf(1-alpha,0,1)  #臨界值
x_leftside = mu+z_leftside*((s_sq/n)**(1/2))  #臨界值 
print(f'因為x_bar {x_bar} 大於臨界值 {x_leftside},故reject H0')




print('#'*60,'第二題')
'''
題目2.:
大學生身高分配的標準差為30.6公分,現在從該大學隨機抽出120位學生,平均身高為170公分
試於alpha=0.1之下檢視學生平均身高是否等於166公分?
'''

#這個例子是取自於檢定的題目  H0 : mu = 166 ,Ha :mu != 166
#######################################################用p-value檢定#######################################################
#1. 常態分配計算p-value
mu = 166
n=120
x_bar = 170
s = 30.6
s_sq = s**2
alpha = 0.1
p_value = stats.norm.cdf(x_bar,mu,(s_sq/n)**(1/2))
print(f'因為p_value*2 {(1-p_value)*2}大於alpha{alpha},故不能reject H0')

#2. 轉成標準常態分配計算p-value
mu = 166
n=120
x_bar = 170
s = 30.6
s_sq = s**2
alpha = 0.1
z_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
p_value = stats.norm.cdf(z_test_statistic,0,1)
print(f'因為p-value*2 {(1-p_value)*2}大於alpha{alpha},故不能reject H0')

#######################################################用臨界值檢定#######################################################
#1. 轉成標準常態分配計算臨界值
mu = 166
n=120
x_bar = 170
s = 30.6
s_sq = s**2
alpha = 0.1
z_Rightside = stats.norm.ppf(1-alpha/2,0,1)  #臨界值
z_leftside = stats.norm.ppf(alpha/2,0,1)
z_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
print(f'因為Z統計量{z_test_statistic} 並未跳出臨界值{z_leftside}~{z_Rightside},故不能reject H0')

#2. 直接用常態分配計算臨界值
mu = 166
n=120
x_bar = 170
s = 30.6
s_sq = s**2
alpha = 0.1
z_Rightside = stats.norm.ppf(1-alpha/2,0,1)  #算右邊的z值
z_lefttside = stats.norm.ppf(alpha/2,0,1)  #算右邊的z值
x_leftside = mu+z_leftside*((s_sq/n)**(1/2))  #臨界值 
x_rightside = mu+z_Rightside*((s_sq/n)**(1/2)) #臨界值 
print(f'因為x_bar {x_bar} 並未跳出臨界值{x_leftside}~{x_rightside},故不能reject H0')  

