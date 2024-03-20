import pandas as pd
from itertools import combinations
import statsmodels.formula.api as smf

df = pd.read_csv('python2011nsc.csv')

variable=[]
aic=[]
bic=[]
Cond=[]
R_sq=[]

for i in range(1,len(df.columns.values[0:-1])):
    var = list(combinations(df.columns.values[0:-2],i))
    for v in var:
        formula = "pl"+"~"+"+".join(v)
        lm = smf.ols(formula,df).fit()
        bic.append(lm.bic)
        aic.append(lm.aic)
        variable.append(v)
        Cond.append(lm.condition_number)
        R_sq.append(lm.rsquared)
        print(formula)

df = pd.DataFrame()
df['variable'] = variable
df['bic'] = bic
df['aic'] = aic
df['Cond'] = Cond
df['R_sq'] = R_sq

df.sort_values('bic',ascending=True)