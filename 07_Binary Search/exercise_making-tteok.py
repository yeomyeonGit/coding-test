n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

start = 0
end = max(lst)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in lst:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    # elif total > m:
    #     start = mid + 1
    else:
        result = mid
        start = mid + 1


print(result)


# mid = (0 + (n-1)) // 2

# total = 0
# max = 0
# for x in lst:
#     if x >= lst[mid]:
#         total += (x - lst[mid])

# if total > m:
#     max = lst[mid] + ((total - m) / 2)
# elif total < m:
#     max = lst[mid] - ((total - m) / 2)
# else:
#     max = lst[mid]

# print(max)
