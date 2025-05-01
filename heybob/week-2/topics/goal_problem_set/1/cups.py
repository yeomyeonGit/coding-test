# # 이렇게 하면 total이 계속 초기화됨
# def cups(n):
#     total = 0

#     if n < 4:
#         return total

#     total += n // 4
#     return cups((n // 4) + (n % 4))

# print(cups(n))

n = int(input())


def cups(n):
    total = 0
    while n >= 4:
        total += n // 4
        n = (n // 4) + (n % 4)

    return total


print(cups(n))
