from bisect import bisect_left

n1 = int(input())
arr_A = list(map(int, input().split()))
arr_A.sort()  # 정렬 추가!

n2 = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    i = bisect_left(arr_A, number)

    if i < len(arr_A) and arr_A[i] == number:
        print(1)
    else:
        print(0)
