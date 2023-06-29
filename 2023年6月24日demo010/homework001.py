# 作业
# 此任务仅包含一个问题，要求您生成树状图。
# 使用 ID 为 165316、1835254、296394、404385 和 448990 的访客轨迹（全部三天数据）创建此树状图。
# 对这些轨迹执行聚类来生成树状图时，使用聚类中所有点的平均距离。


import matplotlib.pyplot as plt

import numpy as np

from scipy.cluster.hierarchy import linkage, dendrogram

import sqlite3

db_filename = 'dinofunworld.db'  # 这是新的数据库文件

conn = sqlite3.connect(db_filename)

c = conn.cursor()
# 在课堂给出的数据库文件中进行了查询：
# select *
# from sequences where id in (165316, 1835254, 296394, 404385, 448990);
# 得到的结果是：五行指定的id，和对应的参观序列
# 然后将得到的数据进行保存操作，得到了demo.csv
# 为了方便我们在代码中进行处理，
# 我们将demo.csv文件中的数据进行了保存，新建result数据库，保存参观序列
c.execute("SELECT visit165316,visit1835254,visit296394,visit404385,visit448990 from result")  # 这是新的数据库文件

results = sum(map(list, list(c.fetchall())), [])  # 将查询结果转换为列表
X = np.matrix(results).reshape(-1, 3)  # 将列表转换为矩阵
links = linkage(X, 'centroid')  # 使用聚类中所有点的平均距离
dendrogram(links)  # 生成树状图
plt.show()  # 显示树状图

from scipy.cluster.vq import whiten

Y = whiten(X)  # 使用whiten函数对数据进行预处理
links = linkage(Y, 'centroid')  # 使用聚类中所有点的平均距离
dendrogram(links)  # 生成树状图
plt.show()  # 显示树状图
