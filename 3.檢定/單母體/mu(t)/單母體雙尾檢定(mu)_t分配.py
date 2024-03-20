from  scipy import stats


#這個例子是取自於檢定的題目  H0 : mu = 0.95 ,Ha :mu != 0.95
#######################################################用p-value檢定#######################################################
#1. 轉成t值求p-value
mu = 0.95
n=10
x_bar = -0.033
s = 1.307
s_sq = s**2
alpha = 0.05
v=n-1
t_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
p_value = stats.t.cdf(t_test_statistic,df=v)
print(f'因為p_value*2 {(p_value)*2}小於alpha{alpha},故reject H0')  


#2. 直接用x求p-value
mu = 0.95
n=10
x_bar = -0.033
s = 1.307
s_sq = s**2
alpha = 0.05
v=n-1
z_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
alpha = 0.05
p_value = stats.t.cdf(x_bar,df=v,loc=mu,scale=(s_sq/n)**(1/2))
print(f'因為p-value*2 {(p_value)*2}大於alpha{alpha},故reject H0')


#######################################################用臨界值檢定#######################################################
#1. 轉t分配計算臨界值
mu = 0.95
n=10
x_bar = -0.033
s = 1.307
s_sq = s**2
alpha = 0.05
v=n-1
t_Rightside = stats.t.ppf(1-alpha/2,v,0,1)  #臨界值
t_leftside = stats.t.ppf(alpha/2,v,0,1)
t_test_statistic = (x_bar-mu) / (s_sq/n)**(1/2)
print(f'因為t統計量{t_test_statistic} 跳出臨界值{t_leftside}~{t_Rightside},故reject H0')

#2. 直接用x計算臨界值
mu = 0.95
n=10
x_bar = -0.033
s = 1.307
s_sq = s**2
alpha = 0.05
v=n-1
t_Rightside = stats.t.ppf(1-alpha/2,v,0,1)  #t右邊的統計量
t_leftside = stats.t.ppf(alpha/2,v,0,1) #t左邊的統計量
x_leftside = mu+t_leftside*((s_sq/n)**(1/2))  #臨界值 
x_rightside = mu+t_Rightside*((s_sq/n)**(1/2)) #臨界值 
print(f'因為x_bar {x_bar} 跳出臨界值{x_leftside}~{x_rightside},故reject H0')  

'''
注意一下如果都是值接求左尾的t值的話(alpha),公式記得是用x_bar + z(alpha)*s
但如果是用右尾的t值的話(1-alpha),公式記得是要用x_bar - z(alpha)*s
解釋:
如果是看統計書的話 其實t檢定的左邊臨界值都是用 1-alpha 在求  
只是因為左右對稱的關係(且因為是查表),所以公式都是寫x_bar - t(1-alpha)*s (那個t因為是用1-alpha 所以會是正數,所以才會是相減)
但因為現在用電腦可以直接積分,所以可以直接求出左邊的z值,實際上會是負值 ,所以公式上差了一個負號,公式應該會要改成x_bar + t(alpha)*s
當然 如果是雙尾檢定就記得要alpha/2
'''