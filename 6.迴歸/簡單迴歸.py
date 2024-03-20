import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('python2011nsc.csv')


#法1.
y=df['ExpectEdu']
x=df['FaEdu']
x=sm.add_constant(x)
Edumodel = sm.OLS(y,x).fit()
print(Edumodel.summary())
'''
解釋能力4.3% (R-sq) ，顯著有效迴歸 F的p-value 小於0.05,迴歸係數:截距項 1.8946 FaEdu 0.1254 ,兩者pvalue均顯著 (p-value <0.05 reject 係數=0的假設)
'''
#法2.
import statsmodels.formula.api as sm
model2 = sm.ols('ExpectEdu~FaEdu',df).fit()
print(model2.summary())

#法3.
import pingouin as pg
lm = pg.linear_regression(df['FaEdu'],df['ExpectEdu'])
print(lm.round(3))