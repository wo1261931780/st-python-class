from typing import final, Final


class Pet:
    kind: Final = "animal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @final
    def info(self):
        print("pet information is kind={},\t name={},\t age={}".format(self.kind, self.name, self.age))


class Dog(Pet):
    eat = "dog eat meat"

    def __init__(self, name, age):
        super().__init__(name, age)
        self.__class__.kind = "dog"

    def info(self):
        # super().info()
        print("this is override information")
        # 直接在这里使用重写也是可以的
        # 课程说的是报错，实际不会报错，但是会提示不应该出现重写


def main():
    dog_son = Dog("dog son", 11)
    dog_son.info()
    # 除此以外，cmd中也不会出现任何info信息


if __name__ == '__main__':
    main
