from  scipy import stats


#這個例子是取自於檢定的題目  H0 : mu = 1.2 ,Ha :mu != 1.2
#######################################################用p-value檢定#######################################################
#1. 常態分配計算p-value
mu = 1.2
n=194
x_bar = 0.8644
s = 1.3033
s_sq = s**2
alpha = 0.05
p_value = stats.norm.cdf(x_bar,mu,(s_sq/n)**(1/2))
print(f'因為p_value*2 {(p_value)*2}小於alpha{alpha},故reject H0')  
#因為計算出來的統計量是在左邊(負值) 所以pvalue算出來的值是左邊 故不用1-p_value (所以如果統計量是正值 代表在右側,就需要1-p_value)

#2. 轉成標準常態分配計算p-value
mu = 1.2
n=194
x_bar = 0.8644
s = 1.3033
s_sq = s**2
z_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
alpha = 0.05
p_value = stats.norm.cdf(z_test_statistic,0,1)
print(f'因為p-value*2 {(p_value)*2}大於alpha{alpha},故reject H0')
#因為計算出來的統計量是在左邊(負值) 所以pvalue算出來的值是左邊 故不用1-p_value (所以如果統計量是正值 代表在右側,就需要1-p_value)

#######################################################用臨界值檢定#######################################################
#1. 轉成標準常態分配計算臨界值
mu = 1.2
n=194
x_bar = 0.8644
s = 1.3033
s_sq = s**2
alpha = 0.05
z_Rightside = stats.norm.ppf(1-alpha/2,0,1)  #臨界值
z_leftside = stats.norm.ppf(alpha/2,0,1)
z_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
print(f'因為Z統計量{z_test_statistic} 跳出臨界值{z_leftside}~{z_Rightside},故reject H0')

#2. 直接用x計算臨界值
mu = 1.2
n=194
x_bar = 0.8644
s = 1.3033
s_sq = s**2
alpha = 0.05
z_Rightside = stats.norm.ppf(1-alpha/2,0,1)  #算右邊的z值
z_lefttside = stats.norm.ppf(alpha/2,0,1)  #算右邊的z值
x_leftside = mu+z_leftside*((s_sq/n)**(1/2))  #臨界值 
x_rightside = mu+z_Rightside*((s_sq/n)**(1/2)) #臨界值 
print(f'因為x_bar {x_bar} 跳出臨界值{x_leftside}~{x_rightside},故reject H0')  

'''
注意一下如果都是值接求左尾的z值的話(alpha),公式記得是用x_bar + z(alpha)*s
但如果是用右尾的z值的話(1-alpha),公式記得是要用x_bar - z(alpha)*s
解釋:
如果是看統計書的話 其實Z檢定的左邊臨界值都是用 1-alpha 在求  
只是因為左右對稱的關係(且因為是查表),所以公式都是寫x_bar - z(1-alpha)*s (那個z因為是用1-alpha 所以會是正數,所以才會是相減)
但因為現在用電腦可以直接積分,所以可以直接求出左邊的z值,實際上會是負值 ,所以公式上差了一個負號,公式應該會要改成x_bar + z(alpha)*s
當然 如果是雙尾檢定就記得要alpha/2
'''