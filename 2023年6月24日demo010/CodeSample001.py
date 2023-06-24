# 1 部分：树状图
# 代码：

import matplotlib.pyplot as plt

import numpy as np

from scipy.cluster.hierarchy import linkage, dendrogram

import sqlite3

# 这四行导入所需的库。我们需要 matplotlib 库才能在 Jupyter Notebook 环境中显示图表。
# Numpy 用于处理数据。Scipy 库基于 numpy 来提供用于构建和显示树状图的功能。
# 最后，sqlite3 向数据库提供一个操作界面。
# 代码：

db_filename = 'cereals.db'

conn = sqlite3.connect(db_filename)

c = conn.cursor()

# 这三行建立与 sql 数据库的连接，该数据库包含将用于树状图的谷物信息。在此示例中，数据库命名为 cereals.db。
# 在先前的其他示例中，我们偶尔也使用 csv 文件而非数据库来输入资料。
# 代码：

c.execute("SELECT Protein, Fat, Carbohydrates FROM cereals")

results = sum(map(list, list(c.fetchall())), [])

X = np.matrix(results).reshape(-1, 3)

# 这三行负责从数据库收集数据，然后打包成适用于 scipy 的格式。第一行执行查询和收集每种谷物的蛋白质含量、脂肪含量和碳水化合物含量。
# 第二行将数据从 sqlite3 返回的元组格式转换为 numpy 矩阵。第三行将矩阵转换为我们需要的正确的格式。
# 代码：

links = linkage(X, 'centroid')

# 这一行负责计算用于说明树状图和树状图链接的聚类。该功能接受数据 X 和距离度量的说明符，用以计算簇的距离。
# 在此示例中，我们使用“质心”来计算每个簇的质心，然后在合并簇时计算它们之间的距离。
# 代码：

dendrogram(links)

plt.show()

# 最后两行构造树状图的可视化，然后在 Notebook 中显示图表。
# 合矢量图
# 请查看以下附件，以查看结果图。
# 结果图

# 第 2 部分：标准化数据
# 我们之前提到过在执行聚类时将数据标准化的重要性。请务必注意，我们在上一示例中没有将数据标准化。
# 接下来，你将对相同数据进行标准化，然后重新绘制树状图。
# 代码：
from scipy.cluster.vq import whiten

Y = whiten(X)
links = linkage(Y, 'centroid')

# 透过Jupyter Notebook 维持单元格之间核(程序)状态的功能，我们可以直接从上一单元格的运算及果开始。
# 若要将数据标准化，首先从 scipy 中导入“whiten”功能，然后将其应用到转换的数据矩阵。
# 这会将特征值标准化到范围 [0, 1]。最后，使用标准化的特征值重新计算树状图。
# 代码：

dendrogram(links)
plt.show()

# 最后几行再次呈现和显示之前由连接功能计算的树状图。
