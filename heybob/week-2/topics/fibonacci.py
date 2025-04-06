# 피보나치 수열


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    n_2 = fibonacci(n - 2)
    n_1 = fibonacci(n - 1)

    return n_1 + n_2


print(fibonacci(7))
