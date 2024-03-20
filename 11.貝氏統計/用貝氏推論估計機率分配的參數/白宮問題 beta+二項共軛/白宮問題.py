import scipy.stats as stats
from scipy.integrate import quad
import matplotlib.pylab as plt
import numpy as np

'''
目標是要估計出 那個"參數"p
而p本身又是機率的意思  但是在這題 p 是指名詞 不是真的機率
這題是要求出p的機率值 ex: p 為45%的機率  或是p 為10%的機率
'''

# 算出 BETA 函數的值
def Bfun(x):
    return (x**(a-1))*((1-x)**(b-1))
#------
# alpha=0.5, beta=0.5
#------
a=0.5
b=0.5
# 積分                
bfun_value, err = quad(Bfun, 0.0, 1.0)
print("alpha=0.5, beta=0.5, BETA = ", bfun_value)

# p 的範圍由 0.0001 到 1.0, 間隔 0.0001
p = np.arange(0.0001, 1.0, 0.0001)

# 將所有的 p 值代入 beta 機率密度函數, 算出對應的密度
beta_pdf1 = 1/bfun_value * p**(a-1) * (1-p)**(b-1)
# 畫出 beta 機率密度圖形 alpha、beta 都為0.5的圖
plt.grid(True)
plt.ylim(0,3)
plt.plot(p, beta_pdf1)
plt.xlabel('p')
plt.ylabel('beta_pdf(p)')
plt.show()

######################################################更新第一次 ->闖入白宮1次且失敗######################################################
#更新第一次 ->闖入白宮1次且失敗
n=1
y=0
#捷徑
a=a+y
b=b+n-y
#新的beta值
bfun_value2, err = quad(Bfun, 0.0, 1.0)  
# 將所有的 p 值代入 beta 機率密度函數, 算出對應的密度  更新完alpha跟beta後的值
beta_pdf2 = 1/bfun_value2 * p**(a-1) * (1-p)**(b-1)
# 畫出 beta 機率密度圖形
plt.grid(True)
plt.ylim(0,3)
plt.plot(p, beta_pdf1, color='b')
plt.plot(p, beta_pdf2, color='purple')
plt.xlabel('p')
plt.ylabel('beta_pdf(p)')
plt.show()

######################################################再更新一次->闖入白宮1次且還是失敗######################################################
#更新第二次 ->闖入白宮1次且失敗
n=1
y=0
#捷徑
a=a+y
b=b+n-y
#新的beta值
bfun_value3, err = quad(Bfun, 0.0, 1.0)  
# 將所有的 p 值代入 beta 機率密度函數, 算出對應的密度  更新完alpha跟beta後的值
beta_pdf3 = 1/bfun_value3 * p**(a-1) * (1-p)**(b-1)
# 畫出 beta 機率密度圖形
plt.grid(True)
plt.ylim(0,3)
plt.plot(p, beta_pdf2, color='b')
plt.plot(p, beta_pdf3, color='purple')
plt.xlabel('p')
plt.ylabel('beta_pdf(p)')
plt.show()

#########################################################更新結束 表達目前資料更新後的分配#########################################################
#信賴區間表達目前的p可能範圍  (90%的信心水準)
alpha = 0.05
left_limit=stats.beta.ppf(alpha,0.5,2.5)
right_limit=stats.beta.ppf(1-alpha,0.5,2.5)
print(f'更新完資訊後,有90%的信心水準歐尼爾進入白宮的機率介於{left_limit:.2f}%~{right_limit:.2f}%')

pro = stats.beta.cdf(0.1,0.5,2.5)
print(f'歐尼爾再沒有預約情況下進入白宮的機率是10%的機率為{pro:.2f}%')