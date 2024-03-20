import pandas as pd
import numpy as np
import scipy.stats as statas

'''
有間學校餐廳經營者想要了解學生對於餐點A、B、C與加點飲料與否之間的關係,故調查某一時段的點餐組合資料想要了解學生與加點飲料之間的關係
'''

# H0 :餐點與加點飲料相互獨立,沒有關係　Ha:餐點與加點飲料有關

alpha=0.05
df = pd.read_excel('獨立性檢定.xlsx')
obs = np.array([[20,16,14],[10,30,10]])
chi2_test_statstic,p_value,v,ex=statas.chi2_contingency(obs,correction=False)
#如果資料是2*2的表,會需要做葉慈修正,這時候correction 就要設定為True
print(f'卡方值: {chi2_test_statstic},p-value: {p_value},自由度: {v} ,預期值: {ex}')
print(f'因為p-value {p_value} 小於 alpha {alpha} ,故拒絕H0')