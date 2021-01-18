# 边界：F(1)=1,F(2)=2
# 最优子结构：F(n-1)和F(n-2)
# 状态转移函数：F(n)=F(n-1)+F(n-2)
def upstairs(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return upstairs(n - 1) + upstairs(n - 2)


def upstairsLoop(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    pr = 2
    ppr = 1
    i = 3
    result = 0
    while i <= n:
        result = pr + ppr
        ppr = pr
        pr = result
        i = i + 1
    return result


class Node:
    def __init__(self, num, cost, value):
        self.num = num
        self.cost = cost
        self.value = value

    def __str__(self):
        return "%d-%d-%d " % (self.num, self.cost, self.value)

    def __repr__(self):
        return "%d-%d-%d " % (self.num, self.cost, self.value)


class Ele:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "%d" % self.value

    def __repr__(self):
        return "%d" % self.value


def package01(node, weight):
    result = [[0 for i in range(len(node))] for j in range(weight)]
    print(result)
    if weight == 0:
        return result
    for i in range(weight):
        j = 0
        while j < len(node):
            lastV = 0
            if j - 1 >= 0:
                lastV = result[i][j - 1].value
            value = lastV
            k = i + 1
            if k >= node[j].cost:
                newV = node[j].value
                if (k - node[j].cost >= 0) and j - 1 >= 0:
                    newV = newV + result[k - node[j].cost][j - 1].value
                if newV > lastV:
                    value = newV
            result[i][j] = Ele(value)
            j = j + 1
    print(result)


if __name__ == '__main__':
    # print(upstairs(10))
    # print(upstairsLoop(10))
    a = [Node(1, 1, 15), Node(2, 3, 30), Node(3, 1, 20)]
    package01(a, weight=4)
