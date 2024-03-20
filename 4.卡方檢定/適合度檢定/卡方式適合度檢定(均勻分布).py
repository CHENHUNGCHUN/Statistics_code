import pandas as pd
from scipy import stats

'''
廠商生產一款袋裝巧克力產品,其內容物的包裝分別有 紅、黃、藍、綠、橙、白 6種顏色,抽取一袋240顆樣本,想要了解個顏色是否都是均勻分布
(應該是就是一袋裡面 有各種不同顏色的包裝,包裝裡面裝一個巧克力)
因為是要算均勻分布 所以理論值(期望值)的每個顏色的數量應該都是要一樣
'''

#H0:巧克力包裝的6種顏色都均勻分布  Ha:巧克力包裝的6種顏色 都不服從均勻分布

alpha = 0.05

df = pd.read_excel('均勻分布.xlsx')
print(df)

f_obs = [48,31,36,52,46,27]   #觀察值
f_exp = [40,40,40,40,40,40]   #理論值(期望值)

chi_test_stastics,p_value = stats.chisquare(f_obs,f_exp)
print(f'因為p-value {p_value} 小於alpha {alpha} 所以拒絕H0,即不服從均勻分布')