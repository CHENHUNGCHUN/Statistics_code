from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


#這個例子是取自於檢定的題目  H0 : sigma = 1.5 ,Ha :sigma != 1.5    (sigma是變異數 不是標準差)
#######################################################用臨界值檢定#######################################################

n = 20
sigma = 1.5
s = 1.273067
s_sq = s**2
v=n-1
alpha = 0.05
chi2_statstic = ((n-1)*s_sq)/sigma
print(f'卡方值 {chi2_statstic}')
left_limit_line=stats.chi2.ppf(alpha/2,df=v) #左邊臨界值
print(f'左邊臨界值 {left_limit_line}')
right_limit_line=stats.chi2.ppf(1-alpha/2,df=v) #右邊臨界值
print(f'右邊臨界值 {right_limit_line}')
print(f'因為卡方統計量 {chi2_statstic} 介於 臨界值 {left_limit_line} ~ {right_limit_line}, 故不拒絕H0')

#######################################################用p-value檢定#######################################################
p_value = stats.chi2.cdf(chi2_statstic,v)
print(f'p_value {(1-p_value)*2} 大於alpha {alpha} 故不拒絕H0')






###############################################################畫圖###############################################################
'''
綠色是卡方值
'''
# H0: sigma2 = 1.5
sigma20 = 1.5
s2 =1.6207
chi0 = (n-1)*s2/sigma20 # 20.5286860139551
chic1 = stats.chi2.ppf(alpha/2,n-1) # 8.906516481987971
chic2 = stats.chi2.ppf(1-alpha/2,n-1) # 32.85232686172969
# (n-1)*s2/sigma2
[(1/chic2)*(n-1)*s2,(1/chic1)*(n-1)*s2] # [0.9373165301360752, 3.4573594607057325]

# 圖 6-16
plt.figure()
x = np.arange(0,50,0.01)
plt.plot(x,stats.chi2.pdf(x,n-1),lw=3,c='black')
plt.ylim(-0.01,0.07);plt.axhline(y=0,lw=2)
y1 = np.linspace(0,0.06,100)
x1 = np.ones(100)*chic1
x2 = np.ones(100)*chic2
plt.plot(x1,y1,lw=3,c='black')
plt.plot(x2,y1,lw=3,c='black')
plt.text(50,-0.002,r'$\chi^2$',ha='center',va='top')
j = x <= chic1
yj = stats.chi2.pdf(x[j],n-1)
plt.fill_between(x[j],yj,0, alpha=0.8, color='red')
ja = x >= chic2
yja = stats.chi2.pdf(x[ja],n-1)
plt.fill_between(x[ja],yja,0, alpha=0.8, color='red')
plt.text(chic1,-0.002,r'$\chi^2_a$',ha='center',va='top')
plt.text(chic2,-0.002,r'$\chi^2_b$',ha='center',va='top')
plt.plot(chi0,0,marker='o',c='black')
plt.text(chi0,-0.002,r'$\chi^2_0$',ha='center',va='top')
plt.text(40,0.06,r'reject $H_0$')
plt.text(0,0.06,r'reject $H_0$')
plt.axis('off')
plt.show()

