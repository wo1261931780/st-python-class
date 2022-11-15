def main():
    dictionary = dict()
    dictionary["demo1"] = [11, 12, 13]
    dictionary["demo2"] = [21, 22, 23]
    dictionary["demo3"] = [31, 32, 33]
    dictionary["demo4"] = [41, 42, 43]
    demo_list = ["demo1", "demo2", "demo3", "demo4"]
    for city in demo_list:
        if city in dictionary:
            print(city, "-----", dictionary[city])
        else:
            print(city, "is not in dictionary")

    city_name = input("请输入城市名称：")
    # print(city_name)
    signal_demo = False
    for city2 in demo_list:
        if city_name == city2:
            signal_demo = True

    print(f"find name : {city_name}" if signal_demo == True else "find nothing")
    # 上面是python中的三元运算符，表达方式比较low


if __name__ == '__main__':
    main()
