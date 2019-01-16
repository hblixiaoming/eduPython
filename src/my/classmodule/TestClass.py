class Animal:
    # class property
    color = 'red'
    __size = 90

    def __init__(self, size, age):
        # instance property
        self._size = size
        self.__size = size
        self.age = age
        pass

    def getAge(self):
        return self.age

    pass

    @classmethod
    def getClassSize(cls):
        return cls.__size
    pass

    @staticmethod
    def getHeight():
        print(Animal.color)
        return 145

    pass

    @classmethod
    def getName(cls):
        # print(cls.__name__)
        print(cls.color)
        return "dog"

    pass


print('---- test static and class method ----')
print(Animal.getName())
print(Animal.getHeight())

print('---- test instance property ----')
ani = Animal(145, 23)
print(ani.age)
print(ani.getAge())

print(ani._size)
print(Animal.getClassSize())