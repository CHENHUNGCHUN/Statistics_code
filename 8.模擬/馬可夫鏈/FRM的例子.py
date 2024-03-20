import numpy as np

#初始狀態
I = np.matrix([1,0])   #起始狀態為上漲 
#移轉矩陣
T =np.matrix([[0.75,0.25],
              [0.65,0.35]])

n=3 #3次轉後的結果

for i in range(n):
    T_tmp = I*T
    I=T_tmp
    print(f'The probability of stock price up/down after {i+1} day :{I}')
