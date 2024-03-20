import pandas as pd
import numpy as np
import yfinance as yf

df= yf.download('spy',start='2022-01-01',end='2023-02-01')
returns = df['Close'].pct_change()
print(returns)

# 將價格變化轉換為狀態
def get_state(ret):
    if ret > 0.01:
        return 2   
    elif ret < -0.01:
        return 0
    else:
        return 1

states = np.zeros(len(returns))
print(states)
for i in range(1,len(returns)):
    states[i] = get_state(returns[i])
print(states)

# 計算轉移概率矩陣
n=int(states.max() + 1)
A = np.zeros((n,n))   
print(n)
print(A)

for i in range(1,len(states)):
    A[int(states[i-1]), int(states[i])] += 1
    print(A)
A /= A.sum(axis=1)[:,None]#把每一列的總和除以各自列的數值   [:,None]這個一定要加
print(A)


prices = np.zeros(100)  #未來100天
prices[0] = df['Close'].iloc[-1] #因為是要預測未來100天的股價 所以第一個股價是有資料的最後一筆
print(A[0])
print(len(A))
print(np.random.choice(len(A)))
state = np.random.choice(len(A), p=A[0]) #用0.25  0.58823529 0.16176471  的機率抽一組0-2的數字

print(returns[1],A[state],get_state(returns[1]))
'''
昨天的價格 + 昨天的價格*(過去股價的第一組報酬率)*(由A(轉移概率矩陣)取出來的機率)
'''