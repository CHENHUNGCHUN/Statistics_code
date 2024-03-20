import pandas as pd
import scipy.stats as stats

#資料餵進去的時候為寬表格

df = pd.read_csv('python2011nsc.csv')
print(df.describe())

########################################################################################################
# 檢定one-way anova  (法1 法2結果都相同)
#1.法一
# 檢定變異數是否相同   (如果不同 理論上應該是要用無母數統計的one-way ;H0 是假設k組樣本的sigma 都相同)
print(stats.levene(df['pl'][df['Race']==1],
                df['pl'][df['Race']==2],
                df['pl'][df['Race']==3]))
#用pingouin檢定one-way
import pingouin as pg
anova = pg.anova(dv='pl',between='Race',data = df,detailed = True)    # dv  應變數   between 應該就是組間(自變數)
print(anova)


#2.法二
# 檢定變異數是否相同 (如果不同 理論上應該是要用無母數統計的one-way ;H0 是假設k組樣本的sigma 都相同)
G=df['Race'].unique()
args=[]
for i in list(G):
    args.append(df[df['Race']==i]['pl'])
print(stats.levene(*args))
#用scipy的stats檢定one-way
print(stats.f_oneway(*args))

# 直接用f_oneway只能看到結果 要知道detail 還要用statsmodels才能抓到
from statsmodels.formula.api import ols
import statsmodels.api as sm
dfaov = sm.stats.anova_lm(ols('pl~C(Race)',df).fit())    #如果是類別型 記得加C 不然不用加
print(dfaov)

########################################################################################################
#事後比較分析

#法1.pairwise(Tukey事後比較法 HSD)
import pingouin as pg
print(pg.pairwise_ttests(dv='pl',between='Race',padjust='bonf',data=df).round(3))  #'bonf'為Bonferroni方法
'''
第一組 (1、2) p-value 大於0.05,代表不拒絕H0,即沒有證據顯示1、2組有顯著差異;
第二組(1、3)、第三組(2、3)的p-value都小於0.05 ,代表有顯著差異,且t值為正(group 1 - group 2) ,代表1、2組平均數大於3
'''

#法2.pairwise_tukeyhsd(Tukey事後比較法 HSD)
from statsmodels.stats.multicomp import pairwise_tukeyhsd
dfaovpost = pairwise_tukeyhsd(df['pl'],df['Race'],alpha=0.05)
print(dfaovpost.summary())
#meandiff是 group2 減group1的數(所以如果是負的 代表group1 大於group 2)

#法3.multicomp(Tukey事後比較法 HSD)
import statsmodels.stats.multicomp as mc
comp = mc.MultiComparison(df['pl'],df['Race'])
post_hoc_res = comp.tukeyhsd()
print(post_hoc_res.summary())
#meandiff是 group2 減 group1的數(所以如果是負的 代表group1 大於group 2)


#法4.Bonderroni法
import statsmodels.stats.multicomp as mc
comp = mc.MultiComparison(df['pl'],df['Race'])
tb1, a1, a2=comp.allpairtest(stats.ttest_ind,method='bonf')
print(tb1)

