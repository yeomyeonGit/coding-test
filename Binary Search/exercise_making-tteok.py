n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()


total = 0
start = 0
end = max(lst)

while start <= end:
    mid = (0 + end) // 2
    for x in lst:
        if x > mid:
            total += x - mid

    if total > m:
        start = mid + 1
    elif total < m:
        start = mid + 1
    else:
        result = mid

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
