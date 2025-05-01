n = int(input())


def tenToEight(n):
    if (n // 8) == 0:
        return str(n % 8)
    else:
        return tenToEight(n // 8) + str(n % 8)

print(tenToEight(n))