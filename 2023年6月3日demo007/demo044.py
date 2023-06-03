# 模块 3 编程作业 Jyputer Notebook 演示2： 高级图形 Module 3: Jupyter Notebook Example 2: Advanced Graphic
# 第 1 部分：马赛克图
# 代码：

import pandas

import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

from statsmodels.graphics.mosaicplot import mosaic

# 这三行导入构造和显示马赛克图所需的程序库。请注意，statsmodels库具有内置的马赛克绘制功能。
# 由于大多数类型的图表已在Python中实现，因此大多时后我们不需要从头开始构建自己的图形功能。
# 代码：
df = pandas.read_csv('cereals_conf.csv', sep=",")

# 此行读取我们在预生成的文件中提供的数据。此文件将每种谷物的脂肪和蛋白质水平分为高和低类别。
# 因为马赛克图将特征的每个不同值视为一种类别，缩减数据集到高和低这两种类别可确保图表易于阅读。


# 代码：
mosaic(df, ['Fat', 'Protein'])

plt.show()

# 这两行分别绘制和显示图表。马赛克函数调用的第二个参数确定应绘制哪些数据列，以及应按何种顺序绘制他们。
# 在此处，因为脂肪和蛋白质列是数据集中仅有的两列，我们该顺序使用它们。

# 第2部分：平行坐标图代码：
import pandas

import matplotlib.pyplot as plt

# from pandas.plotting import mosaic

# 这三行代码的目的与用于马赛克图时的目的相同。需要注意的是，平行坐标图功能是内置在pandas库中，而不是statsmodels库中。
# 代码：
df = pandas.read_csv('cereals_num.csv', sep=",")

# 我们同样从文件中加载与绘制马赛克图时类似的数据集。
# 在这个数据集中，我们已将谷物数据筛选并缩减为三种特征：蛋白质、脂肪和碳水化合物，以便最大程度地让绘图的结果容易阅读。
# 假使我们使用超过这三种特征，将会导致图表拥挤且难以阅读。

# 代码：
# parallel_coordinates(data, 'Cereal')

# plt.gca().legend_.remove()

# plt.show()

# 同样，图形在第一行中被绘制，并在最后一行中显示在Notebook中。
# 第二行代码会删除图形中的图例，因为在这个示例中显示所有谷物类型的图例没有太大意义。
# 在此示例中，绘图的目的是显示谷物成分的整体趋势。
# 不过对于平行坐标图来说，省略图例并不是必要的。假使我们只有少量数据实例需要绘制，图例可能会很有用。

# 第3部分：像素图
# 代码：
import numpy as np

# import matplotlib.pyplot as plt

import matplotlib.cm as cm

# 与其他两个图表一样，我们导入程序库以帮助绘制图形。在这里，色图指示图cm用于指定配色方案。
# 此外，我们还使用numpy（而不是pandas）来处理数据。
# 代码：
inData = np.loadtxt('cereals_normed.csv', delimiter=',', dtype=float, skiprows=1)

tData = inData.transpose()

# 和前面的示例一样，第一行代码加载数据。
# 与前面不同的是，此行将数据加载到numpy矩阵中，而不是pandas数据框中。
# 第二行转置数据，以便矩阵按列而非按行排列。
# 代码：
plt.imshow(tData, interpolation='nearest', cmap=cm.inferno)

plt.axis('off')

plt.show()

# 这些代码绘制和显示像素图。
# Matplotlib的imshow函数将之前加载的矩阵视为像素值的矩阵。
# Cmap参数指定要用于绘制数据的配色方案。
# 在此处，为了使图表容易阅读，我们关闭了图表的轴。


# 第4部分：散点图
# 代码：
import pandas

import matplotlib.pyplot as plt

# 和前面的示例相同，在此导入构造图表所需的程序库。在这里，散点图内置在pandas库中，因此无需导入其他程序库。
# 代码：
df = pandas.read_csv('cereals_num.csv', sep=",")

# 此行导入与在平行坐标图中使用的相同的数据文件。虽然此数据集包含三种特征，散点图通常只能够绘制两种特征。稍后我们将选择这些特征。
# 代码：
plt.scatter(df['Fat'], df['Protein'])

plt.show()

# 最后几行绘制和显示图表。在scatter程序的调用中指定数据集的脂肪列为X值，蛋白质列为Y值。
# 第5部分：WordCloud / Wordle
# 代码：
from wordcloud import WordCloud

import matplotlib.pyplot as plt

# 和前面一样，这些行导入所需的库。因为Wordless使用文本数据而不是数值数据，因此pandas库在此处没有用处。
# 另一方面，wordcloud库包含成功绘制Wordle所需的许多功能。
# 代码：
text = open('kjb.txt').read()

# 此行阅读在线免费提供的钦定版《圣经》的文本。钦定版《圣经》通常用作文本分析技术的样本文本。
# 代码：
wordcloud = WordCloud(background_color='white')

wordcloud.generate(text)
# 在此处，我们初始化并生成Wordle / WordCloud。
# 因为JupyterNotebook背景为白色，因此我们将背景颜色显式设置为白色，否则Wordle将显示在黑色背景上。
# 代码：
plt.imshow(wordcloud, interpolation='bilinear')

plt.axis('off')

plt.show()

# 同样，我们使用imshow函数显示wordle图像。
# 因为imshow函数将wordle视为矩阵，因此我们必须显式关闭图表的轴，并指示matplotlib使用插值相应地缩放图像。
