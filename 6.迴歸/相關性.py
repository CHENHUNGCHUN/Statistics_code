import pandas as pd

df = pd.read_csv('python2011nsc.csv')
x1 = df['pl']
x2 = df['achievement']
result = x1.corr(x2)


#檢定相關性 (H0 : r = 0 兩變項之間無顯著相關)
import scipy.stats as stats
result2 = stats.pearsonr(df['pl'],df['achievement'])
print(result2)
'''
reject H0 =>顯示兩者有顯著相關 但相關係數僅0.2
'''

#作圖
#1.pandas
import matplotlib.pyplot as plt
df.plot.scatter(x='pl',y='achievement')
plt.show()
#2.matplotlibe
import matplotlib.pyplot as plt
plt.scatter(df['pl'],df['achievement'],c='darkblue',alpha=0.5)
plt.show()
#3.seanborn
import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(x='pl',y='achievement',data=df)
plt.show()

#熱力圖
import seaborn as sns
df_col = df[['pl','achievement']]
print(df_col.corr())
sns.heatmap(df_col.corr(),annot=True,vmin=-1,vmax=1)
plt.show()