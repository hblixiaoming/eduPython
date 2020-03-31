class Animal():
    name = 'animal'

    def sleep(self):
        print('I can sleep')


class Person(Animal):
    def work(self):
        print('I can work')
        pass

    pass


class Teacher(Person):
    def teach(self):
        print('I can teach')
        pass

    pass


t = Teacher()
t.sleep()
print(Teacher.__mro__)
Teacher.__()

