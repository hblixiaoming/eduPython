import pickle
import json


# d = dict(name="Bob", age=23, score=88)
#
# # pickle.dumps(d)
#
# f = open("a.txt", "wb")
#
# pickle.dumps(d, f)
#
# f.close()

# d = dict(name='Bob', age=20, score=88)
# jsonStr = json.dumps(d)
#
# jsonObj = json.loads(jsonStr)
#
# print(jsonObj['name'])

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __dict__(self):
        return {
            "name": self.name,
            "age": self.age,
            "score": self.score
        }

    pass


s = Student('Bob', 20, 88)
print(json.dumps(s, defalut=lambda x: x.__dict__))
