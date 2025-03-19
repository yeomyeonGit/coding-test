# 이진 ㅊ탐색 문제는 입력 데이터가 많거나 탐색 범위가 매우 넓은 편이어서 빠르게 입력 받는 것이 중요함
# 입력 데이터가 많은 문제는 sys 라이브러리의 readline() 함수를 이용하면 됨

import sys

input_data = sys.stdin.readline().rstrip()
print(input_data)