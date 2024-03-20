import pandas as pd


#H0:性別與期望的教育程度之間沒有關聯性  Ha:性別與期望的教育程度之間有關聯性

table = pd.read_csv('python2011nsc.csv')
df_1 = table[['Gender','ExpectEdu']] #Gender 的1 為男生 2 為女生     ExpectEdu的 1為高中 2大學 3碩士 4博士

#轉成列聯表
#因為ExpectEdu的4 (博士) 數量太少 所以合併3(碩士)
df_1['ExpectEdu'] = df_1 ['ExpectEdu'].map({1:'H',2:'U',3:'M',4:'M'}) #M 碩士以上
#轉成次數
from collections import Counter
frequency_count = Counter(df_1['ExpectEdu'])
print(frequency_count)
df_key = frequency_count.keys()
df_value = frequency_count.values()
frequency_table = pd.DataFrame(zip(df_key,df_value),columns = ['expectedu_1','fre'])
print(frequency_table)

#建立指標變數列聯表
expectedu_2 = frequency_table['expectedu_1'].tolist()
print(expectedu_2)
#取得另一指標變數之一的對應數值頻率計次
#男性
M_1 = df_1[df_1['ExpectEdu']==expectedu_2[0]][df_1['Gender']==1].shape[0]
M_2= df_1[df_1['ExpectEdu']==expectedu_2[1]][df_1['Gender']==1].shape[0]
M_3 = df_1[df_1['ExpectEdu']==expectedu_2[2]][df_1['Gender']==1].shape[0]
list1 = [M_1,M_2,M_3]
print(list1)
#女性
F_1 = df_1[df_1['ExpectEdu']==expectedu_2[0]][df_1['Gender']==0].shape[0]
F_2= df_1[df_1['ExpectEdu']==expectedu_2[1]][df_1['Gender']==0].shape[0]
F_3 = df_1[df_1['ExpectEdu']==expectedu_2[2]][df_1['Gender']==0].shape[0]
list2 = [F_1,F_2,F_3]
print(list2)

#建立最終關聯表
chi_table=pd.DataFrame(zip(list1,list2),columns=['男性','女性'],index=[expectedu_2[0],expectedu_2[1],expectedu_2[2]])
print(chi_table)


#跑卡方檢定
import numpy as np
obs = np.array([chi_table.iloc[0,:].tolist(),
                chi_table.iloc[1,:].tolist(),
                chi_table.iloc[2,:].tolist()
                ])
print(obs)

from scipy import stats

alpha=0.05
chi2_test_statstic,p_value,v,ex = stats.chi2_contingency(obs,correction=False)
print(p_value)
print(f'p-value{p_value}小於alpha值{alpha},故拒絕H0,表示性別與期望的教育程度之間有關聯性')