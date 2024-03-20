import pandas as pd

df = pd.read_csv('TPRMOE2018.csv')
print(df.info())


from scipy.stats import ttest_rel
col1 = df['cohnesion1']
col2 = df['cohnesion2']
print(col1.mean(),col2.mean())
print(col1.std(),col2.std())
print(ttest_rel(col1,col2))