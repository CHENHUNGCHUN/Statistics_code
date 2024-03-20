import pandas as pd


df = pd.read_csv('python2011nsc.csv')

#法1.
import statsmodels.formula.api as sm
formula = 'achievement~Sportyear+ExpectEdu+pl+al+ss+tr'
model3 = sm.ols(formula,df).fit()
print(model3.summary())
'''
整體R-sq 14.3% ,且顯著(F test P-value <0.05%),但其中Sportyear、ExpectEdu、tr 的 p-value 大於0.05 not-reject H0:係數=0 
故僅採用截距項、pl、al、ss
'''
#法2.
import pingouin as pg
lm = pg.linear_regression(df[['Sportyear','ExpectEdu','pl','al','ss','tr']],df['achievement'])
print(lm.round(3))