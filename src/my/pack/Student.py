class Student:
    __slots__ = ('name', 'age', 'id')

    def __init__(self, name):
        self.name = name
        pass

    def __del__(self):
        self.name = None
        self.age = None
        self.id = None
        pass

    def getUserName(self):
        return self.name
        pass

    def setUserName(self, name):
        self.name = name
        pass

    pass


def sum(a, b):
    return a + b
pass




# stu = Student("zhangsan")
# print(stu.getUserName())
# stu.setUserName("lisi")
# print(stu.getUserName())
#
# stu.age = 1
# print(stu.age)
#
# del stu
#
# stu1 = Student("liu2")
# stu1.age =23
# stu1.id=1
# try:
#     print(stu1.__dict__)
# except AttributeError as ex:
#     print("error")
#     #raise ex
#     pass
# except Exception as e:
#     print("exception")
#     print(e)
#     pass
# finally:
#     print("finally")
#     pass

# print(22)

