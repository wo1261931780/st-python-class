import statistics

data = [11, 321, 2, 12, 1, 21, 312, 3, 453, 4, 354, 321]


def main():
    a = statistics.mean(data)
    print("我是a：" + str(a))
    b = statistics.median(data)
    print("我是b：" + str(b))
    c = statistics.mode(data)
    print("我是c：" + str(c))
    d = statistics.stdev(data)
    print("我是d:" + str(d))
    e = statistics.variance(data)
    print("我是e：" + str(e))


main()
