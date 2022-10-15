def foo(n):
    m = 10
    print("我是m：" + str(m))
    n = n + m
    print("我是n：" + str(n))
    global demo  # 全局变量需要在外面完成初始化的过程
    demo += 4
    print("我是demo：" + str(demo))


def main():
    demo2 = 10
    foo(demo2)
    print("我是demo1:" + str(demo) + ",我是demo2:" + str(demo2))


demo = 60

main()
