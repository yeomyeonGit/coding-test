# 링크: https://www.acmicpc.net/problem/1816

# 완전탐색 - 모든 경우의 수를 구한다

n = int(input())
array = []

for _ in range(n):
    number = int(input())
    array.append(number)

for number in array:
    for i in range(2, 1000001):
        if number%i == 0:
            print("No")
            break
        if i == 1000000:
            print("YES")


# # 약수가 2 이상 1,000,000 이하라면 No
#    # 약수를 모두 구한다
# # 약수가 1,000,000보다 크면 YES
#    # 모두 수가 2 이상 1,000,000 이하 수로 나누어지지 않는다면

# for number in array:
#     for i in range(2, 1000001):
#         if number % i == 0:   # 약수를 구하는 코드
#             print("NO")
#             break
    
#         if i == 1000000:    # 약수를 다 구했는데, 2 이상 1000000로 나누어 떨어지지 않는다
#             print("YES")


