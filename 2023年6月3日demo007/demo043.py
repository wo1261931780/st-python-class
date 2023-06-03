# 模块 3 编程作业 Jupyter Notebook 演示1：机器学习 Module 3: Jupyter Notebook Example: Machine Learning
# 第1部分：K均值
# 代码：
import numpy
import scipy
import sklearn
from sklearn.datasets import load_wine
from scipy.cluster.vq import kmeans2, whiten

# 此语句序列使用K均值为聚类导入必要的库。
# Numpy 库不直接使用，但由其他库使用，以比基本 Python 更好地处理矩阵。
# Load_wine 函数包含葡萄酒及其特征的数据集，用于演示机器学习技术。

# 代码:
[data, target] = load_wine(return_X_y=True)

whitened = whiten(data)

# 这两行加载葡萄酒数据集并执行白化或特征方面的标准化。
# 传递到 load函数的参数导致它分别返回特征矩阵和类标签。
# 需要对数据进行白化，因为k均值认为所有特征在数值上是相等的，
# 因此在不进行白化的情况下，范围为 1000 - 9000 的特征将比范围为 1 - 9 的特征具有更大的权重。
# 代码:
start = [whitened[0], whitened[int(len(whitened) / 2)], whitened[len(whitened) - 1]]
[centroid, label] = kmeans2(whitened, start)

# 这三行确定三个簇的起始质心并执行聚类。在不定义起始质心的情况下，k 均值算法将选择随机质心，这将导致不可预测的行为和不一致的聚类。

# 代码：
errors = 0.0
for i in range(len(label)):
    if target[i] != label[i]: errors += 1

acc = (len(data) - errors) / len(data)

print(acc)

# 这些行评估和报告聚类的准确性。在这种情况下，我们只计入分配到不同于其真实标签的簇的数据实例。
# 这是一个简单示例，对于更复杂的数据集，需要对聚类可靠性进行更复杂的评估。

# 第 2 部分：决策树
# 代码：
import numpy
import scipy
from sklearn.datasets import load_wine
from sklearn import tree

# 这几行的函数与在 k 均值示例中相同。在此处，决策树函数 tree 是 sklearn 或 Scikit Learn 库的一部分，与来自 scipy 的 k 均值相反。

# 代码：
[data, target] = load_wine(return_X_y=True)

# 同样，加载数据集作为单独的特征值和真实类标签。由于决策树单独考虑每个特征，因此在此情况下，没有必要对特征矩阵进行白化。

# 代码：
data_train = data[0:len(data) - 2]

target_train = target[0:len(data) - 2]

# 为了演示决策树的有效性，我们使用留一法交叉验证创建培训集。
# 在这种情况下，留下数据的最后一个数据实例。

# 代码
dtc = tree.DecisionTreeClassifier()

dtc = dtc.fit(data_train, target_train)

print(dtc.predict(data[len(data) - 1].reshape(1, -1)))

# 最后三行使用培训数据集初始化、培训和测试决策树。最后一行是测试步骤，还报告了决策树的预测。
# 如果我们确实执行留一法交叉验证，将随机选择留下许多样本，针对留下的每个样本培训新的树，累积所有样本的测试结果。

# 第 3 部分：支持向量机(SVM)
# 代码：
import numpy
import scipy
from sklearn.datasets import load_wine
from sklearn import svm

# 这几行的函数与在k均值示例中相同。
# 在此处，支持向量机函数svm是sklearn或ScikitLearn库的一部分，与来自scipy的k均值相反。


# 代码：
[data, target] = load_wine(return_X_y=True)

data_train = data[0:len(data) - 2]
target_train = target[0:len(target) - 2]

# 同样，数据集将加载为特征和标签，并划分为培训和测试集。与决策树一样，SVM 通常不需要数据白化。


# 代码
clf = svm.LinearSVC()

clf.fit(data_train, target_train)

print(clf.predict(data[len(data) - 1].reshape(1, -1)))

# 同样，我们初始化、培训和测试 SVM 分类器。
# 在这两个示例中，决策树和 SVM 分类器都将正确预测最后一个样本的类。
# 能否找到一个或两个分类器没有正确预测的样本？
