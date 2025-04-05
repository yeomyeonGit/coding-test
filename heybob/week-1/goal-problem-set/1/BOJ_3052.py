# 나머지
# https://www.acmicpc.net/problem/3052

numbers = [int(input()) for _ in range(10)]
left = set()

for number in numbers:
    left.add(number % 42)

print(left)
print(len(left))
