import pandas as pd
import scipy.stats as stats

#資料餵進去的時候為寬表格

df = pd.read_csv('python2011nsc.csv')
# print(df.describe())

########################################################################################################
# 檢定two-way anova (交互作用不顯著) 
import pingouin as pg
import researchpy as rp
# 統計資料描述
cont1 = rp.summary_cont(df['pl'].groupby(df['Gender'])).round(3)
print(cont1)
cont2 = rp.summary_cont(df['pl'].groupby(df['Race'])).round(3)
print(cont2)
print('==================================================')
# two-way ANOVA 檢定
print('法1.')
print(df.anova(dv='pl',between=['Gender','Race'],effsize='n2').round(3))


print('法2.')
import statsmodels.formula.api as sm
import statsmodels.api as sm1
formula = 'pl~C(Gender)*C(Race)'     #如果是類別型 記得加C 不然不用加
model = sm.ols(formula,df).fit()
print(sm1.stats.anova_lm(model,typ=2))


'''
Gender*Race的交互作用p-value為0.912 > 0.05 表不顯著 代表兩者沒有交互作用 ,可以直接看Gender跟Race的one-way結果
不過因為Gender只有2項 (0,1) 且 p-Value 為0.011 > 0.05 表示不拒絕H0 就是兩者的母體平均值沒有顯著差異
但是Race有三項(1,2,3) 且 p-value 0.002小於0.05 表示拒絕H0 三者至少有一項的母體平均值顯著差異 ,所以做Race的事後比較分析(Tukey)
'''
#Race的事後比較分析(Tukey)
from statsmodels.stats.multicomp import pairwise_tukeyhsd
dfaovpost = pairwise_tukeyhsd(df['pl'],df['Race'],alpha=0.05)
print(dfaovpost.summary())

print('==================================================')
# 檢定two-way anova (交互作用顯著)
# 統計資料描述
cont1 = rp.summary_cont(df['pl'].groupby(df['Race'])).round(3)
print(cont1)
cont2 = rp.summary_cont(df['pl'].groupby(df['ExpectEdu'])).round(3)
print(cont2)
print('==================================================')
print(df.anova(dv='pl',between=['Race','ExpectEdu'],effsize='n2'))
'''
Race*ExpectEdu 的交互作用p-value為 < 0.05 表顯著 代表兩者有交互作用 ,需要做後續的 單純主要效果(simple main effect)分析
'''
#單純主要效果(simple main effect)分析
import statsmodels.stats.multicomp as mc
interaction_groups = 'Race_'+df.Race.astype(str)+'&'+'ExpectEdu_'+df.ExpectEdu.astype(str)   #建立group名稱時候用
comp = mc.MultiComparison(df['pl'],interaction_groups)
post_hoc_res = comp.tukeyhsd()
print(post_hoc_res.summary())
