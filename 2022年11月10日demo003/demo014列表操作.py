def main():
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [2, 1, 3, 3, 4, 4]
    print(list1.reverse())  # None
    print(list1)  # [6, 5, 4, 3, 2, 1]
    print(list1.sort())  # None
    print(list1)  # [1, 2, 3, 4, 5, 6]
    print("===================================")
    list1.insert(2, "demo")  # 指定位置插入指定元素， [1, 2, 'demo', 3, 4, 5, 6]
    print(list1)


if __name__ == '__main__':
    main()
