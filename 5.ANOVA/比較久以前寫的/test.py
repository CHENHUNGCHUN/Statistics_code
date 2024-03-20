import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd  #two-way-ANOVA
from statsmodels.stats.multicomp import MultiComparison  #多重比較

data = pd.read_csv('test123.csv')
print(data)
print(pd.crosstab(data['v'],(data['d'])))
model = ols('respond ~ C(d)+C(v)',data = data).fit()  #v是block
print(sm.stats.anova_lm(model,typ=2))


mc = MultiComparison (data['respond'],data['d'])
mcresult = mc.tukeyhsd(0.05)
print(mcresult)

'''
# print(pairwise_tukeyhsd(data['respond'],data['v'],alpha=0.05)) #v是block
print(pairwise_tukeyhsd(data['respond'],data['d'],alpha=0.05))
'''