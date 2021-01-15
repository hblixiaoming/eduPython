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


class Ele:
    def __init__(self, node, value):
        self.node = node
        self.value = value


def package01(*node, weight):
    result = []
    if weight == 0:
        return result
    


if __name__ == '__main__':
    print(upstairs(10))
    print(upstairsLoop(10))
