import pandas as pd
import numpy as np
from scipy.stats import norm

# 假設您已經有了一個包含市場數據的DataFrame，其中包含債券的價格、收益率和到期時間等信息
df = pd.read_csv('bond_market_data.csv')

# 計算債券的違約概率，假設債券到期時間為T年，收益率為y，無風險收益率為r
def default_prob(T, y, r):
    d1 = (np.log(1 / (1 - y)) + (r + 0.5 * (0.2 ** 2)) * T) / (0.2 * np.sqrt(T))
    d2 = d1 - 0.2 * np.sqrt(T)
    return norm.cdf(-d2)

# 將計算違約概率的函數應用到DataFrame中的每個債券上
df['default_prob'] = df.apply(lambda x: default_prob(x['time_to_maturity'], x['yield'], 0.02), axis=1)

# 計算違約密度，假設時間間隔為1年
default_density = (df['default_prob'].shift(-1) - df['default_prob']) / (df['time_to_maturity'].shift(-1) - df['time_to_maturity'])
df['default_density'] = default_density.fillna(method='backfill')

# 查看計算出來的違約密度
print(df['default_density'])

#################################################################################################################################################


import pandas as pd

# 假設您有一個包含債券市場數據的DataFrame，其中包含債券的價格、收益率和到期時間等信息
df = pd.DataFrame({
    'bond_id': [1, 2, 3, 4, 5],
    'price': [99.5, 101.2, 95.8, 98.7, 100.1],
    'yield': [0.025, 0.028, 0.035, 0.032, 0.030],
    'time_to_maturity': [2.5, 3.0, 4.0, 1.5, 2.0]
})

# 計算債券的違約概率，假設債券到期時間為T年，收益率為y，無風險收益率為r
def default_prob(T, y, r):
    # 根據Black-Scholes模型計算違約概率
    # 此處假設風險中立且服從標準正態分佈
    # 其中，0.2是波動率的估計值，這裡用固定值代替了實際波動率的估計
    d1 = (np.log(1 / (1 - y)) + (r + 0.5 * (0.2 ** 2)) * T) / (0.2 * np.sqrt(T))
    d2 = d1 - 0.2 * np.sqrt(T)
    return norm.cdf(-d2)

# 將計算違約概率的函數應用到DataFrame中的每個債券上
df['default_prob'] = df.apply(lambda x: default_prob(x['time_to_maturity'], x['yield'], 0.02), axis=1)

# 計算違約密度，假設時間間隔為1年
default_density = (df['default_prob'].shift(-1) - df['default_prob']) / (df['time_to_maturity'].shift(-1) - df['time_to_maturity'])
df['default_density'] = default_density.fillna(method='backfill')

# 查看計算出來的違約密度
print(df['default_density'])






#################################################################################################################################################




import pandas as pd
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv("data.csv")

# 创建KaplanMeierFitter对象
kmf = KaplanMeierFitter()

# 计算生存率曲线
kmf.fit(data["time"], event_observed=data["status"])

# 绘制生存率曲线
kmf.plot()

# 设置图形标题和标签
plt.title("Survival Curve")
plt.xlabel("Time")
plt.ylabel("Survival Probability")

# 显示图形
plt.show()