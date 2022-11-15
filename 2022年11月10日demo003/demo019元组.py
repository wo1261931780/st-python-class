def main():
    tup1 = (0, 1, 12, 3, 4, 5, 6)
    print(tup1)
    print(tup1[0], "元组0号元素")
    print(tup1[2], "元组3号元素")
    print(tup1[:-3])  # (0, 1, 12, 3)
    # 上面就是从0号元素到索引为3的所有元素
    print(tup1[5:])  # (5, 6)
    # 从5号索引到最后
    tup2 = ("a1", "a2", "a3", "a4", "a5", "a6")
    tup3 = (1, 2, 3, 4, "demo5", 6)


if __name__ == '__main__':
    main()
