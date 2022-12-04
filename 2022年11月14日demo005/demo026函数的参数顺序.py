# def print_info(num1, num2, num3=0, num4):
# 如果上面num3给了默认值，但是num4没有
# 就会直接报错
def print_info(num1, num2, num3=0, num4=0):
    print("num1:{},num2:{},num3:{},num4:{}".format(num1, num2, num3, num4))
    return num1+num2+num3+num4


if __name__ == '__main__':
    print_info(1, 0, 0, 1)
    print(print_info(1, 2, 3))
    print_info(1, 0, num4=11) # 直接跳过一个参数，给第四个参数赋值
