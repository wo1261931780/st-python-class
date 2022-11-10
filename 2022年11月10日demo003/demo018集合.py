def main():
    set1 = {1, 2, 3, 4, "demo1", "demo2"}
    set2 = {1, 2, 2, 3.1, 4.5, "demo3", "demo4"}
    set3 = {3.3, "demo5", 2, "demo6"}
    if set1 == set2 and set2 == set3:
        print("equal")
    else:
        print("error")

    print(set1)  # {'demo2', 1, 2, 3, 4, 'demo1'}
    print(set2)  # {1, 2, 3.1, 4.5, 'demo3', 'demo4'}
    # 首先，集合中自动去除重复元素
    # 其次，集合中的元素会自动排序，按照数字从小到大
    # 集合中的元素还可以混合存在
    for x in set3:
        print(x, end=",")  # 2,3.3,demo5,demo6,
    print("\n")
    print(set1)


if __name__ == '__main__':
    main()
