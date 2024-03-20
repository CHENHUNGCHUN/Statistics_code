import matplotlib.pylab as plt
import numpy as np
from scipy.integrate import quad

'''
目標是要估計出 那個"參數" λ 
就是鯊魚攻擊人的平均次數
會用gamma主要是因為x軸可以為0到無限大
只是alpha (a)  跟beta (b)要先設定好狀態
然後持續更新 alpha 跟 beta 去改變gamma分配的型態
'''

# x 的範圍由 0.0 到 15.0, 間隔 0.001
x = np.arange(0.0, 15.0, 0.001)
#先假設alpha 跟 beta 為2.1跟1 (書中有解釋為什麼)
a=2.1
b=1
# 算gamma "function"     gamma function 是在gamma distribution中
def g_f(t):
    return t**(a-1) * np.exp(-t)
# 算出 gamma 函數的值
def gamma(x):
    return quad(g_f, 0.0, np.inf)   #從0積分到無限大
ans, err = gamma(a)

# 將所有的 x 值代入 gamma 機率密度函數, 算出對應的密度(gamma 分配)
g_pdf1 = (b**a * x**(a-1) * np.exp(-b*x)) / gamma(a)[0]
######################################################更新第一次 ->接受到新資料  一年內發生了五起鯊魚攻擊事件######################################################
#用捷徑算出更新過後的alpha 跟 beta
a=7.1
b=2.0
#算出更新後的gamma分配
g_pdf2 = (b**a * x**(a-1) * np.exp(-b*x)) / gamma(a)[0]
######################################################更新第二次 ->接受到新資料  另外5年的鯊魚攻擊次數######################################################
#用捷徑算出更新過後的alpha 跟 beta
a=17.1
b=7.0
g_pdf3 = (b**a * x**(a-1) * np.exp(-b*x)) / gamma(a)[0]


# 畫出 gamma 機率密度圖形
plt.grid(True)
plt.ylim(0,0.8)
plt.plot(x, g_pdf1, color='b', linewidth=2)
plt.plot(x, g_pdf2, color='purple', linewidth=1)
plt.plot(x, g_pdf3, "--", color='purple', linewidth=1)
plt.xlabel('λ')
plt.ylabel('density')
plt.show()

#########################################################更新結束 表達目前資料更新後的分配#########################################################
#信賴區間表達目前的λ可能範圍  (90%的信心水準)
import scipy.stats as stats

print(stats.gamma.ppf([0.01, 0.5, 0.90],a=17.1,loc =(17.1/7)/7,scale=1/7))  #目前loc = (alpha / beta) / beta   scale = 1/beta  但不知道對不對 (好像要在多除beta)


