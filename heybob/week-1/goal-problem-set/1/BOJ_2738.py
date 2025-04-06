n, m = map(int, input().split())

lst_1 = []
for i in range(n):
    numbers = list(map(int, input().split()))
    lst_1.append(numbers)

lst_2 = []
for i in range(n):
    numbers = list(map(int, input().split()))
    lst_2.append(numbers)

for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(lst_1[i][j] + lst_2[i][j])
    print(*tmp)