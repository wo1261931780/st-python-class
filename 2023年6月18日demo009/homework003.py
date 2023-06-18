# 数据与提示
# Pysal包里的样例数据包括美国本土的 48 个州，您可以通过以下方式加载数据：
# 除了逐个州的数据外，数据集还包含每个州的形状文件，可用于创建分区统计和比例符号地图，您可以通过以下方式加载：
# 使用提供的数据，执行作业要求分析并创建所需的地图。
# 作业
# 1：使用 PySal 数据，创建美国的分区统计图，描述 2009 年美国每个州的人均收入。
# 你只需绘制本土48州的地块。你需要在图中显示清晰的纬度和经度。下面是代码：
import pysal as ps
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from libpysal import examples

usincome_path = examples.get_path('usjoin.csv')  # 获取数据路径
usincome = gpd.read_file(usincome_path)  # 读取数据
us48_path = examples.get_path('us48.shp')  # 获取数据路径
us48 = gpd.read_file(us48_path)  # 读取数据
us48.plot()  # 绘图
plt.show()  # 显示图像
# 2：再次使用 PySal，创建一个比例符号地图，
# 要求在美国每个州的质心处显示一个点，该点的大小需要按该州2009年的人均收入按比例缩放，收入越高点的面积越大。
# 处理的数据保留整数，不要保留小数。你需要在图中显示清晰的纬度和经度。下面是参考代码：

data = gpd.read_file(us48_path)  # 读取数据
data['centroid_column'] = data.centroid  # 计算质心
data = data.set_geometry('centroid_column')  # 设置质心
data['gdp_per_cap'] = data.AREA / data.PERIMETER
data.plot()  # 绘图
plt.show()  # 只有质心，没有点的大小,仅做测试

centroids = list(data['centroid_column'])  # 计算质心

df = pd.DataFrame(
    {'y': [centroids[i].y for i in range(len(centroids))],
     'x': [centroids[i].x for i in range(len(centroids))],
     'data': list(data['gdp_per_cap'])})  # 创建数据框

base = data.plot(color='white', edgecolor='black')  # 绘图，白色背景，黑色边框

df.plot(kind='scatter', x='x', y='y', s=df['data'] * 300, ax=base)  # 绘制散点图，点的大小按照数据框中的数据进行缩放
# 这里手动调整了点的放缩比例，否则点太小看不清

plt.show()  # 显示图像

import numpy as np
import pysal.lib.io as psio

f = psio.open(examples.get_path("stl_hom.txt"))  # 获取数据路径
y = np.array(f.by_row()['HR8893'])  # 读取数据
w = psio.open(examples.get_path('stl.gal')).read()  # 读取数据
from esda.moran import Moran

gdf = gpd.read_file(f)  # 读取数据
# 考虑pysal的版本问题
# 这里使用的是Queen邻接矩阵，也可以使用其他的邻接矩阵，比如Rook邻接矩阵
moran = Moran(y, w)  # 计算莫兰指数
print(moran.I)  # 打印莫兰指数
