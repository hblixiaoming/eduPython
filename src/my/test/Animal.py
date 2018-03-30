class Animal(object):
    def run(self):
        print("animal is running")

    pass


class Dog(Animal):
    def eat(self):
        print("dog is eating")

    def run(self):
        print("dog is running")

    pass


class Cat(Animal):
    def run(self):
        print("cat is running")

    pass


dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(cat, Dog))

print("-------------")

print(type(123) == int)

print(dir(cat))
