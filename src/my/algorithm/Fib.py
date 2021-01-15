def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fibC(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    pr = 1
    ppr = 0
    i = 3
    result = 0
    while i <= n:
        result = pr + ppr
        ppr = pr
        pr = result
        i = i + 1
    return result


if __name__ == '__main__':
    print(fib(9))
    print(fibC(9))
