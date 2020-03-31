if __name__ == '__main__':
    # 定义一个列表
    l1 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(l1)

    # 列表的内涵，取l1中偶数
    l2 = [x for x in l1 if x % 2 == 0]

    print(l2)

    l3 = ['a', 'b', 'c', 'd', 'e', 'f']

    # 列表的遍历
    for x in l3:
        print(x, end=' ')

    print("\n")

    print("*" * 20)

    # 判断一个元素属于一个列表
    if 'a' in l3:
        print('{0} i am in zhe list'.format('a'))

    # 返回一个列表的长度
    print(len(l3))

    # 返回一个元素在列表中的下标
    print(l3.index('b'))

    # 在列表的末尾插入一个元素
    l3.append('g')
    print(l3)

    # 在指定位置插入一个元素
    l3.insert(0, '0')
    print(l3)

    print('*' * 20)
    print(l3)
    # 弹出末尾的元素
    e = l3.pop()
    print(e)
    print(l3)

    print('*' * 20)
    print(l3)
    # 弹出指定位置的元素
    e1 = l3.pop(0)
    print(e1)
    print(l3)

    # 浅copy 一个列表
    l4 = l3.copy()
    print(l4)

    l4[0] = 'A'
    print(l3)
    print(l4)

    # 此时l5与l3指向同一块地址空间
    l5 = l3
    l5[1] = 'B'
    print(l3)
    print(l5)

    # 列表分片相关
    l6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 返回下标1后面的所有元素,包括下标1的元素
    l7 = l6[1:]
    print(l7)

    # 返回下标2到下标5之间的元素，不包含结尾的元素（包含头不包含尾）
    l8 = l6[1:5]
    print(l8)

    # 返回从头开始到下标5之间的元素，不包含结尾的元素（包含头不包含尾）
    l9 = l6[:5]
    print(l9)

    # 返回倒数第一个元素
    l10 = l6[-1]
    print(l10)

    # 返回倒数第5个到倒数第2个元素，不包含倒数第2个
    l11 = l6[-5:-2]
    print(l11)

    # 返回倒数第二一直到末尾的元素
    l12 = l6[-2:]
    print(l12)

    # 返回从开始到倒数第5个元素，不包含倒数第5
    l13 = l6[:-5]
    print(l13)

    # 返回整个列表
    l14 = l6[:]
    print(l14)

    # 表示从头到结尾每隔2个元素打印一次
    l15 = l6[::2]
    print(l15)

    # 表示从结尾到头每隔2个元素打印一次
    l16 = l6[::-2]
    print(l16)

    # 从这里可以看出切片是对原列表的copy等同于copy方法，新列表与原列表指向不同的内存空间
    l17 = l6[::]
    l17[0] = 'a'
    print(l6)
    print(l17)

    str = "0123456789"
    print("打印第0个元素:", str[0])
    print("负数表示倒数第N个元素，-1表示倒数第一个元素:", str[-1])
    print("分片操作，str[start:end], start会包含在结果中而end却不会:", str[1:5])
    print("冒号后不写表示从start到末尾:", str[5:])
    print("表示从倒数第二个元素一直到末尾:", str[-2:])
    print("表示从倒数第六个元素到倒数第二个元素，但不包含倒数第二个元素:", str[-6:-2])
    print("start不写表示从开头开始到end, 但不包含end:", str[:4])
    print("start和end都不写表示整个列表:", str[:])
    print("支持步长，步长为正数表示从start到end每隔N个数打印一个:", str[::2])
    print("步长为负数表示从end到start每隔N个数打印一个:", str[::-2])
    print("若end比start小，则步长必须为负数否则会出错:", str[-1:-6:-1])

    print("*" * 20)

    l18 = [10, 11, 12, 13, 14]
    # 删除指定下标的元素
    del l18[0]
    print(l18)

    print("*" * 20)

    # 删除指定元素
    l19 = [10, 11, 12, 13, 14, 15]
    l19.remove(10)
    print(l19)

    # 请款整个列表
    print("*" * 20)
    l20 = [10, 11, 12, 13, 14, 16]
    l20.clear()
    print(l20)

    # 将一个列表整体追加到另一个
    l21 = [1, 2, 3, 4, 5]
    l22 = ['a', 'b', 'c', 'd']
    l21.extend(l22)
    print(l21)
