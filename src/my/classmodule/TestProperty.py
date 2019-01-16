# python @property and @setter 的用法
class Student:
    def __init__(self, score):
        self.__score = score
        pass

    @property
    def score(self):
        return self.__score

    pass

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('score error')
        self.__score = score
    pass

stu = Student(2)
print(stu.score)
stu.score = 60
print(stu.score)

stu.score = 200
print(stu.score)

