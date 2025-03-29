# 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다.
# 다음 T줄에는 각각 두 정수 A와 B가 주어진다.
# A와 B는 1 이상, 1,000 이하이다.

# 요구사항: 순서쌍의 합을 출력


import sys


my_input = sys.stdin.readline
n = int(my_input().rstrip())

arr = [sum(list(map(int, my_input().rstrip().split()))) for _ in range(n)]

for i in arr:
    print(i)
