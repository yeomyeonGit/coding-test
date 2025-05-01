n = int(input())
# 문자열 입력 받기
matrix = [list(map(int, input())) for _ in range(n)]


def func(li, lj, ri, rj):

    # 종료 조건 1: 1칸일 때
    if ri - li == 1:
        if matrix[li][lj] == 1:
            return str(1)
        else:
            return str(0)

    # 종료 조건 2: 모든 색깔이 동일할 때
    color = matrix[li][lj]
    isConsitent = True

    for i in range(li, ri):
        for j in range(lj, rj):
            if color != matrix[i][j]:
                isConsitent = False
                break

        if not isConsitent:
            break

    if isConsitent:
        if color == 1:
            return str(1)
        else:
            return str(0)

    mi = (li + ri) // 2
    mj = (lj + rj) // 2

    rec1 = func(li, lj, mi, mj)
    rec2 = func(li, mj, mi, rj)
    rec3 = func(mi, lj, ri, mj)
    rec4 = func(mi, mj, ri, rj)

    res = "(" + rec1 + rec2 + rec3 + rec4 + ")"

    return res


print(func(0, 0, n, n))


# 종료 조건 없이
def quat_tree(matrix, x, y, size):
    color = matrix[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if color != matrix[i][j]:
                half = size // 2
                return (
                    "("
                    + quat_tree(matrix, x, y, half)
                    + quat_tree(matrix, x, y + half, half)
                    + quat_tree(matrix, x + half, y, half)
                    + quat_tree(matrix, x + half, y + half, half)
                    + ")"
                )

    return str(color)


# print(quat_tree(matrix, 0, 0, n))
