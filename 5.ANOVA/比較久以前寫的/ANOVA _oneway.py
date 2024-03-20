import pandas as pd
import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

a = [349.4,348,349.8,344.5,353.5,345.8,346.8,344.7,348.3,347.6]
b = [347.8,349.2,347.8,348.1,348.1,347.6,348.3,347.1,346.5,347.6]
c = [350.8,350.1,348.9,351.2,349.6,348.5,350.9,349.6,351,351.2]
d = [349.8,351.4,350.9,349.5,346.8,350.9,351,349.5,351.6,347.6]

'''
a = [85, 86, 88, 75, 78, 94, 98, 79, 71, 80]
b = [91, 92, 93, 90, 97, 94, 82, 88, 95, 96]
c = [79, 78, 88, 94, 92, 85, 83, 85, 82, 81]
'''

print(f_oneway(a, b, c))

df = pd.DataFrame({'score': [349.4,348,349.8,344.5,353.5,345.8,346.8,344.7,348.3,347.6,
                             347.8,349.2,347.8,348.1,348.1,347.6,348.3,347.1,346.5,347.6,
                             350.8,350.1,348.9,351.2,349.6,348.5,350.9,349.6,351,351.2,
                             349.8,351.4,350.9,349.5,346.8,350.9,351,349.5,351.6,347.6],
                   'group': np.repeat(['機台一', '機台二', '機台三','機台四'], repeats=10)}) 
print(df)
tukey = pairwise_tukeyhsd(endog=df['score'],
                          groups=df['group'],
                          alpha=0.05)
print(tukey)

'''
機台一跟機台三 有顯著不同
機台一跟機台四 有顯著不同
機台三根機台二 有顯著不同
機台四根機台二 有顯著不同

Thus, we would conclude that there is a statistically significant difference between the means of groups a and b 
and groups b and c, but not a statistically significant difference between the means of groups a and c.
'''