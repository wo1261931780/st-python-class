def main():
    demo = dict()
    demo = {"demo1": 111, "demo2": 222, "demo4": 444, "demo3": 333}
    print(demo)  # 不会按照key排序
    print(demo["demo2"])  # 222
    print(demo.get("demo"))  # None,
    # 推荐使用下面这种get方式根据key获取value
    # 在key输入错误的时候不会报错


if __name__ == '__main__':
    main()
