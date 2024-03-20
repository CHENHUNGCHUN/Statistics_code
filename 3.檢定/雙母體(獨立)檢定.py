import pandas as pd

df = pd.read_csv('python2011nsc.csv')

#變異數同質性檢定 (兩個母體的變異數是否相等)
import scipy.stats as stats
#H0:樣本母體變異數相同 H1:樣本母體變異數不同
print(stats.levene(df['pl'][df['Gender']==1],
            df['pl'][df['Gender']==0]
            ,center='mean'))
'''
pvalue >0.05 ,non-reject H0 ,樣本母體變異數相同
'''
#雙母體(獨立)檢定
group1 = df['pl'][df['Gender']==1]
group2 = df['pl'][df['Gender']==0]
print(group1.count(),group1.mean(),group1.std())
print(group2.count(),group2.mean(),group2.std())
#H0 兩母體的平均值相同 ,H1 兩母體的平均值不同
print(stats.ttest_ind(group1,group2,equal_var=True))

#因為stats的ttest只能看到最終結果  要看detail的話可以用researchpy的ttest呈現
import researchpy as rp
print(rp.ttest(group1=group1,group1_name='Male',
                group2=group2,group2_name='FEMale'))
