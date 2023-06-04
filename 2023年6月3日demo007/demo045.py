# 1: 游乐园的管理员希望你帮助他们了解游客游览游乐园的不同路线以及他们参加的不同游乐项目。
# 在此任务中，他们随机选择了 5 名游客，并希望你分析这些游客的登记序列。
# 现在，他们希望你针对这 5 名游客构造一个距离矩阵。五名游客的编号为：165316、1835254、296394、404385 和 448990。

# SQL语句：===========================================================================================
# select *
# from sequences
# where visitorID in (165316, 1835254, 296394, 404385, 448990);
# SQL语句：===========================================================================================
# 将上面的SQL语句得到的数据，转化为向量矩阵，然后计算向量矩阵的距离矩阵，代码如下：
import pandas
import numpy as np
from scipy.spatial.distance import pdist, squareform

# df = pandas.read_csv('sequences.csv', sep=",")
# df = df[df['visitorID'].isin([165316, 1835254, 296394, 404385, 448990])]
# df = df.sort_values(by=['visitorID', 'sequence'])
# df = df[['visitorID', 'sequence', 'index']]
# df = df.groupby(['visitorID', 'sequence'])['index'].apply(list).reset_index(name='index')
# df['index'] = df['index'].apply(lambda x: np.array(x))
# df = df.groupby(['visitorID'])['index'].apply(list).reset_index(name='index')
# df['index'] = df['index'].apply(lambda x: np.array(x))
# df = df['index'].apply(lambda x: np.array(x))
# df = df.apply(lambda x: np.vstack(x))
# df = df.apply(lambda x: pdist(x, metric='hamming'))
# df = df.apply(lambda x: squareform(x))
# df = df.apply(lambda x: np.sum(x, axis=0))
# print(df)

# 这道题真的不会，向量都不知道怎么表示……


# 2: 游乐园的管理员想要了解每个游乐项目的参加动态（请注意，并非所有景点都是游乐项目）。
# 他们希望看到一张图(例如平行坐标图)上看到每个游乐项目的最小（非零）参入量、一整天的平均参入量以及每个游乐项目的最大参入量。
import pandas
from pandas.plotting import parallel_coordinates
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# from pandas.plotting import mosaic
# 1.在attraction表中找到所有category包含了Rides的数据,将其作为t1表
# 2.根据t1表中的attractionID，计算checkin表中每天每个attractionID的数量
# 3.按照游览项目，将其分类，得到项目的平均访问量，最大访问量，最小访问量
# 4.按照游览项目的平均访问量，最大访问量，最小访问量进行排序
# 5.将排序后的结果输出
# SQL语句：===========================================================================================
# select t1.category, avg(t2.num), max(t2.num), min(t2.num)
# from attraction t1,
#      (select attraction, count(*) as num
#       from checkin
#       group by attraction) t2
# where t1.attractionID = t2.attraction
#   and t1.category like '%Rides%'
# group by t1.category
# order by avg(t2.num) asc, max(t2.num) asc, min(t2.num) asc;
# SQL语句：===========================================================================================
df = pandas.read_csv('demo045table.csv', sep=",")
parallel_coordinates(df, 'Category', colormap=plt.get_cmap("Set2"))
plt.gca().legend_.remove()
plt.show()
# 下面是sql查询结果：
data1 = [
  {
    "Category": "Kiddie Rides",
    "avg(t2.num)": 3841.909090909091,
    "max(t2.num)": 4062,
    "min(t2.num)": 3597
  },
  {
    "Category": "Rides for Everyone",
    "avg(t2.num)": 6998.25,
    "max(t2.num)": 25074,
    "min(t2.num)": 4935
  },
  {
    "Category": "Thrill Rides",
    "avg(t2.num)": 18306.555555555555,
    "max(t2.num)": 27747,
    "min(t2.num)": 14415
  }
]
import json

json_str = json.dumps(data1)
data2 = json.loads(json_str)
print("结果打印：", data2)

# 3: 除了平行坐标图，管理员希望看到描述每个游乐项目的最小、平均和最大参入量的散点图矩阵，如上所述。
df = pandas.read_csv('demo045table2.csv', sep=",")
plt.scatter(df['avg'], df['max'])
plt.show()
# 管理注意事项
# 为了让你的答案可以正确登记在该系统中，你必须将你的答案代码填写在每个问题对应的单元格内。
# 此外，你的作业必须连同该单元格区域显示的代码一同提交。
# 该显示区域应该仅仅包含你为该问题给出的答案，除此之外别无其它信息，要么就是没有正确选择答案。
# 待评分的每个单元格在开头有几行评语。这些行极其重要，不得修改或删除。
