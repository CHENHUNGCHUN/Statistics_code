import pandas as pd

df = pd.read_csv('python2011nsc.csv')
print(df)
print(df.info())
print(df.describe())

print(df[['pl','al']].describe())

print('========================================================')
#單一樣本t檢定

from scipy import stats
#檢定是否常態分布
print('=======================常態分配檢定=======================')
#H0 :資料服從常態分配  H1 :資料不服從常態分配 
print(stats.shapiro(df['Grade']))

#t檢定
print('=======================t檢定=======================')
print(df['Grade'].mean(),df['Grade'].std())
#H0 :Mu=70  H1 :Mu != 70 
print(stats.ttest_1samp(df['Grade'],70))
'''
p-value 小於0.05 表拒絕 H0: Grade的母體平均數=70的假設  ,Grade的母體平均數與70有顯著差異
'''