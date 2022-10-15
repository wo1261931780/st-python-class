data = []
sum = 0
n = 0
with open("demo007.txt") as f:
    data = f.readlines()
    print("我是读取到的数据" + str(data))
    # 这里的是逐行读取，因为后面有s，所以是读取多行数据
    # ['1\n', '1\n', '2\n', '1\n', '31\n', '32\n', '132\n', '1\n', '3']
    for d in data:
        if (d):
            sum = sum + int(d)
            n += 1
            print("当前行的数据：" + str(d))
f.close()
average = sum / n
print("我是平均数据：" + str(average))
