class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return self.__name + "," + str(self.__age)

    def __iter__(self):
        return self.__age

    def __getattr__(self, item):
        if item == "score":
            return 'no score'

    def __call__(self):
        print("method call")

    pass


stu = Student("lxm", [23, 45, 67])
print(stu)

print(stu.score)

print(stu())

# judge whether a object can call
print(callable(stu))

