class Pet:
    bleed = "pet"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        # print("pet breed={},name={},age={}", self.bleed, self.name, self.age)
        print("pet breed={},name={},age={}".format(self.bleed, self.name, self.age))


class Dog(Pet):
    eat = "meat"

    def __init__(self, name, age):
        # super.__init__(name, age)
        # super.__init__(self)
        super().__init__(name, age)  # 必须这样写
        self.__class__.bleed = "dog animal"
        self.info()
        print("dog eat", self.__class__.eat)


def main():
    animal = Pet("animal", 5)
    dog1 = Dog("dog1", 7)
    print("===================================")
    print("animal1,name=", animal.bleed, "，age:", animal.age)
    dog1.info()


if __name__ == '__main__':
    main()
