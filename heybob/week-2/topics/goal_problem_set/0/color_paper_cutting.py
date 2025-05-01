n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


# 방식 1
def func(li, lj, ri, rj):

    # 한 칸이라서 종료. 이게 없으면 범위를 벗어나 분할을 하거나(잘못된 인덱스 접근)
    # 무한 재귀를 할 수 있다
    if ri - li == 1:
        if matrix[li][lj] == 0:
            return [1, 0]
        else:
            return [0, 1]

    # 모두 같은 색일 때 종료
    color = matrix[li][lj]
    isColor = True  # 모두 같은 색일 때

    for i in range(li, ri):
        for j in range(lj, rj):
            if color != matrix[i][j]:
                isColor = False  # 같은 색이 아닐 때
                break
        if not isColor:
            break

    if isColor:
        if color == 0:
            return [1, 0]
        else:
            return [0, 1]

    mi = (li + ri) // 2
    mj = (lj + rj) // 2

    res = [0, 0]
    rec1 = func(li, lj, mi, mj)
    rec2 = func(li, mj, mi, rj)
    rec3 = func(mi, lj, ri, mj)
    rec4 = func(mi, mj, ri, rj)

    res[0] = rec1[0] + rec2[0] + rec3[0] + rec4[0]
    res[1] = rec1[1] + rec2[1] + rec3[1] + rec4[1]

    return res


res = func(0, 0, n, n)
print(res[0])
print(res[1])

# 바식 2 - 종료 조건 없이
white = 0
blue = 0


def countColor(matrix, x, y, size):
    global white, blue
    color = matrix[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != color:
                half = size // 2
                countColor(matrix, x, y, half)
                countColor(matrix, x + half, y, half)
                countColor(matrix, x, y + half, half)
                countColor(matrix, x + half, y + half, half)
                return

    # print(color)
    if color == 0:
        white += 1
    else:
        blue += 1


countColor(matrix, 0, 0, n)
print(white)
print(blue)
