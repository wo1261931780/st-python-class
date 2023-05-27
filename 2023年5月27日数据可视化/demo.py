import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

from pandas._libs.reshape import explode

# 找到数据库文件的路径

# 这里是测试课堂代码

db_filename = 'cereals.db'
# print("数据库打开成功")
connect = sqlite3.connect(db_filename)
cursor = connect.cursor()

conn = sqlite3.connect(db_filename)

c = conn.cursor()

# 此代码块包括其余示例所需的库。在此示例中，我们需要将用于绘图的 sqlite3 和 pandas 库以及部分 matplotlib库。
# 此外，我们加载数据库并创建游标，以便可以提取要绘图的数据。
# 第2部分：图表
# 代码：
c.execute("SELECT Manufacturer, count(*) FROM cereals GROUP BY Manufacturer")

counts = c.fetchall()
print(counts)
# 此单元格将生成并显示一个用于按制造商来表示麦片的分布的饼图。这两行通过要求数据库计入每个制造商的数据来绘制数据。
# 第3部分：图表
# 代码:
manuStats = pd.DataFrame.from_records(counts, columns=['manufacturer', 'value'])

print(manuStats)
manufacturer = list(manuStats['manufacturer'])
print(manufacturer)
labels = list(manuStats['value'])
print(labels)
dataDemo = labels
plt.pie(dataDemo, explode=None, labels=manufacturer,
        autopct='%1.1f%%',
        shadow=False, startangle=90)
#
plt.axis('equal')
plt.show()
