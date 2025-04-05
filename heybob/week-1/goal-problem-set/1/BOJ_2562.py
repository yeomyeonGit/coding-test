# 2562
# https://www.acmicpc.net/problem/2562

lst = [int(input()) for _ in range(9)]

max = 0
final_i = 0
for i in range(len(lst)):
    if lst[i] > max:
        max = lst[i]
        final_i = i + 1

print(max)
print(final_i)
