# 在python里函数也是一个变量

from functools import reduce

if __name__ == '__main__':
    fun1 = lambda x, y: x + y
    print(fun1(1, 2))

    fun2 = lambda x: print('hello %s' % x)
    print(fun2('boy'))

    l1 = [x for x in range(0, 10)]
    print(l1)
    # 对所有元素+10后输出
    l2 = map(lambda x: x + 10, l1)
    for x in l2:
        print(x, end=' ')

    print('\n')
    # 对l1中的所有元素进行聚合
    n1 = reduce(lambda x, y: x + y, l1)
    print(n1)

    # 使用filter过滤l1中所有的奇数
    l3 = filter(lambda x: x % 2 == 1, l1)
    for x in l3:
        print(x, end=' ')

    print('\n')

    l4 = [2, 5, 6, 1, 8, 3, 4, 7, 0]

    # 对l4进行排序操作
    l5 = sorted(l4, key=lambda x: x)
    print(l5)


    def fun1(x, before, after):
        before()
        print('execute ing %s' % x)
        after()


    # 函数作为参数使用
    fun1('li', lambda: print('execute before'), lambda: print('execute after'))


    # 函数嵌套，同时函数作为返回值
    def fun2(*args):
        print(args)

        def innerFun():
            print('inner fun args:%s' % args)
            return 'ni daye zai ci'

        return innerFun


    l6 = ['a', 'b', 'c', 'd']
    funResult = fun2(l6)
    print(funResult)
    print(funResult())
