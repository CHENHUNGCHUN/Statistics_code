from scipy import stats
import matplotlib.pyplot as plt
import numpy as np



#這個例子是取自於檢定的題目  H0 : sigma >= 2 ,Ha :sigma < 2    (sigma是變異數 不是標準差)
#######################################################用臨界值檢定#######################################################

n = 20
sigma = 2
s = 1.273067
s_sq = s**2
v=n-1
alpha = 0.05
chi2_statstic = ((n-1)*s_sq)/sigma
print(chi2_statstic)
left_limit_line=stats.chi2.ppf(alpha,df=v)
print(left_limit_line)
print(f'因為卡方統計量 {chi2_statstic} 大於 臨界值 {left_limit_line}, 故不拒絕H0')

#######################################################用p-value檢定#######################################################
p_value = stats.chi2.cdf(chi2_statstic,df=v)
print(f'因為p_value {p_value} 大於alpha值 {alpha}, 故不拒絕H0')








###############################################################畫圖###############################################################
'''
綠色是卡方值
'''
# H0: sigma2 >= 2
sigma02 = 2
s2 =1.6207
chi0 = (n-1)*s2/sigma02 # 15.396514510466325
chic = stats.chi2.ppf(alpha,n-1) # 10.117013063859044

# 圖 6-14
plt.figure()
x = np.linspace(0,50,200)
plt.plot(x,stats.chi2.pdf(x,df=n-1),lw=3,c='black')
plt.ylim(-0.01,0.07);plt.axhline(y=0,lw=2)
plt.text(50,-0.002,r'$\chi^2$',va='top',ha='center')
x1 = np.ones(100)*chic
y1 = np.linspace(0,0.06,100)
plt.plot(x1,y1,lw=3,c='black')
plt.plot(chi0,0,marker='o',c='black')
j = x <= chi0
yj = stats.chi2.pdf(x[j],n-1)
plt.fill_between(x[j],yj,0, alpha=0.8, color='green')
plt.text(chi0,-0.002,r'$\chi^2_0$',va='top',ha='center')
plt.text(chic,-0.002,r'$\chi^2_c$',va='top',ha='center')
ja = x <= chic
yja = stats.chi2.pdf(x[ja],n-1)
plt.fill_between(x[ja],yja,0, alpha=0.8, color='red')
plt.text(0,0.06,r'reject $H_0$')
plt.text(8,0.005,r'$\alpha$')
plt.text(35,0.06,r'$H_0:\sigma^2 \geq 2$')
plt.axis('off')
plt.show()