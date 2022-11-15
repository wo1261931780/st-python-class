class Pet:
    breed = "animal"

    def __int__(self, name, age):
        self.name = name
        self.age = age


def main():
    # alf = Pet("alf",11) # 这里会直接报错，无法进行带参构造
    alf = Pet()
    alf.name = "alf"
    alf.age = 11  # 这是实例属性的修改方法，但是上面无法完成带参构造，所以这样也是可行的
    moon = Pet()
    moon.name = "moon"
    moon.age = 22
    print("alf:", alf.__class__.breed)
    print("moon:", format(moon.__class__.breed))
    print("{} is {} years old".format(alf.name, alf.age))  # 给对象的属性赋值的两种方式
    print(moon.name, "is ", moon.age, "years old")
    print("===================================")
    alf.__class__.breed = "alf_animal"
    print("我是alf的breed属性：", alf.__class__.breed)


def __del__(self):
    if self.name == "alf":
        __del__(self)  # 析构函数，手动删除对象，回收垃圾
    print("==========删除完成===========")


if __name__ == '__main__':
    main()
