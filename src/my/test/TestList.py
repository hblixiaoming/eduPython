if __name__ == '__main__':
    # 列表的内涵
    l1 = [x for x in range(1, 10)]
    print(l1)

    l2 = [x for x in range(1, 100) if x % 2 == 1]
    print(l2)

    l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l4 = [x + 4 for x in l3]
    print(l4)

    