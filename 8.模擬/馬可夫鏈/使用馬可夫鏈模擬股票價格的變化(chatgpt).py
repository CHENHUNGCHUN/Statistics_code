import numpy as np
import pandas as pd

# 載入股票歷史數據
data = pd.read_csv('stock_prices.csv')

# 計算價格變化
returns = data['Close'].pct_change()

# 將價格變化轉換為狀態
def get_state(ret):
    if ret > 0.01:
        return 2   
    elif ret < -0.01:
        return 0
    else:
        return 1

states = np.zeros(len(returns))
for i in range(1, len(returns)):
    states[i] = get_state(returns[i])

# 計算轉移概率矩陣
def get_transition_matrix(states):
    n = int(states.max() + 1)
    A = np.zeros((n, n))
    for i in range(1, len(states)):
        A[int(states[i-1]), int(states[i])] += 1
    A /= A.sum(axis=1)[:,None]
    return A

# 模擬股票價格變化
def simulate_stock_price(n, start_price, A):
    prices = np.zeros(n)
    prices[0] = start_price
    state = np.random.choice(len(A), p=A[0])
    for i in range(1, n):
        prices[i] = prices[i-1] * (1 + returns[i] * A[state][get_state(returns[i])])
        state = get_state(returns[i])
    return prices

# 計算轉移概率矩陣
A = get_transition_matrix(states)

# 模擬100天的股票價格變化
prices = simulate_stock_price(100, data['Close'].iloc[-1], A)