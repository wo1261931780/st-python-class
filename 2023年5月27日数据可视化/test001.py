# 代码:
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

db_filename = 'dinofunworld-1.db'

conn = sqlite3.connect(db_filename)

c = conn.cursor()

# 上面的代码为公共代码
# 图表 1：描绘游览惊险飞车（thrill ride）景点的饼图。
# 先筛选attraction表中category为thrill rides的数据，然后按照attraction_id分组，
# 就可以得到所有的景点AttractionId
# 然后筛选checkin中的数据，获得所有游客的VisitorID
# 查询游客Attraction数据，获得所有景点的访问量
# 最后将数据转换为饼图的格式
# 最后绘制饼图
# SQL语句：===========================================================================================
# select attraction, count(*) as count
# from checkin
# where attraction in (select AttractionID
#                      from attraction
#                      where category LIKE '%Thrill%')
#   and visitorID in (select distinct visitorID
#                     from checkin
#                     where attraction in (select AttractionID
#                                          from attraction
#                                          where category LIKE '%Thrill%')
#                     group by visitorID
#                     having count(*) >= 2)
# group by attraction
# order by count desc;
# SQL语句：===========================================================================================
# limit 10;
# 代码：
c.execute(
    "select attraction, count(*) as count from checkin where attraction in (select AttractionID from attraction where category LIKE '%Thrill%') and visitorID in (select distinct visitorID from checkin where attraction in (select AttractionID from attraction where category LIKE '%Thrill%') group by visitorID having count(*) >= 2) group by attraction order by count desc")

counts = c.fetchall()

# 第3部分：图表
# 代码:
tableResult1 = pd.DataFrame.from_records(counts, columns=['AttractionID', 'count'])
# print(tableResult1)
AttractionID = list(tableResult1['AttractionID'])
# print(AttractionID)
count = list(tableResult1['count'])
# print(count)
dataDemo = count
plt.pie(dataDemo, explode=None, labels=AttractionID,
        autopct='%1.1f%%',
        shadow=False, startangle=90)

plt.axis('equal')

plt.show()

# 图表 2：描绘美食摊位（food stall）总访问量的柱状图(包含所有数据，无论是否为actual)。
# 查询Attraction表中category为food的数据，获得所有的景点AttractionID
# 然后筛选checkin中的数据，获得所有游客的VisitorID
# 查询游客Attraction数据，获得所有景点的访问量
# 最后绘制柱状图
# SQL语句：===========================================================================================
# select attraction, count(*) as count
# from checkin
# where attraction in (select AttractionID
#                      from attraction
#                      where category LIKE '%Food%')
#   and visitorID in (select distinct visitorID
#                     from checkin
#                     where attraction in (select AttractionID
#                                          from attraction
#                                          where category LIKE '%Food%')
#                     group by visitorID
#                     having count(*) >= 2)
# group by attraction
# order by count desc;
# SQL语句：===========================================================================================
# 代码:
c.execute(
    "select attraction, count(*) as count from checkin where attraction in (select AttractionID from attraction where category LIKE '%Food%')  and visitorID in (select distinct visitorID from checkin where attraction in (select AttractionID from attraction where category LIKE '%Food%')                     group by visitorID having count(*) >= 2) group by attraction order by count desc")

tableResult2 = c.fetchall()
tableResult2Frame = pd.DataFrame.from_records(tableResult2, columns=['attraction', 'count'])
tableResult2Label = list(tableResult2Frame['count'])
# plt.hist(tableResult2Frame['attraction'],bins=12, label=tableResult2Label)
print(tableResult2)
plt.hist(
    tableResult2Frame['attraction'],  # 指定要绘制直方图的数据
    bins=12,  # 设置长条形的数目
    # range,# 指定直方图数据的上下界，默认包含绘图数据的最大值和最小值（范围）
    # density=True or False, # 如果"True"，将y轴转化为密度刻度 默认为None
    # weights,# 该参数可为每一个数据点设置权重
    # cumulative=True or False,# 是否需要计算累计频数或频率 默认值False
    bottom=0,  # 可以为直方图的每个条形添加基准线，默认为0
    # histtype={'bar', 'barstacked', 'step', 'stepfilled'} # 设置样式
    # bar柱状形数据并排，默认值。
    # barstacked在柱状形数据重叠并排（相同的在一起）
    # step柱状形颜色不填充
    # stepfilled填充的线性
    # align='mid' or 'left' or 'right', # 设置条形边界值的对其方式，默认为mid，除此还有’left’和’right’
    # orientation={'vertical', 'horizontal'},# 设置直方图的摆放方向，默认为垂直方向vertical
    rwidth=0.3,  # 设置直方图条形宽度的百分比
    # log=True or False,# 是否需要对绘图数据进行log变换 默认值False
    # color='r',# 设置直方图的填充色
    label=tableResult2Frame['attraction']  # 设置直方图的标签
    # stacked=True or False, # 当有多个数据时，是否需要将直方图呈堆叠摆放，默认False水平摆放；
    # facecolor,# 设置长条形颜色(和color效果一致，设置color就不用再设置facecolor)
    # edgecolor,# 设置边框的颜色
    # alpha # 设置透明度
)
# 注意组距，得到满意的展示效果
# 注意y轴所代表的变量是频数还是频率
plt.show()

# 图表 3：描绘一天之中参加最新游乐项目 Atmosfear 的折线图。
# 查询Attraction表中name为Atmosfear的数据，获得所有的景点AttractionID
# 然后筛选checkin中的数据，获得所有游客的VisitorID
# 查询游客Attraction数据，获得所有景点的访问量
# 最后绘制折线图
# SQL语句：===========================================================================================
# select substr(timestamp, 1, 13) as hour, count(*) as count
# from checkin
# where attraction = 8
# group by hour
# order by hour;
# SQL语句：===========================================================================================

# 代码:
c.execute(
    "select substr(timestamp, 6, 8) as hour, count(*) as count from checkin where attraction = 8 group by hour order by hour")

tableResult3 = c.fetchall()
tableResult3Frame = pd.DataFrame.from_records(tableResult3, columns=['hour', 'count'])
app = list(tableResult3Frame['count'])
tableResult3Count = list(tableResult3Frame['count'])
# print(tableResult3Count)
tableResult3Label = list(tableResult3Frame['hour'])
dataXslim = np.arange(0, 44)
fig = plt.figure(num=1, figsize=(6, 4))

ax = fig.add_subplot(111)
ax.plot(dataXslim, app)

ax.set_xlim([0, 44])
ax.set_ylim([0, 1500])

ax.set_xticklabels(tableResult3Label, fontsize=7, rotation=10)
plt.show()

# 图表 4：描绘游乐场的儿童碰碰车（Kiddie Rides）总游览量的箱线图。
# 查询Attraction表中category为Kiddie Rides的数据，获得所有的景点AttractionID
# 然后筛选checkin中的数据，获得所有游客的VisitorID
# 查询游客Attraction数据，获得所有景点的访问量
# 最后绘制箱线图
# 将上面的数据作为数据来源,绘制箱线图
# 计算上四分位数Q3，下四分位数Q1，中位数Q2，最大值Max，最小值Min
# 计算内限，内限 = Q3 - Q1
# 计算外限，外限 = Q3 + 1.5 * 内限
# 最终箱线图的上边缘为Q3，下边缘为Q1，中间的线为Q2，上边缘到外限之间的线为上边缘的盒须，下边缘到外限之间的线为下边缘的盒须
# SQL语句：===========================================================================================
# select max(count) as Max,
#        min(count) as Min,
#        avg(count) as Avg,
#        median(count)                                             as Median,
#        max(count) - min(count)                                   as IQR,
#        max(count) - min(count) + 1.5 * (max(count) - min(count)) as Outlier
# from (select attraction, count(*) as count
#       from checkin
#       where attraction in (select AttractionID
#                            from attraction
#                            where category LIKE '%Kiddie Rides%')
#         and visitorID in (select distinct visitorID
#                           from checkin
#                           where attraction in (select AttractionID
#                                                from attraction
#                                                where category LIKE '%Kiddie Rides%')
#                           group by visitorID
#                           having count(*) >= 2)
#       group by attraction
#       order by count desc) as demo;
# SQL语句：===========================================================================================
c.execute(
    "select attraction, count(*) as count from checkin where attraction in (select AttractionID from attraction where category LIKE '%Kiddie Rides%') and visitorID in (select distinct visitorID from checkin where attraction in (select AttractionID from attraction  where category LIKE '%Kiddie Rides%') group by visitorID  having count(*) >= 2) group by attraction order by count desc")

tableResult4 = c.fetchall()
tableResult4Frame = pd.DataFrame.from_records(tableResult4, columns=['attraction', 'count'])
# 代码:
plt.boxplot(tableResult4Frame['count'])

plt.show()
