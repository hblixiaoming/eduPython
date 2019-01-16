# 位置传参
def positonParam(a, b, c):
    print(a)
    print(b)
    print(c)
    pass


positonParam(1, 2, 3)


# 元组传参
# 元组传参是指在函数调用过程中，用*将元组拆解后按位置进行传递的方式
# 元组传参时，序列拆解的位置将与形参一一对应
# 元组的位置信息对应相应的参数

def listParam(*list):
    print(list)
    pass


list = [1, 2, 3]
listParam(list)

tuple = (4, 5, 6)
listParam(tuple, 7, 8)


# 关键字传参：
# 关键字传参是指传参时，按形参的名称给形参赋值
# 实参和形参按形参名进行匹配（可以不按位置顺序进行匹配

def keyWordsParam(a, b, c):
    print(a)
    print(b)
    print(c)
    pass


keyWordsParam(b=2, a=1, c=3)

# 默认参数

print('----默认参数----')


def defaulParam(a, b, c=3):
    print(a)
    print(b)
    print(c)
    pass


defaulParam(1, 2)

# 函数传参

print('------ 函数作为参数------')


def funParam(x, y, fun):
    return fun(x, y)


def add(x, y):
    return x + y


print(funParam(1, 2, add))

print(funParam(1, 2, lambda x, y: x * y))
