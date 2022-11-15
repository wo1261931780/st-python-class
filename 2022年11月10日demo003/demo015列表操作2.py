def main():
    demo_list = [1, 2, 3, "demo", 5]  # python的列表可以数字/字符串混用
    print("列表长度：", len(demo_list))
    demo_list.append("nextStr")  # 直接插入，默认就在最后，堆栈的内存逻辑
    print(demo_list)  # [1, 2, 3, 'demo', 5, 'nextStr']
    print("===================================")

    demo_list.insert(2, "two")  # 在指定位置插入数据
    print(demo_list)  # [1, 2, 'two', 3, 'demo', 5, 'nextStr']
    print("===================================")

    demo_list.insert(2, "demo")
    print(demo_list.count("demo"))  # 2,python可以直接计算字符串出现次数
    # 这里的字符串是完全匹配，有任何出入都不符合
    print("===================================")
    list_copy = demo_list.copy()
    print(list_copy)  # [1, 2, 'demo', 'two', 3, 'demo', 5, 'nextStr']
    # 相当于完全拷贝了列表的所有数据和元素顺序

    print("===================================")
    list_copy.extend(["demo1", "demo2"])
    print(list_copy)  # [1, 2, 'demo', 'two', 3, 'demo', 5, 'nextStr', 'demo1', 'demo2']


if __name__ == '__main__':
    main()
