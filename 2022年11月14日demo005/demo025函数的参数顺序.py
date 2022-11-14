def print_info(name, age):
    print("name:", name)
    print("age:", age)
    return


if __name__ == '__main__':
    print_info("Tom", 18)  # python中，对函数的调用默认是遵循变量的顺序
    print_info(age=18, name="Tom")  # 但是也可以自己设置顺序，
    # 设置顺序的时候需要说明具体的变量
