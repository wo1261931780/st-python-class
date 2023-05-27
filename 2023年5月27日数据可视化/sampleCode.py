# 图表
# 此示例中生成的四个图表如下：
# 饼图 条形图 直方图 箱形图 单元格
# 在此示例提供的Notebook中，生成每个图表的代码在自己的单元格中。这允许你一次生成一个图表，并在不影响其他图表的情况下修改一个图表的代码。
# 为了设置绘图环境，每次打开Notebook并尝试运行任何图表代码之前，必须运行第一个单元格中的代码。
# 第1部分：
# 代码:
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os


# 找到数据库文件的路径

db_filename = 'cereals.db'
# print("数据库打开成功")
conn = sqlite3.connect(db_filename)

c = conn.cursor()

# 此代码块包括其余示例所需的库。在此示例中，我们需要将用于绘图的 sqlite3 和 pandas 库以及部分 matplotlib库。
# 此外，我们加载数据库并创建游标，以便可以提取要绘图的数据。
# 第2部分：图表
# 代码：
c.execute("SELECT Manufacturer, count(*) FROM cereals GROUP BY Manufacturer")

counts = c.fetchall()

# 此单元格将生成并显示一个用于按制造商来表示麦片的分布的饼图。这两行通过要求数据库计入每个制造商的数据来绘制数据。
# 第3部分：图表
# 代码:
manuStats = pd.DataFrame.from_records(counts, columns=['manufacturer', 'value'])

# 在此行中，要用于绘制的数据是从数据库返回的记录，并将其转换为DataFrame。此伪表格格式由bokeh绘图函数使用。
# 使用from_records()可以轻松从数据库记录中构造此格式。
# 第4 部分：图表
# 代码:
# plt.pie(manuStats['value'], labels='manufacturer', shadow=False)
print(manuStats)
manufacturer = list(manuStats['manufacturer'])
print(manufacturer)
labels = list(manuStats['value'])
print(labels)
dataDemo = labels
plt.pie(dataDemo, explode=None, labels=manufacturer,
        autopct='%1.1f%%',
        shadow=False, startangle=90)

plt.axis('equal')

plt.show()

# 第一行的代码用于创建图表。从之前创建的DataFrame中指定“值”列，可表明要用于绘制的数据列。类似地，“标签”列可将标签应用到饼图的每个部分。
# 最后，plt.show()函数在 Notebook 中呈现该图表。
# 第 5 部分：图表
# 代码:
c.execute("SELECT Cereal,Sugars FROM cereals")

sugars = c.fetchall()

sugarFrame = pd.DataFrame.from_records(sugars, columns=['Cereal', 'Sugar'])

# 此单元格将生成一个条形图，用于显示每种麦片的含糖量。
# 这几行代码从数据库中查询糖的含量与麦片名称相应的配对，并格式化数据以显示在bokeh# 图表中。
# 第6部分：图表
# 代码:
plt.bar(range(len(sugarFrame['Sugar'])), sugarFrame['Sugar'])

plt.xticks([])

plt.show()

# 这两行代码还是创建图表，然后在Notebook中进行呈现。
# 在这种情况下，该图表是一个条形图，用于显示每种命名麦片的“糖”字段的值。
# 第7部分：图表
# 代码:
c.execute("SELECT Sugars FROM cereals")

sugar = c.fetchall()
print(sugar)
sugarFrame = pd.DataFrame.from_records(sugar, columns=['Sugar'])

# 此单元格将生成一个直方图，用于显示数据集中数据的含糖量的分布。
# 在这种情况下，我们仅需要每个记录中的糖值，因此我们的查询仅请求这些值。
# 如上所述，最后一行格式化数据，以用bokeh。
# 第8部分：图表
# 代码:
plt.hist(sugarFrame['Sugar'], bins=9)

plt.show()

# 在此处，我们将生成包含实际糖值的直方图。Bokeh包的内置直方图可以执行所有直方图计算。
# 但在此处，我们指定bin的数量以符合 √N规则。最后一行代码在Notebook中呈现图形。
# 第9部分：图表
# 代码:
c.execute("SELECT Manufacturer, Sugars FROM cereals ")

sugarByMan = c.fetchall()

sugarBoxFrame = pd.DataFrame.from_records(sugarByMan, columns=['Manufacturer', 'Sugar'])

# 此单元格生成一个按制造商分类的含糖量的箱形图。
# 在这种情况下，我们需要数据集中所有糖含量的列表，并加上制造商标签，因此每个记录都要求具有这两项。
# 再次重复，第三行代码为bokeh重新格式化数据。
# 第10部分：图表
# 代码:
plt.boxplot(sugarFrame['Sugar'])

plt.show()

# 在此处，我们使用bokeh的内置BoxPlot函数。
# 为了使函数提供准确的结果，我们必须表明用于按制造商对糖进行分组的数据特征。
# 然后，该函数将计算分位数。最后一行代码在Notebook中呈现该图。
