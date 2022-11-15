class Pet:
    kind = "animal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("pet kind={},\tname={},\tage={}".format(self.kind, self.name, self.age))


class Dog(Pet):
    eat = "dog eat meat"

    def __init__(self, name, age):
        super().__init__(name, age)
        self.__class__.kind = "Dog"

    def info(self):
        print("dog kind={},\tname={},\tage={},\teat={}".format(self.kind, self.name, self.age, self.eat))


def main():
    pet_father = Pet("father", 1)
    dog_son = Dog("dog1", 22)
    pet_father.info()
    dog_son.info()


if __name__ == '__main__':
    main()
