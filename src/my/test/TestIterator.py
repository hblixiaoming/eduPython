from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key in d:
    print(d[key])

print("-----------------------------")

for k, v in d.items():
    print(k + ":" + str(v))

print("-----------------------------")

for ch in 'ABC':
    print(ch)

print("-----------------------------")

isinstance("abc", Iterable)

isinstance([1, 2, 3], Iterable)

