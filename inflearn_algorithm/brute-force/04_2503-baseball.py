# 숫자 야구  #2503

# 구하는 것: 조건의 맞는 모든 답의 개수
# 조건:
    # 숫자를 하나 설정
    # 답변의 숫자와 비교한다.
        # i가 숫자의 첫번째 자리에 있으면 스트라이크
        # j가 숫자의 두번째 자리에 있으면 스트라이크
        # k가 숫자의 세 번째 자리에 있으면 스트라이크

        # i가 숫자의 다른 자리에 있으면 볼
        # j가 숫자의 다른 자리에 있으면 볼
        # k가 숫자의 다른 자리에 있으면 볼
    # 비교하는 모든 숫자와 스트라이크와 볼 수가 일치하면 답으로 취급한다.

# 질문 개수: n
# 답변 개수: n


n = int(input()) # 몇 번 질문할 것인가
ary = [] # 답변을 저장

answer = 0
for _ in range(n):
    a = list(map(int, input().split()))
    ary.append(a)


for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if (i == j or j == k or k==i):  # 하나라도 같으면 고려하지 않는다.
                continue

            # 한가지 숫자가 정해져서 내려온다

            cnt = 0

            for E in ary:
                number = E[0]
                strike = E[1]
                ball = E[2]

                strike_cnt = 0
                ball_cnt = 0

                # 올 스트라이크
                if strike == 3:
                    answer = 1

                # # 스트라이크 & 볼 따로 계산
                # # 스트라이크 계산
                # if str(i) == str(number)[0]:
                #     strike_cnt += 1
                # if str(j) == str(number)[1]:
                #     strike_cnt += 1 
                # if str(k) == str(number)[2]:
                #     strike_cnt += 1
                
                # # 볼 계산
                # if str(i) == str(number)[1] or str(i) == str(number)[2]:
                #     ball_cnt += 1
                # if str(j) == str(number)[0] or str(j) == str(number)[2]:
                #     ball_cnt += 1
                # if str(k) == str(number)[0] or str(k) == str(number)[1]:
                #     ball_cnt += 1

                ### 스트라이크 & 볼 같이 계산
                if str(i) in str(number):
                    if str(i) == str(number)[0]:
                        strike_cnt += 1
                    else:
                        ball_cnt += 1

                if str(j) in str(number):
                    if str(j) == str(number)[1]:
                        strike_cnt += 1
                    else:
                        ball_cnt += 1  

                if str(k) in str(number):
                    if str(k) == str(number)[2]:
                        strike_cnt += 1
                    else:
                        ball_cnt += 1


                if ball == ball_cnt and strike == strike_cnt:
                    cnt += 1

                if cnt == n:
                    answer += 1  

print(answer)



