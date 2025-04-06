# 재귀함수란?
# 함수 정의 내에서 자기 자신을 호출

# 예시: 카운트다운 함수

# 1. 종료 조건
# 2-1. 재귀 호출
# 2-2. 데이터 통합

def countdown(n):

    # 종료 조건
    if n == 1:
        return '1 end!'
    
    # 재귀 호출, '재귀 데이터를 받음'
    recur_out = countdown(n-1)
    
    # 현재 데이터
    cur_out = str(n)

    # 결과 통합
    combo_out = cur_out + ', ' + recur_out

    # 지금 만든 데이터를 다시 '재귀 데이터'로 만들어줌
    return combo_out

print(countdown(5))

# 자기 자신을 호출하는 것으로 인해 반복 발생 