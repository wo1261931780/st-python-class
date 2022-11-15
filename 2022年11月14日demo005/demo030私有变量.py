class Pet:
    kind = "pet class"

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __set_name__(self, owner, name):
        self.__name = name

    def print__name(self):
        print("name is {}".format(self.__name))

    def __set_age__(self, age):
        self.__age = age

    def print__age(self):
        print("age is {}".format(self.__age))


def main():
    dog = Pet("dog", 5)
    dog.print__name()
    dog.print__age()
    print("===================================")
    # dog.kind="dog"
    # 下面的已经无法访问了, 因为已经变成了私有变量
    # dog.__class__.__name__ = "dog1"
    # dog.__class__.__age__ = 11
    # dog.print__name()
    # dog.print__age()
    # print("===================================")
    dog.__class__.__set_name__('moon')
    dog.__class__.__set_age__(6)
    dog.print__name()
    dog.print__age()
    print("===================================")


if __name__ == '__main__':
    main()
