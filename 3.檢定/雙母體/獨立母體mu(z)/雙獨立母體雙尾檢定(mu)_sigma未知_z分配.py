from scipy import stats
import matplotlib.pyplot as plt
import numpy as np




#H0:mu1-mu2 = 3        Ha:mu1-mu2 != 3
#####################################################臨界值檢定#####################################################
#1.轉成Z統計量
mu1_mu2=3
n1=100
n2=120
x_bar_1 = 0.6121
x_bar_2 = -0.0439
s_1 = 6.5654
s_2 = 7.5295
s_1_sq = s_1**2
s_2_sq = s_2**2
alpha= 0.05 

z_test_stastic = ((x_bar_1-x_bar_2)-mu1_mu2) / (s_1_sq/n1+s_2_sq/n2)**(1/2)
right_limit = stats.norm.ppf(1-alpha/2,0,1)
left_limit = stats.norm.ppf(alpha/2,0,1)
print(f'因為z統計量 {z_test_stastic} 跳出臨界值 {left_limit}~{right_limit},所以拒絕H0')

#2.直接算
mu1_mu2=3
n1=100
n2=120
x_bar_1 = 0.6121
x_bar_2 = -0.0439
s_1 = 6.5654
s_2 = 7.5295
s_1_sq = s_1**2
s_2_sq = s_2**2
alpha= 0.05 
right_limit = stats.norm.ppf(1-alpha/2,mu1_mu2,(s_1_sq/n1+s_2_sq/n2)**(1/2))
left_limit = stats.norm.ppf(alpha/2,mu1_mu2,(s_1_sq/n1+s_2_sq/n2)**(1/2))
x = x_bar_1-x_bar_2
print(f'因為x {x} 跳出臨界值 {left_limit}~{right_limit},所以拒絕H0')

#####################################################p-value檢定#####################################################
#1.轉成z分配計算p-value
mu1_mu2=3
n1=100
n2=120
x_bar_1 = 0.6121
x_bar_2 = -0.0439
s_1 = 6.5654
s_2 = 7.5295
s_1_sq = s_1**2
s_2_sq = s_2**2
alpha= 0.05 
z_test_stastic = ((x_bar_1-x_bar_2)-mu1_mu2) / (s_1_sq/n1+s_2_sq/n2)**(1/2)
p_value = stats.norm.cdf(z_test_stastic,0,1)
print(f'因為p-value {p_value*2} 小於alpha  {alpha},所以拒絕H0')


#2.不轉成z分配計算p-value
mu1_mu2=3
n1=100
n2=120
x_bar_1 = 0.6121
x_bar_2 = -0.0439
s_1 = 6.5654
s_2 = 7.5295
s_1_sq = s_1**2
s_2_sq = s_2**2
alpha= 0.05 

p_value = stats.norm.cdf((x_bar_1-x_bar_2),mu1_mu2,(s_1_sq/n1+s_2_sq/n2)**(1/2))
print(f'因為p-value {p_value*2} 小於alpha  {alpha},所以拒絕H0')


#######################################畫圖#######################################
xbar0=x_bar_1-x_bar_2
sy=(s_1_sq/n1+s_2_sq/n2)**(1/2)
mu0 = 3
z0 = (xbar0-mu0)/sy # -2.4660225684001786
zc = stats.norm.ppf(1-alpha/2,0,1) # 1.959963984540054
# p value
2*stats.norm.cdf(xbar0,mu0,sy) # 0.01366227258371998
2*stats.norm.cdf(z0,0,1) # 0.01366227258371998
[xbar0-zc*sy,xbar0+zc*sy] # [-1.2070081841155336, 2.518978971473118]


plt.figure()
z = np.arange(-4,4,0.01)
plt.plot(z,stats.norm.pdf(z,0,1),lw=3,c='black')
plt.ylim(-0.05,0.45);plt.axhline(y=0,lw=2)
yz = np.linspace(0,0.4,100)
xz1 = np.ones(100)*zc;xz2 = np.ones(100)*-zc
plt.plot(xz1,yz,lw=3,c='black');plt.plot(xz2,yz,lw=3,c='black')
j = z <= -zc
yj = stats.norm.pdf(z[j],0,1)
plt.fill_between(z[j],yj,0, alpha=0.8, color='red')
ja = z >= zc
yja = stats.norm.pdf(z[ja],0,1)
plt.fill_between(z[ja],yja,0, alpha=0.8, color='red')
plt.text(-zc,-0.01,r'-$z_c$',ha='center',va='top')
plt.text(zc,-0.01,r'$z_c$',ha='center',va='top')
plt.text(4,-0.01,'z',ha='center',va='top')
plt.plot(z0,0,marker='o',c='black')
plt.text(z0,-0.01,r'$z_0$',ha='center',va='top')
plt.arrow(2.3,0.01,0.7,0.19)
plt.text(3,0.2,r'$\frac{\alpha}{2}$')
plt.show()