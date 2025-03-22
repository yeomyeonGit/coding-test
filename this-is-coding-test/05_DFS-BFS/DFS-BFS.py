# 실전 문제 - 음료수 얼려 먹기 백지 코딩

n, m = map(int, input().split())

print(n, m)

ice = []
for i in range(n):
    ice.append(list(map(int, input().strip())))

print(ice)


def iceCream(x, y):
    if x < 0 or y >= m or y < 0 or x >= n:
        return False
    
    if ice[x][y] == 0:
        ice[x][y] = 2   # 방문처리
        iceCream(x, y - 1)
        iceCream(x - 1, y)
        iceCream(x + 1, y)
        iceCream(x, y + 1)
        return True
    
    return False

result = 0

for i in range(n):
    for j in range(m):
        if iceCream(i, j):
            result += 1

print(result)
