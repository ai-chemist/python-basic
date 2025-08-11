"""다른 모듈에서 클래스 가져옴"""
# import human - human. 으로 사용 가능
# from 모듈명 import * - 모든 요소 import 가능
# 모듈에서 모듈 import 가능, as 를 통한 별칭 지정 가능
from human import Human, User
from child import Child as Ch

my_new_human = Human('Adam', 'Rose', 'Man')
print(my_new_human.get_profile())

my_new_human.grade = 80
my_new_human.get_grade()

my_user = User('Ad', 'Zeren', 'Man')
print(my_user.uid.get_uid())

my_child = Ch('name', 3, 'woman', 'Parent')
print(my_child.get_parent())