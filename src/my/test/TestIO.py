import os


def readFile(fileName):
    try:
        f = open(fileName, "r")
        result = f.read()
        # f.read(1024)
        # f.readLine()
        print(result)
    except FileNotFoundError as e:
        print(e)
    finally:
        if f:
            f.close()
    pass


def writeFile(fileName):
    try:
        f = open(fileName, "w+")
        f.write("hello world")
    except FileNotFoundError as e:
        print(e)
    finally:
        if f:
            f.close()
    pass


# readFile("a.txt")
# writeFile("a.txt")

print(os.name)
# print(os.environ)

# print(os.path.abspath("."))

print(os.path.join("D:\\test", "abc"))
print(os.mkdir(os.path.join("D:\\test", "abc")))


