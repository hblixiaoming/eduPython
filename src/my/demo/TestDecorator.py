# 装饰器
import functools


# 这就是一个装饰器
def decorator_a(fun):
    print('decorator a')

    @functools.wraps(fun)
    def inner_a(*args, **kwargs):
        print("inner a")
        return fun(*args, **kwargs)

    return inner_a


def decorator_b(fun):
    print('decorator b')

    @functools.wraps(fun)
    def inner_b(*args, **kwargs):
        print('inner b')
        return fun(*args, **kwargs)

    return inner_b


@decorator_b
@decorator_a
def hello():
    print('hello word')


hello()

# 装饰hello就相当于
# hello = decorator_a(hello)
# 此时会执行decorator_a，故会打印出decorator a,
# 当执行时因为decorator_a返回的是inner_a函数故会执行inner_a函数
# 当执行inner_a函数时会打印inner a，同时inner_a函数里调用了hello函数所以。hello会被最后执行
# 故如果只有一个装饰器的时候会先打印
# decorator a
# inner_a
# hello world

# 当有多个装饰器的时候会形如如下
# hello = decorator_b(decorator_a(hello))
# 故先打印了decorator a 在打印decorator b
# 执行时先decorator_b 返回的内部函数故打印了inner b
# 执行inner_b函数时会在执行包装的decorator_a里的inner_a
# 故打印了inner_a,在执行inner_a时又执行了hello故打印了hello


# 所以包装顺序为从下向上，执行顺序为从上向下
