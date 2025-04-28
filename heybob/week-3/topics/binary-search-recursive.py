def bs_recur(arr, target, l, r):
    if l > r:
        return -1

    mid = (l + r) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return bs_recur(arr, target, l, mid - 1)
    else:
        return bs_recur(arr, target, mid + 1, r)


arr = [2, 5, 17, 22, 27, 35, 42, 51, 62, 70]  # sorted list
# 이진탐색은 정렬된 배열에만 적용 가능하다
target = 51

print(bs_recur(arr, target, 0, len(arr) - 1))
