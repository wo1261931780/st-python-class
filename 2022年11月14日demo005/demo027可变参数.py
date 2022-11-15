# def print_info(num1, num2, num3=0, num4):
# 如果上面num3给了默认值，但是num4没有
# 就会直接报错
def print_multiple(*num):
    # python支持通配符，实际上是默认num为可变长度的元祖
    print(num)
    print(type(num))  # <class 'tuple'>
    # 虽然元祖是默认不可变的长度和元素，但是这样操作又让它变成可变元素
    demo_sum = 0
    for i in num:
        demo_sum += i
        print(demo_sum)
    return demo_sum

if __name__ == '__main__':
    print("===================================")
    print("最终结果为：", print_multiple(1, 1, 1))
    print("最终结果为：", print_multiple(1, 2, 3, 4))
    print("===================================")
