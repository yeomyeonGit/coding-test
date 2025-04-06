# 인풋 예시 'ATCBA' => 아웃풋 예시 False
# 인풋 예시 'abba' => 아웃풋 예시 True


# 반복문으로 풀기
def isPalindrome_for(s):
    n = len(s)
    s = s.upper()

    for i in range((n // 2) + 1):
        if s[i] != s[-(i + 1)]:
            return False
        return True


res = isPalindrome_for("egge")
print(res)


# 재귀함수로 풀기
# 메모리 사용 비효율적임
# 새로운 배열을 만들게 됨


def isPalindrome_recur(s):
    isFlag = True
    if len(s) <= 1:
        return isFlag

    if s[0] != s[-1]:
        isFlag = False
        return isFlag
    else:
        # 메모리 사용 비효율
        # 왜냐하면 새로운 배열을 만들기 때문
        res = isPalindrome_recur(s[1:-1])
    return res


res = isPalindrome_recur("hello")
print(res)
