import array

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# 第 1 部分：分级统计图
# 这三行导入所需的库以构造分级统计图。
# Pandas 和 geopandas 库将处理数据表示，从而构造图形。
# 顾名思义，geopandas 库依赖于 pandas 库。
# 我们同时也需要 matplotlib 库才能在 Jupyter Notebook 环境中显示图表。

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

world = world[(world.pop_est > 0) & (world.name != "Antarctica")]
print(world)
print(world.head())

world['gdp_per_cap'] = world.gdp_md_est / world.pop_est

# 在这些行中，程序将从 geopandas 库中加载国家及其边界、人口和 GDP 的数据集。
# 第二行将筛选掉估计人口为零的地区和南极洲，以避免在计算步骤（即第三步）中出错。
# 此步骤将计算要绘制的数量，即人均 GDP。


world.plot(column='gdp_per_cap')

plt.show()

# geopandas 库能帮助我们快速轻松地绘制分级统计图。
# 在计算关注的数量后，我们只需要调用plot 函数即可。
# 此函数会使用指定列来确定要绘制的数据值，并产生分级统计图。
# 最后我们使用 matplotlib（而非 geopandas）的显示功能将使图形输出到 Notebook 环境。

# 第 2 部分：比例符号图
# 与分级统计图一样，比例符号图只需要 pandas、geopandas 和 matplotlib 库。
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

world = world[(world.pop_est > 0) & (world.name != "Antarctica")]

# 与分级统计图的操作一样，这两行加载了世界地图。此数据集实例将用作显示比例符号的基础。
# 这是必要的。因为我们使用地理信息，如果没有世界地图作为基础，数据将难以理解。


data = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

data = data[(data.pop_est > 0) & (data.name != 'Antarctica')]

data['centroid_column'] = data.centroid

data['gdp_per_cap'] = data.gdp_md_est / data.pop_est

# 在这些行中，我们将重新输入数据集，以使其与基础层数据分开。
# 最后两行将重复分级统计图中的人均 GDP 计算，并计算每个国家的质心。
# 通过计算质心，我们可以在每个国家的轮廓中心绘制该国家的比例符号。在后续步骤中我们会看到这一点。


centroids = list(data['centroid_column'])

df = pd.DataFrame(
    {'y': [centroids[i].y for i in range(len(centroids))], 'x': [centroids[i].x for i in range(len(centroids))],
     'data': list(data['gdp_per_cap'])})

# 这两行将数据变量中存储的数据转换为适合使用 pandas进行绘图的 pandas 数据框。
# 在上一个函数中计算的质心数据将被存储在坐标数据结构中。
# 该结构对应于最终图表上的 y 和 x。最后，我们计算的人均 GDP 将确定标记的大小。


base = world.plot(color='white', edgecolor='black')

df.plot(kind='scatter', x='x', y='y', s=df['data'] * 1000, ax=base)

plt.show()

# 这三行分别用于绘制世界地图库、绘制符号和在 Notebook 上显示结果。
# 在 geopandas 的轮廓图上绘制 pandas 的散点图能够帮助我们将每个国家的人均 GDP 表示为位于该国家质心上的一个点。
# 散点图中的 s 参数确定每个点的比例。在这里，我们将数据值乘以 1000，以使较贫穷国家的点清晰可见。

# 第 3 部分：莫兰指数
import pysal

import numpy as np

# 这两行导入帮助计算莫兰指数所需的函数库。正如我们将看到的，Python 空间分析 (pysal) 库以易于访问的方式实现我们将使用的分析技术。
# 它还包含我们将在本示例中使用的样本数据。
from libpysal import examples
# usincome_path = examples.get_path('usjoin.csv')
# usincome = gpd.read_file(usincome_path)
# us48_path = examples.get_path('us48.shp')
# us48 = gpd.read_file(us48_path)
import pysal.lib.io as psio

# f = pysal.open(examples.get_path("stl_hom.txt"))
f = psio.open(examples.get_path("stl_hom.txt"))

# y = np.array(f.by_row.by_col['HR8893'])
y = np.array(f.by_row()['HR8893'])

w = psio.open(examples.get_path('stl.gal')).read()

# 这三行导入密苏里州圣路易斯的不同地区的凶杀率。第一行导入原始数据集，而第二行选择要分析的数据的特定列。
# 第三行导入使用 Rook 连续性计算的连续性矩阵。


# mi = pysal.Moran(y, w, two_tailed=False)
# print(mi.I)
from esda.moran import Moran
from libpysal.weights.contiguity import Queen

gdf = gpd.read_file(f)
# w = Queen.from_dataframe(gdf)
moran = Moran(y, w)
print(moran.I)
# 这两行计算和报告在上一个步骤中加载的数据的莫兰指数。
# 莫兰数据结构包含更多信息，而不仅仅是可能对空间分析有用的最终 I 计算。
# 您可在 pysal 文档中找到有关 pysal 的结构和其他特征的完整信息。
