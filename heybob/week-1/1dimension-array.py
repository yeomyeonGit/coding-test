# input 함수

# split(): 공백 기준으로 문자열을 나눠서 배열에 담을 수 있다
arr = input().split()
print(arr)
# 입력: 우가우가 흠냐링
# 출력: ['우가우가', '흠냐링']

arr = map(int, input().split())
print(arr)
# 입력: 1 2 3 4 5
# 출력 - 주소값: <map object at 0x000001FD5EA68520>

arr = list(map(int, input().split()))
print(arr)
# 입력: 1 3 5 7 9
# 출력: [1, 3, 5, 7, 9]

# 가끔 문제 풀 때
# input이 느려서 안 풀리는 경우가 있다.
# 참고 사항
# 버퍼에 문자열이 담기고 flush를 해야 input이 끝나게 됨
# flush 과정이 느림
# 'input 한 번 받는 게 느리다'

# input() 대신 sys.readline()
# colab / jupyter notebook에서는 실행 안 됨
import sys

my_input = sys.stdin.readline  # () 이걸 없애줘야 함수로 작동하지 않는다
arr = list(map(int, my_input().split()))
print(arr)
# 입력: 10 9 8 7 6 5
# 출력: [10, 9, 8, 7, 6, 5]

# 2차원 배열 입력받기
N, M = list(map(int, input().split()))
# 입력 2 4
# print(N) 출력 : 2
# print(M)  출력 : 2
arr = [list(map(int, input().split())) for _ in range(N)]
# 입력:
# 1 2 3 4
# 5 6 7 8
print(arr)
# 출력: [[1, 2, 3, 4], [5, 6, 7, 8]]

# 느리니까 2차원 배열도 이렇게 입력받자
import sys

my_input = sys.stdin.readline

N, M = map(int, my_input().split())  # 입력: 2 4
arr = [list(map(int, my_input().split())) for _ in range(M)]
# 입력:
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
print(arr)
# 출력: [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]

# 여러 줄을 받을 때
N, M = [1, 3]  # 배열 해체도 가능하다 - 출력:  N: 1 M: 3
print("N:", N, "M:", M)
arr = [int(input()) for _ in range(M)]
# 입력:
# 3
# 2
# 1
print(arr)  # 출력: [3, 2, 1]
