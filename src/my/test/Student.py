class Student(object):
    name = "bob"
    age = 23

    # limit zhe attribute
    __slots__ = ("__name", "__age", "__score")

    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score

    def print(self):
        print(self.__name + ":" + str(self.__age))

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


student = Student("lxm", 23, 23.4)
student.print()

print(student.get_age())
print(student.name)
student.score = 30.4
print(student.score)

