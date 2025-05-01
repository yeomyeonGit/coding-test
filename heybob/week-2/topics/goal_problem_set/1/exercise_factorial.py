n = int(input())


def doubleFactorial(n):
    if n <= 1:
        return 1
    else:
        return n * doubleFactorial(n - 2)


print(doubleFactorial(n))
