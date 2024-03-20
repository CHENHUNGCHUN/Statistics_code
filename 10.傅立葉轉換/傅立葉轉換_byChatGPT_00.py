import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 256)
f1, f2, f3 = 10, 20, 30
x = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t) + 0.2*np.sin(2*np.pi*f3*t)
plt.plot(x)
plt.show()

xn = np.fft.fft(x)
freqs = np.fft.fftfreq(len(xn))

# 繪製頻譜表示
plt.plot(freqs, np.abs(xn))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()




import numpy as np
import pandas as pd

# 设置随机数生成器种子，以保证生成的数据是可重复的
np.random.seed(12345)

# 生成100天的股票价格数据
dates = pd.date_range(start='2020-01-01', periods=100, freq='D')
prices = 100.0 + np.cumsum(np.random.randn(100))

# 将股票价格数据保存为CSV文件
data = pd.DataFrame({'date': dates, 'price': prices})
data.to_csv('stock_price.csv', index=False)



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# 读取股票数据
data = pd.read_csv('stock_price.csv', index_col=0)

# 计算傅立叶变换
y = data['price'].values
N = len(y)
timestep = 100  # 时间步长为1
freq = fftfreq(N, d=timestep)
fft_values = fft(y)
fft_amplitude = 2.0/N * np.abs(fft_values)
plt.plot(y)
plt.show()

# 绘制傅立叶变换的频谱图
plt.plot(freq, fft_amplitude)
plt.title('FFT of Stock Price')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.show()





import numpy as np
import matplotlib.pyplot as plt

# 生成時間序列
t = np.linspace(0, 2*np.pi, 1000, endpoint=False)
y = np.sin(t)

# 計算傅立葉變換
fft_y = np.fft.fft(y)

# 計算振幅
amp_y = np.abs(fft_y)

# 計算頻率
freq_y = np.fft.fftfreq(len(y), t[1]-t[0])

# 繪製結果
fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t, y)
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Amplitude')
axs[1].plot(freq_y, amp_y)
axs[1].set_xlabel('Frequency')
axs[1].set_ylabel('Amplitude')
plt.show()



import numpy as np
import matplotlib.pyplot as plt

# 設定時間軸
t = np.linspace(0, 1, 1000)

# 設定頻率
f1 = 10  # 低頻
f2 = 100  # 高頻

# 產生具有低頻和高頻的波形
waveform = np.sin(2*np.pi*f1*t) + 0.2*np.sin(2*np.pi*f2*t)

# 執行傅立葉轉換
spectrum = np.fft.fft(waveform)

# 取得頻率軸
freqs = np.fft.fftfreq(len(waveform), t[1]-t[0])

# 取得振幅
amplitude = np.abs(spectrum)

# 繪製圖形
plt.plot(freqs, amplitude)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()




import csv
import random

with open('revenue.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Quarter', 'Revenue'])
    for i in range(1, 21):
        quarter = f'Q{i}'
        revenue = random.randint(1000, 5000)
        writer.writerow([quarter, revenue])
        
        
        
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('revenue.csv')
revenue = df['Revenue'].values

# 计算傅立叶变换
fourier_transform = np.fft.fft(revenue)
freqs = np.fft.fftfreq(len(revenue))

# 绘制傅立叶变换的振幅谱
plt.figure(figsize=(8, 6))
plt.plot(freqs, np.abs(fourier_transform))
plt.title('Amplitude spectrum of revenue')
plt.xlabel('Frequency (1/quarter)')
plt.ylabel('Amplitude')
plt.show()




'''
import pandas as pd
import numpy as np
import datetime

start_date = datetime.date(2016, 1, 1)
end_date = datetime.date(2021, 12, 31)

date_range = pd.date_range(start_date, end_date, freq='Q')
revenue = np.sin(np.arange(len(date_range)) * 2 * np.pi / 8) + np.sin(np.arange(len(date_range)) * 2 * np.pi / 4) + np.random.normal(0, 0.2, len(date_range))

df = pd.DataFrame({'date': date_range, 'revenue': revenue})
df.to_csv('revenue.csv', index=False)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("revenue.csv", parse_dates=["Quarter"])

# 对数据进行傅立叶变换
revenue_fft = np.fft.fft(df['revenue'])

# 获取对应的频率
freqs = np.fft.fftfreq(len(df['Quarter']), (df['Quarter'].iloc[-1] - df['Quarter'].iloc[0]).days / len(df['Quarter']))

# 绘制傅立叶变换后的频率振幅谱
fig, ax = plt.subplots()
ax.plot(freqs, abs(revenue_fft))
ax.set_xlabel('Frequency (1/Quarter)')
ax.set_ylabel('Amplitude')
ax.set_xlim([0, 0.5])
plt.show()
'''


import numpy as np
import matplotlib.pyplot as plt

# 設定每日營收數據
revenue = [500, 700, 600, 800, 900, 1000, 1200]

# 計算傅立葉轉換
fft = np.fft.fft(revenue)

# 計算相應的頻率
freq = np.fft.fftfreq(len(revenue))

# 繪製傅立葉轉換結果
plt.plot(freq, np.abs(fft))
plt.xlabel('頻率')
plt.ylabel('傅立葉幅度')
plt.show()



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