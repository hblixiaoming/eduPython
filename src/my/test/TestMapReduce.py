from functools import reduce


def mapFun(x):
    return x * x


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

m = map(mapFun, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(m))


def reduceFun(x1, x2):
    return x1 + x2


r = reduce(reduceFun, L)

print(r)

print(list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9]))))

L = [1, 2, 3, -5, 4]
print(sorted(L), lambda x: abs(x))
