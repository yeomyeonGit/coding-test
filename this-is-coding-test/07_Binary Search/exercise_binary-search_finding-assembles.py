n = int(input())
lst1 = list(map(int, input().split()))
lst1.sort()
# 이진탐색은 리스트가 무조건 정렬돼 있어야 한다

m = int(input())
lst2 = list(map(int, input().split()))

##################### 이코테 풀이 1) 이진 탐색

# 이진탐색은 쉽게 말하자면 리스트를 접어 중간 인덱스의 값을 확인하는 거다. 그러니까 mid는 그 자체가 중간값이 아니라, 중간값의 인덱스!


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == lst1[mid]:
            return mid
            # 중간값이 찾는 값이랑 일치하면 바로 리턴한다

        elif target < lst1[mid]:
            end = mid - 1

        else:  # target > mid
            start = mid + 1

    return None
    # 찾는 값이 그 어떤 중간값에도 없으면 None 리턴, 즉, 이 리스트에는 찾는 값이 없다는 것을 알 수 있다


for i in lst2:
    result = binary_search(lst1, i, 0, n - 1)

    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")

##################### 나만의 풀이 1) 중첩 반복문
# answer = ""
# for i in range(m):
#     for j in range(n):
#         if lst2[i] == lst1[j]:
#             answer = "yes"
#             break
#         else:
#             answer = "no"

#     print(answer, end=" ")

##################### 나만의 풀이 2) in 존재 여부로 확인
# for i in range(m):
#     if lst2[i] in lst1:
#         print("yes", end= " ")
#     else:
#         print("no", end= " ")
