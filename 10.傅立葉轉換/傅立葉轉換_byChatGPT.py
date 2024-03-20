import random
import numpy as np
import matplotlib.pyplot as plt

# 生成900個隨機數作為每日營收
np.random.seed(0)
daily_revenue = np.random.randint(100, 1000, 900)

# 繪製原始數據
plt.figure(figsize=(10, 5))
plt.plot(daily_revenue)
plt.title("Daily Revenue over 900 Days")
plt.xlabel("Days")
plt.ylabel("Revenue")
plt.show()


# 對信號進行傅立葉轉換
'''
在傅立葉分析中，DC成分或稱直流成分，是指一個信號中的平均值或基準值。在進行傅立葉變換時，DC成分通常會在頻譜中顯示為頻率為0的分量。

在上面的例子中，營收資料是從100到1000的隨機整數，因此平均值接近550，而頻譜圖中的0頻率分量表示的就是該平均值，因此頻譜中0頻率處的震幅就很高。

可以通過將信號的平均值從原始數據中減去來消除DC成分，從而改善頻譜圖的可讀性。在python中，可以使用以下代碼實現：
'''
daily_revenue = daily_revenue - np.mean(daily_revenue)
fft_result = np.fft.fft(daily_revenue)

# 計算頻率和幅度

n = daily_revenue.size
timestep = 1  # 每天的時間間隔為1
freq = np.fft.fftfreq(n, d=timestep)
amplitude = np.abs(fft_result) / n

# 繪製頻譜圖
'''
x軸是代表天數 只是要記得除以1  => 0.02代表  1/0.02 = 50天
'''
plt.figure(figsize=(10, 5))
plt.plot(freq, amplitude)
plt.title("Frequency Spectrum of Daily Revenue over 900 Days")
plt.xlabel("Frequency (1/day)")
plt.ylabel("Amplitude")
plt.xlim(0, 0.05)
plt.show()






###########################################################################################################################有週期性的
import numpy as np
import matplotlib.pyplot as plt

# 生成週期性營收數據
t = np.arange(0, 900)
daily_revenue = 500 + 200 * np.sin(2 * np.pi * t / 30) + 50 * np.sin(2 * np.pi * t / 7) + 10 * np.random.randn(len(t))
daily_revenue = daily_revenue-np.mean(daily_revenue)
# 傅立葉轉換
y = np.fft.fft(daily_revenue)
freq = np.fft.fftfreq(len(daily_revenue))

# 繪製頻譜圖
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(freq, np.abs(y))
ax.set_xlabel('頻率（Hz）')
ax.set_ylabel('震幅')
ax.set_xlim(0, 0.1)
ax.set_ylim(0, 1500)
plt.show()
'''
其中 30 天的 (0.03  ; 1/0.03 =30) 震幅非常明顯的高 代表30天可能會是一個週期性
'''