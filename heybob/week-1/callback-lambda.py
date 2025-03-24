# 가장 기초적인 배열 탐색은 for 문을 이용한 탐색

# 배열 내 최댓값 찾기

arr = [1, 2, 4, 6, 1, 2, 3]
max_value = float("-inf")
# print(max_value)

for ele in arr:
    if ele > max_value:
        max_value = ele

print(max_value)
