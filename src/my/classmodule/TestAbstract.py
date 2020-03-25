from abc import abstractmethod
from abc import ABC


class Fly(ABC):
    def __init__(self):
        print('init fly')
        pass

    @abstractmethod
    def fly(self):
        pass

    pass


class Bird(Fly):
    def __init__(self):
        print('init bird')
        pass

    def fly(self):
        print('fly with 翅膀')

    pass


if __name__ == '__main__':
    # fly = Fly()
    # fly.fly()
    bird = Bird()
    bird.fly()
