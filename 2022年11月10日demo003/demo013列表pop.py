def main():
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [2, 1, 3, 3, 4, 4]
    # print("list1=" + list1)
    print("list1=", list1)  # list1= [1, 2, 3, 4, 5, 6]
    print("list2=", list2)  # list2= [2, 1, 3, 3, 4, 4]
    print("===================================")
    for element in list1:
        if element == 1:
            # list1.pop()  # 弹出最上面的元素，6被删除
            print(list1.pop())  # 删除的同时，将被删除的元素返回过来，
            # 虽然打印出来，但是删除还是执行的
    for element in list2:
        if element == 1:
            list2.pop(0)  # 弹出指定位置的元素，第一个元素被删除
    print("list1=", list1)  # list1= [1, 2, 3, 4, 5]
    print("list2=", list2)  # list2= [1, 3, 3, 4, 4]


if __name__ == '__main__':
    main()
