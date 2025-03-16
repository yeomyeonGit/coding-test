n, k = map(int, input().split())

aryA = list(map(int, input().split()))
aryB = list(map(int, input().split()))

# print(aryA)  # 출력: [1, 2, 3, 4, 5]
# print(aryB)  # 출력: [5, 5, 5, 6, 6]


##### 아래 코드도 좋지만, 매번 정렬을 해야 해서 시간복잡도 측면에서 비효율적임
# for _ in range(k):
#     aryA = sorted(aryA)
#     aryB = sorted(aryB)
#     if aryA[0] < aryB[n-1]:
#         aryA[0], aryB[n-1] = aryB[n-1], aryA[0]
#     print(aryA)
#     print(aryB)

# print(aryA)
# print(sum(aryA))

aryA.sort()
aryB.sort(reverse=True)

for i in range(k):
    if aryA[i] < aryB[i]:
        aryA[i], aryB[i] = aryB[i], aryA[i]
        print(aryA)

print(aryA)
print(sum(aryA))


