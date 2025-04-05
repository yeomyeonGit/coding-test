# 최댓값
# https://www.acmicpc.net/problem/2566

import sys

# 입력
numbers = sys.stdin.read()

# 입력받은 것을 한줄씩 분리하고 한개씩 떼기
tmp = list(map(lambda x: x.split(), numbers.split("\n")))

# 리스트 안에 있는 숫자들을 정수형으로 변환
lst = []
for i in tmp:
    tmp2 = []
    for j in i:
        tmp2.append(int(j))
    lst.append(tmp2)

# 최대값 찾기, 그 위치도 찾기
maximum = -1
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] >= maximum:
            maximum = lst[i][j]
            final_i = i + 1
            final_j = j + 1

# 최대값과 그 위치 프린트
print(maximum)
print(final_i, final_j)


# 조금 어려웠지만 잘했다!
