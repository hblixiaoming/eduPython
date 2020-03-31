# 测试列表常用方法
if __name__ == '__main__':
    # id() 返回变量的唯一标识类似于内存地址
    a = 'abc'
    print(id(a))
    # len() 请求一个变量的长度
    l = [1, 2, 3, 4]
    print(len(l))
    # type() 返回一个变量的类型，不会考虑继承的问题
    l = 3
    print(type(3))

    # instance() 判断某个对象是否是某个类的实例，会考虑继承
    b = 'abc'
    print(isinstance(a, str))
    print(isinstance(a, object))
    # str() 相当于java的toString()
    d = ['a', 1, 4, 5, 'r']
    print(str(d))
