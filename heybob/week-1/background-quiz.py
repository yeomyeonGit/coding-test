# # Q1. 내장함수 split

# text = 'a b c d e'
# print(text.split())

# # Q2. 리스트 합치기
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)

# #Q3. 형변환
# my_num = '112'
# print(int(my_num))

# my_data = {1, 2, 3}   # () 이게 튜플
# print(list(my_data))

# # Q4. 1차원 배열 탐색하기 - 점검하기!!!!!
# lst = []
# for _ in range(2):
#     lst.append(input())

# fruits = lst[0].split()

# for i in range(len(fruits)):
#     if lst[1] == fruits[i]:
#         print(lst[1]," 발견!")
#         print(lst[1],"의 인덱스는", i)


# # Q5. 2차원 배열 탐색하기

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# target = 5
# isFlag = False

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(f"position: {i}, {j}, element: {matrix[i][j]}")
#         if target == matrix[i][j]:
#             isFlag = True
#             print(f"target이 matrix 안에 있나요? {isFlag}")
#             break
#     if isFlag:
#         break

# ###### break를 조건식 없이 쓰면 그냥 1번 실행되고 종료되는구나!

# Q6. 인덱싱이 가능한 자료형
my_list = [1,2,3,4]
print(my_list[0])
my_tuple = (1,2,3,4)
print(my_tuple[0])
my_set = {1,2,3,4}
# print(my_set[0]) - set은 순서가 없어서 인덱싱이 안되는구나
# File "c:\Users\win\Desktop\coding test\heybob\week-1\background-quiz.py", line 60, in <module>
#     print(my_set[0])
#           ~~~~~~^^^
# TypeError: 'set' object is not subscriptable
my_dict = {1:'a',2:'b',3:'c',4:'d'}

# print(my_dict[0])    

