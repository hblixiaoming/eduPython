def pow(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(pow(2, 2))

