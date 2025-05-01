def func(li, lj, ri, rj):

    # 데이터가 1개일 경우 종료
    if ri - li == 1:
        return matrix[li][lj]

    mi = (li + ri) // 2
    mj = (lj + rj) // 2

    max1 = func(li, lj, mi, mj)
    max2 = func(li, mj, mi, rj)
    max3 = func(mi, lj, ri, mj)
    max4 = func(mi, mj, ri, rj)

    return max(max1, max2, max3, max4)


# 2차원 배열의 최대값을 재귀적으로 찾는 함수
def find_max_recursive(matrix, x, y, size):
    # 베이스 케이스
    if size == 1:
        return matrix[x][y]
    # TODO
    # 재귀 케이스 : 현재 매트릭스를 네 개의 사분면으로 나누어 각 부분의 최대값을 찾기
    half = size // 2
    max1 = find_max_recursive(matrix, x, y, half)  # TODO)                # 왼쪽 위
    max2 = find_max_recursive(matrix, x, y + half, half)  # TODO)           # 오른쪽 위
    max3 = find_max_recursive(matrix, x + half, y, half)  # TODO )          # 왼쪽 아래
    max4 = find_max_recursive(matrix, x + half, y + half, half)  # TODO )

    #   print(max1, max2, max3, max4)   # 오른쪽 아래

    # 네 사분면 중 가장 큰 값을 반환
    return max(max1, max2, max3, max4)


# 예제 입력
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# 매트릭스의 크기
n = len(matrix)

# 재귀 함수를 사용하여 최대값 찾기
max_value = find_max_recursive(matrix, 0, 0, n)

# 최대값 출력
print("분할: ", max_value)  # 예상 출력: 16
print("범위:", func(0, 0, n, n))
