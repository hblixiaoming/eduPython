class Animal(object):
    def dispay(self):
        print("we are animal")

    pass


class Runable(object):
    def run(self):
        print("we can run")

    pass


class Flyable(object):
    def fly(self):
        print("we can fly")

    pass


class Dog(Animal, Runable):
    pass


class Bird(Animal, Flyable):
    pass


dog = Dog()
dog.run()
dog.dispay()
