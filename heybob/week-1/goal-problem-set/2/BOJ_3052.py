numbers = [int(input()) for _ in range(10)]

tmpSet = {i % 42 for i in numbers}
print(len(tmpSet))