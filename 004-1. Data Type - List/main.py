﻿# 리스트를 만들어 보자
# 타 언어에서의 배열이라고 생각하면 된다
_list = [1, 2, 3, 4]
# 파이썬의 리스트는 여러가지 자료형이 올 수 있다
_list = [1, 2, 3.5, 'hello']
# 리스트의 한 요소가 리스트일 수도 있다
_list = [1, 2, ['hello', 'hi'], 3]

# 인덱싱 가능
print(_list[2])
print(_list[-1])
# 리스트 안의 리스트는 2번 접근하자
print(_list[2][1])

# 슬라이싱도 가능
print(_list[0:3])

# 리스트나 문자열이나 문법적인 부분은 많이 닮아 있다
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(list_a + list_b)
print(list_a * 2)

# 리스트는 추가하고 수정하고 삭제할 수 있어야 할 것이다
# 그냥 리스트를 붙여 보자
list_a += [4]
# append를 쓰는 방법도 있다
list_a.append(5)
print(list_a)

# 수정은 인덱싱으로 접근해서 값을 바꾸면 된다
list_a[3] = 5
# 수정도 슬라이싱 방식으로 할 수 있다. 정확히는 치환이다
list_a[0:3] = [3, 4, 1, 4, 5, 6]
# 치환이기 때문에 굳이 슬라이싱 범위와 리스트 갯수를 맞추지 않아도 된다
# 0, 1, 2번째 인덱스의 요소들이 위의 리스트로 치환될 것이다
print(list_a)

# 삭제는 del 함수를 사용한다
del list_a[-3:-1]
print(list_a)

# 리스트와 뒤에서 배울 dictionary, tuple 등은 iterable 객체이다
# 파이썬에서 iterable(반복 가능한) 객체는 굉장히 특별한데, unpack이라는 개념을 알고 있으면 좋다
a, b, c, d = [1, 2, 3, 4]
print(a, b, c, d)
