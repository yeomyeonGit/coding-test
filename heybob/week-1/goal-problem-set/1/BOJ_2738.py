n, m = map(int, input().split())
# print(n, m)

arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

# print(arr1)
# print(arr2)


for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(arr1[i][j] + arr2[i][j])
    print(*tmp)
