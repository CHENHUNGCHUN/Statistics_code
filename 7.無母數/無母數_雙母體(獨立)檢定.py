import pandas as pd

df=pd.read_csv('python2011nsc.csv')

#檢定常態分配
#1. 小樣本 (n<30)   shapiro
from scipy import stats
dfrandom = df.sample(n=25)
print(stats.shapiro(dfrandom['pl']))

#2. 大樣本 (n>=30)  normaltest
from scipy import stats
print(stats.normaltest(df['pl']))

#檢定變異數同質性
from scipy import stats
print(stats.levene(df['pl'][df['Gender']==1],
                df['pl'][df['Gender']==0],
                center = 'mean'))

#雙母體(獨立)檢定 wilcoxon rank sum test (母體中位數是否相同;雙尾檢定)
from scipy import stats
print(stats.ranksums(df[df['Gender']==1]['pl'],
                df[df['Gender']==0]['pl']))

#雙母體(獨立)檢定 M-W U test (母體中位數是否相同;雙尾檢定)
from scipy import stats
print(stats.mannwhitneyu(df[df['Gender']==1]['pl'],
                df[df['Gender']==0]['pl'],
                use_continuity=True,
                alternative = 'two-sided'))