# 이진 탐색
# 찾는 값의 인덱스를 반환한다

def bs(arr, target):
    # 맨 첫 인덱스와 맨 끝 인덱스
    l, r = 0, len(arr) - 1

    while l <= r:
        # 중간 인덱스
        mid = (l + r) // 2
        # 중간값이 찾는 값과 일치하면 반환
        if arr[mid] == target:
            return mid
            # 중간값이 찾는 값보다 크면 맨 끝 인덱스를 조정해서 값을 찾는 범위를 조정
        elif target < arr[mid]:
            r = mid - 1
        else:
            # 중간값이 찾는 값보다 작으면 맨 처음 인덱스를 조정해서 값을 찾는 범위를 조정
            l = mid + 1

    # 아무 거에도 해당이 안되면 -1 반환
    return -1


arr = [2, 5, 17, 22, 27, 35, 42, 51, 62, 70]  # sorted list
# 이진탐색은 정렬된 배열에만 적용 가능하다
target = 51

print(bs(arr, target))
