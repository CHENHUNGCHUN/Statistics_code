import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_csv('test.csv')
print(data)
print(pd.crosstab(data['factor_A'],(data['factor_B'])))
model = ols('response ~ C(factor_A)+C(factor_B)',data = data).fit()  #B是block?
print(sm.stats.anova_lm(model,typ=2))

from statsmodels.stats.multicomp import pairwise_tukeyhsd  #two-way-ANOVA
from statsmodels.stats.multicomp import MultiComparison  #多重比較

mc = MultiComparison (data['response'],data['factor_A'])
mcresult = mc.tukeyhsd(0.05)
print(mcresult.summary())


