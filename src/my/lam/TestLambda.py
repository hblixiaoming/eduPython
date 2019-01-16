f = lambda x, y, z: x + y + z
print(f(1, 2, 3))


def action(x):
    return lambda y: x + y


a = action(2)
print(a(3))

# lambda in lambda
c = lambda x: lambda y: x + y

result = c(2)(3)
print(result)

print('----test filter----')

result = filter(lambda x: x >= 3, [1, 2, 3, 4, 5])

list = []
for x in result:
    list.append(x)
    pass

print(list)

print('-----test sorted-----')
result = sorted([2, 4, 5, 7, 1, 6], key=lambda x: x)
for x in result:
    print(x)
    pass

print('----test map----')

result = map(lambda x: x + 1, [1, 2, 3, 4, 5])
for x in result:
    print(x)
    pass

print('---- test reduce----')

from functools import reduce

result = reduce(lambda x, y: x + y, [1, 2, 3])
print(result)

result = reduce(lambda x, y: 1, [1, 2, 3])
print(result)

result = reduce(lambda x, y: x + 1, [1, 2, 3])
print(result)

result = reduce(lambda x, y: x + 1, [1, 2, 3], 0)
print(result)

result = reduce(lambda x, y: y + 1, [1, 2, 8])
print(result)

print('----测试组合----')

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = reduce(lambda x, y: x + y, map(lambda x: x + 1, filter(lambda x: x <= 3, list)))
print(result)
