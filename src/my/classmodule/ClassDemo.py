class Animal:
    name = '动物'
    # 1:动物 2:植物
    __type = 1

    def __init__(self, color, age, weight):
        self.color = color  # 定义在构造器里的属性属于实力属性
        self.age = age
        self.__weight = weight
        print('父类构造函数被执行')
        pass

    def normal_method(self):
        print('颜色：%s，年龄：%s，重量：%s' % (self.color, self.age, self.__weight))

    def normal_method1():
        print('normal_method1')
        pass

    @classmethod
    def class_method(cls):  # 增加classmethod修饰后为类属方法只能通过类访问切无法访问实力属性
        print(cls.name)
        pass

    @staticmethod
    def static_method():  # 通过staticmethod修饰后即可以通过属性访问也可以通过类访问
        print('static_method')
        pass

    class Eye:
        def __init__(self, color, num):
            self.__color = color
            self.__num = num
            pass

        @property
        def color(self):
            print()
            return self.__color

        @color.setter
        def color(self, color):
            self.__color = color
            pass

        @property
        def num(self):
            return self.__num

        @num.setter
        def num(self, num):
            self.__num = num
            pass

    pass


class Walk:
    def __init__(self, legs):
        self.__legs = legs
        pass

    @property
    def legs(self):
        print('get legs')
        return self.__legs

    @legs.setter
    def legs(self, legs):
        print('set legs')
        self.__legs = legs
        pass

    pass


class Dog(Animal, Walk):
    name = "狗"

    def __init__(self):
        super().__init__('红色', 23, 299)
        self.color = '黄色'
        pass

    pass


if __name__ == '__main__':
    animal = Animal('黄色', 23, 100)
    animal.static_method()
    # 方法1
    eve = Animal.Eye("黑色", 2)
    print(eve.color)
    print('--------------')
    # 方法 2
    eve2 = animal.Eye('蓝色', 2)
    print(eve2.color)

# Animal.class_method()
# animal = Animal('红色', 10, 170)
# print(animal.name)
# animal.normal_method()
# Animal.static_method()
# animal.static_method()
# Animal.normal_method1()
# dog = Dog()
# print(dog.color)
# dog.normal_method()
# dog.static_method()
# dog.class_method()
# Dog.class_method()
# print(dog.name)
# print('------------------')
# chicken = Walk(2)
# chicken.legs = 1
# print(chicken.legs)
#
# print('-----------------')
# dog.legs = 4
# print(dog.legs)
