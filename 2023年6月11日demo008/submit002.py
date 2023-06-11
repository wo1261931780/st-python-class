# 1：游乐园管理员对数据窗口中游乐项目“Atmosfear”的参入量表示担心。
# 为了减轻他们的压力，他们要求你创建一个此游乐项目总参入量的控制图。
# 使用提供的数据，创建一个控制图，以显示参入量、平均值以及一到两个标准差的标准差带。
# 下面是SQL：
# select count(*) as count,substr(timestamp, 0, 14)
# from checkin
# where attraction = 8
#   and type = 'actual' group by substr(timestamp, 0, 14)
# order by timestamp

import sqlite3
import matplotlib.pyplot as plt
import numpy as np

db_filename = 'dinofunworld.db'

conn = sqlite3.connect(db_filename)

c = conn.cursor()

c.execute(
    "select substr(timestamp, 0, 14) as timestamp, count(*) as count from checkin where attraction = 8  and type = 'actual' group by substr(timestamp, 0, 14) order by timestamp")

counts = c.fetchall()
# print(counts)

import pandas as pd

data = np.genfromtxt('demo048.csv', delimiter=',', skip_header=1)

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

# 2：游乐园的一些管理员在解释“Atmosfear”参入量的控制图时遇到困难，
# 因此他们要求你除了提供在上一个问题中创建的控制图外，还要提供参入量的移动平均图。
# 在此情况下，他们要求你针对移动平均窗口的大小使用 50 个样本。
# 获得移动平均数
window_size = 50
counts = data['count']
plt.plot(np.convolve(temps, np.ones(window_size) / window_size, 'same'))
plt.show()

# 3：为了提供有关图表的选项，游乐园管理员还要求你提供一个包含 50 个样本的移动平均窗口，
# 其中通过相同的“Atmosfear”参入量数据使用指数加权（即指数加权移动平均值）计算平均值。
import pandas as pd
# 将原始数组转换为DataFrame对象
df = pd.DataFrame({'temps': temps})
print(df)
df_exp = df.ewm(span=50).mean()
plt.plot(df_exp)
plt.show()
