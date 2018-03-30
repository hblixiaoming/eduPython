class Person:
    __privateName = ""
    __privateAge = 0
    __privateIsMarried = False

    def __init__(self):
        self.__privateName = 'this is a pen \
        this is a apple'

        self.__privateAge = 23

        self.__privateIsMarried = True

    def run(self):
        if self.__privateIsMarried:
            print(self.__privateName, "has married")
        else:
            print(self.__privateName, "has not married")
