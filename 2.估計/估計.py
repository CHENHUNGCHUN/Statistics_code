from scipy import stats

#################################################################估計母體平均數#################################################################
#估計母體的mu (大樣本) ->z分配
x_bar=172
s=25
s_sq=s**2 #母體sigma已知就帶sigma ,不知的話就用樣本的s
n=100
alpha = 0.05
z_rightside = stats.norm.ppf((1-alpha/2),0,1)  #正的z值
z_leftside = stats.norm.ppf(alpha/2,0,1)  #負的z值
print('母體mu在樣本平均數為',x_bar,'的前提下,95%信心水準的區間估計: ',round(x_bar-z_rightside*(s_sq/n)**(1/2),4),'~',round(x_bar+z_rightside*(s_sq/n)**(1/2),4))

#估計母體的mu (小樣本) ->t分配
x_bar=7750
s=900
s_sq=s**2  #基本上只能用樣本的s
n=25
v = n-1
alpha = 0.05
t_rightside = stats.t.ppf((1-alpha/2),v)
t_leftside = stats.t.ppf((alpha/2),df=v)
print('母體mu在樣本平均數為',x_bar,'的前提下,95%信心水準的區間估計: ',round(x_bar-t_rightside*(s_sq/n)**(1/2),4),'~',round(x_bar+t_rightside*(s_sq/n)**(1/2),4))


#################################################################估計母體比率#################################################################

#估計母體的P (只有大樣本) ->z分配

p_hat=0.282
q_hat=1-p_hat
n=1000
alpha = 0.05
z_rightside = stats.norm.ppf((1-alpha/2),0,1)  #正的z值
z_leftside = stats.norm.ppf(alpha/2,0,1)  #負的z值
print('母體P在樣本平均數為',p_hat,'的前提下,95%信心水準的區間估計: ',round(p_hat-z_rightside*((p_hat*q_hat)/n)**(1/2),4),'~',round(p_hat+z_rightside*((p_hat*q_hat)/n)**(1/2),4))


#################################################################估計母體sigma#################################################################\

n=20
s=6.854925
s_sq = s**2
alpha = 0.05
v=n-1
chi_rightside = stats.chi2.ppf(alpha/2,df=v)
chi_leftside = stats.chi2.ppf(1-alpha/2,df=v)
print('母體sigma在樣本標準差為',s,'的前提下,95%信心水準的區間估計: ',round((n-1)*s_sq/chi_leftside,4),'~',round((n-1)*s_sq/chi_rightside,4))


######################################################估計雙群體的的sigma是否相同######################################################

n1=11
n2=11
s1=65**(1/2)
s2=77**(1/2)
s1_sq = s1**2
s2_sq = s2**2
alpha = 0.05
v1 = n1-1
v2 = n2-1
f_rightside = stats.f.ppf((alpha/2),v1,v2)
f_leftside =stats.f.ppf((alpha/2),v2,v1)
print('估計雙母體的變異數比值為',round((s1_sq/s2_sq)*f_leftside,4),'~',round((s1_sq/s2_sq)/f_rightside,4)\
    ,'其中因為包含了1 表示兩個母體的sigma沒有顯著差異')


