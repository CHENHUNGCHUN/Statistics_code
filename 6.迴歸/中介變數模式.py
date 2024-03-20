import pandas as pd

df = pd.read_csv('python2011nsc.csv')

import pingouin as pg
print(pg.mediation_analysis(data=df,x='al',m='ss',y='achievement'))

'''
若將中介變數放入模式中 x的係數變小 但對y的影響仍然顯著 此中介變項對模式的影響為Partial mediation 
即x對y的雖有影響 但有一部份是透過中介變項影響y。
若將中介變數放入模式中 x的係數變小 但對y的影響已不顯著 此中介變項對模式的影響為Full mediation 
即x對y的影響不顯著 而是完全透過中介變項影響y。
'''