# 📝 복습 문제 3: 리스트 컴프리헨션을 이용하여 특정 문자 변형하기
# 문제 설명
# 리스트 컴프리헨션을 이용하여, 알파벳으로 된 이름의 특정 문자(e)만 2개로 늘려서 변형시키는 코드를 작성해 봅시다!

name = "Heybob"
new_name_list = list(map(lambda x: x * 2 if x == "e" else x, name))
# 람다식에서 if를 쓰면 무조건 else도 써야 한다.

new_name = "".join(new_name_list)
print(new_name)
