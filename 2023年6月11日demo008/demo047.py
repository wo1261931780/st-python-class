import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('daily-minimum-temperatures-in-me.csv', delimiter=',', skip_header=1)
print(data)
temps = data[:, 1]
mean = np.nanmean(temps)
std = np.nanstd(temps)

plt.plot([0, len(temps)], [mean, mean], 'g-')
plt.plot([0, len(temps)], [mean + std, mean + std], 'y-')
plt.plot([0, len(temps)], [mean - std, mean - std], 'y-')
plt.plot([0, len(temps)], [mean + 2 * std, mean + 2 * std], 'r-')
plt.plot([0, len(temps)], [mean - 2 * std, mean - 2 * std], 'y-')
plt.plot(range(len(temps)), temps, 'b-')
plt.show()

# 绘制曲线：

print("----------------------------")
window_size = 50
plt.plot(np.convolve(temps, np.ones(window_size) / window_size, 'same'))
plt.show()
# 绘制卷积图：
import pandas as pd

df = pd.DataFrame({'temps': temps})
print(df)
df_exp = df.ewm(span=50).mean()
plt.plot(df_exp)
plt.show()
