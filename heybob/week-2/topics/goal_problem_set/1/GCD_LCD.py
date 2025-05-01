a, b = map(int, input().split())


def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)


print(GCD(a, b))
print(int((a * b) / GCD(a, b)))
