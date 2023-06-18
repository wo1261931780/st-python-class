# 数据与提示
# Pysal包里的样例数据包括美国本土的 48 个州，您可以通过以下方式加载数据：

# 除了逐个州的数据外，数据集还包含每个州的形状文件，可用于创建分区统计和比例符号地图，您可以通过以下方式加载：

# 使用提供的数据，执行作业要求分析并创建所需的地图。
#
# 作业
# 1：使用 PySal 数据，创建美国的分区统计图，描述 2009 年美国每个州的人均收入。
# 你只需绘制本土48州的地块。你需要在图中显示清晰的纬度和经度。下面是代码：
import pysal as ps
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

world = world[(world.pop_est > 0) & (world.name == "United States of America")]
# print(world)
print(world.head())

world['gdp_per_cap'] = world.gdp_md_est / world.pop_est

world.plot(column='gdp_per_cap')

plt.show()
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

world = world[(world.pop_est > 0) & (world.name == "United States of America")]
data = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

data = data[(data.pop_est > 0) & (data.name == 'United States of America')]

data['centroid_column'] = data.centroid

data['gdp_per_cap'] = data.gdp_md_est / data.pop_est

centroids = list(data['centroid_column'])

df = pd.DataFrame(
    {'y': [centroids[i].y for i in range(len(centroids))], 'x': [centroids[i].x for i in range(len(centroids))],
     'data': list(data['gdp_per_cap'])})

base = world.plot(color='white', edgecolor='black')

df.plot(kind='scatter', x='x', y='y', s=df['data'] * 1000, ax=base)

plt.show()

# 注意：PySal 和 GeoPandas 库都包含一些实用的函数，可以使此任务更容易。
#
# 2：再次使用 PySal 数据，创建一个比例符号地图，在美国每个州的质心处显示一个点，该点的大小需要按该州2009的人均收入按比例缩放，收入越高点的面积越大。
#
# 你只需绘制本土48州的地块。你需要在图中显示清晰的纬度和经度。
#
# 注意：本单元的演示笔记本包含执行类似任务的代码，可能是作业的有用参考。
#
# 3：使用相同的数据，使用 Rook Continuity计算 2009 年美国每个州人均收入的Moran's I 的值。
# 该值需要四舍五入到小数点后 4 位（即 X.xxxx）
#
# 此问题只需要返回一个值。
#
# 注意：同样，PySal 和 GeoPandas 库包含实用的函数来帮助你计算本题。
#
# 管理注意事项
# 为了让你的答案可以正确登记在该系统中，你必须将你的答案代码填写在每个问题对应的代码单元格内。
# 此外，你的作业必须连同该单元格区域显示的代码一同提交。该显示区域应该仅仅包含你为该问题给出的答案，除此之外别无其它信息，要么就是没有正确选择答案。
# 待评分的每个单元格在开头有几行评语。这些行极其重要，不得修改或删除。
