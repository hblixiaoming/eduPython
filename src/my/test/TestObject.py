'''
 1 python和 java 一样都有对象属性方法和类属性和方法
 2 python的类属性直接定义在类中 例如 下面的 name = 'jiangjing'
 就属于类属性，在类中访问可以通过__class__.属性名字例如(__class__.name)或者通过类名访问例如(A.name)
 3 python的实例属性则可以直接通过将属性直接赋值给对象本身来创建例如(self.name = 'niuniu')
 4 python方法中的第一个参数self属于占位符并不是关键字，换成其他的也可以，有self的方法属于实例方法
 5 python中没有self的方法默认属于类方法
 6 通过实例.例如(a.class_say())的方式调用方法的情况，因为python默认会把当前实例a传递给class_say()
 但是class_say()并没有参数来接a固会报错，可以看做class_say()是类的方法，此时也可以随便传1个参数
 7 python遵从鸭子模型，因为python是弱类型语言所以python针对方法并不会去校验方法参数的类型，只要
 需要对象的属性和传入对象的属性一致就可以
'''


class A():
    # 类的属性，直接赋值给对象本身的是对象的属性
    name = 'jingjing'
    age = 23

    def __init__(self):
        self.name = 'niuniu'
        self.age = 16
        pass

    # 带有self的方法都是属性方法，self并不是一个关键字只是一个占位符,系统会默认把当前对象传递给self
    def object_say(self):
        print('%s is %s years old' % (self.name, self.age))
        print(A.name)
        return None

    def object_run(self):
        self.legs = 4
        return None

    # 可以在类内部通过__class__访问到类的属性
    def object_changeName(s):
        __class__.name = 'zhuzhu1'
        return None

    def object_setEys(s):
        s.eyes = 2
        print(s.eyes)
        return None

    # 这个方法是类方法
    def class_say():
        print(__class__.name)
        return None

    def yaZiTestObject(self):
        print(self.name)
        return None

    pass


class B():
    name = 'classB'
    pass


class C():
    class_age = 18

    # 用来限制可以绑定的属性名
    __slots__ = ('__dict__', 'age', 'name', 'sex')

    def say(self):
        # 默认会访问类的属性
        print(self.class_age)
        print(id(self.class_age))
        self.age = 20
        print(self.age)
        print(id(self.age))
        print(id(__class__.class_age))
        return None

    pass


if __name__ == '__main__':
    a = A()
    a.object_say()
    print(a.__dict__)
    print(A.__dict__)
    a.object_run()
    print(a.legs)
    a.name = 'zhuzhu'
    print(A.name)
    a.object_changeName()
    print(A.name)
    a.object_setEys()

    # 因为python默认会把当前实例a传递给class_say()
    #  但是class_say()并没有参数来接a固会报错
    # a.class_say()
    A.class_say()

    print('*' * 20)
    a1 = A()
    a1.yaZiTestObject()
    # 鸭子模型此处可以传递一个有name属性的对象就不会报错
    A.yaZiTestObject(a1)
    # 此处直接传递了一个B类对象，因为B类对象也有name属性所以不会报错
    A.yaZiTestObject(B)

    b = B()
    # b.name = 'objectB'
    # 此时对象b并没有name属性，但是直接访问了B类的name属性
    A.yaZiTestObject(b)

    print('*' * 20)
    c = C()
    print(c.class_age)
    c.say()

    print('*' * 20)
    print(c.__dict__)
    C.legs = 2
    print(C.legs)
