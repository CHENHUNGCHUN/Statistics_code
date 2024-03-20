from  scipy import stats


#這個例子是取自於檢定的題目  H0 : mu <= -0.5 ,Ha :mu > 0.5
#######################################################用p-value檢定#######################################################
#1. 常態分配計算p-value
mu = -0.5
n=193
x_bar = 0.0754
s = 6.8684
s_sq = s**2
alpha = 0.05
p_value = stats.norm.cdf(x_bar,mu,(s_sq/n)**(1/2))
print(f'因為p_value {1-p_value}大於alpha {alpha},故沒有證據去reject H0')#因為是右尾檢定(cdf是從左邊積到右邊) ,所以記得要用1-p_value 

#2. 轉成標準常態分配計算p-value
mu = -0.5
n=193
x_bar = 0.0754
s = 6.8684
s_sq = s**2
z_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
alpha = 0.05
p_value = stats.norm.cdf(z_test_statistic,0,1)
print(f'因為p-value {1-p_value}大於alpha {alpha},故沒有證據去reject H0') #因為是右尾檢定(cdf是從左邊積到右邊) ,所以記得要用1-p_value 

#######################################################用臨界值檢定#######################################################
#1. 轉成標準常態分配計算臨界值
mu = -0.5
n=193
x_bar = 0.0754
s = 6.8684
s_sq = s**2
alpha = 0.05
z_leftside = stats.norm.ppf(1-alpha,0,1)  #臨界值
z_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
print(f'因為Z統計量{z_test_statistic} 小於臨界值 {z_leftside},故不reject H0')

#2. 直接用x算臨界值
mu = -0.5
n=193
x_bar = 0.0754
s = 6.8684
s_sq = s**2
alpha = 0.05
z_leftside = stats.norm.ppf(1-alpha,0,1)  #臨界值
x_leftside = mu+z_leftside*((s_sq/n)**(1/2))  #臨界值 
print(f'因為x_bar {x_bar} 小於臨界值 {x_leftside},故不reject H0')

'''
注意一下如果都是值接求左尾的z值的話(alpha),公式記得是用x_bar + z(alpha)*s
但如果是用右尾的z值的話(1-alpha),公式記得是要用x_bar - z(alpha)*s
解釋:
如果是看統計書的話 其實Z檢定的左邊臨界值都是用 1-alpha 在求  
只是因為左右對稱的關係(且因為是查表),所以公式都是寫x_bar - z(1-alpha)*s (那個z因為是用1-alpha 所以會是正數,所以才會是相減)
但因為現在用電腦可以直接積分,所以可以直接求出左邊的z值,實際上會是負值 ,所以公式上差了一個負號,公式應該會要改成x_bar + z(alpha)*s
當然 如果是雙尾檢定就記得要alpha/2
'''