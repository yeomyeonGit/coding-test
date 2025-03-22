# 답안 예시(계수 정렬)

#

########### 계수 정렬 알고리즘 구현
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
tmp = [0] * len(array)

for i in range(len(array)):
    tmp[array[i]] += 1

for i in range(len(tmp)):
    print(tmp[i], end=" ")
    # for j in range(tmp[i]):
    #     print(i, end=" ")

# 그러니까 계수 정렬은 특정 값의 인덱스에 마크를 해두는 거.

print()

for i in range(len(tmp)):
    for j in range(tmp[i]):
        print(i, end=" ")

# 마크한 횟수만큼 인덱스를 출력해 수를 정렬
