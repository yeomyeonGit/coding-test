# https://www.acmicpc.net/problem/2562
# import sys

# lst = list(map(int, sys.stdin.readlines()))
# print(lst)

# maxVal = max(lst)

# for i in range(len(lst)):
#     if maxVal == lst[i]:
#         print(lst[i])
#         print(i+1)

import sys

lst = list(map(int, sys.stdin.readlines()))

max_value = max(lst)  # 최댓값 찾기
max_index = lst.index(max_value) + 1  # 최댓값의 위치 (1-based index)

print(max_value)
print(max_index)
