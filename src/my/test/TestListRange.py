list = list(range(1, 11))

print(list)

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

L = ['Hello', 'World', 'IBM', 'Apple']

print([s.lower() for s in L])
