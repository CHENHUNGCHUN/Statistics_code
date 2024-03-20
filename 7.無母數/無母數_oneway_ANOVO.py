import pandas as pd

df= pd.read_csv('python2011nsc.csv')

#取代one-way ANOVA (多組母體的中位數是否相等)  
#法1. welch (較建議用這個)
import pingouin as pg
print(pg.welch_anova(dv='pl',between='Race',data=df))

#法2. Kruskal-Wallis H-test for independent samples
import pingouin as pg
print(pg.kruskal(dv='pl',between='Race',data=df,detailed = True))


#如果多組母體中位數檢定出來是顯著不同,就可以繼續後續 事後比較分析,使用的方法是Games-Howell方式
import pingouin as pg
print(pg.pairwise_gameshowell(dv='pl',between='Race',data=df))
'''
這邊的t值是正的 是代表群組A-B ,意思是說1,2比3大,然後有顯著不同

'''
