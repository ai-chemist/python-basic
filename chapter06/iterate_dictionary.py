# Iterate key-value
dict_0 = {
    'name' : 'NAME',
    'age' : 'AGE',
}

# items() 메서드 - key, value 순으로 할당
for key, value in dict_0.items():
    print("KEY :", key)
    print("VALUE :", value)

# Iterate key only
dict_1 = {
    'name' : 'NAME',
    'age' : 'AGE',
}

# keys() 메서드 사용
print("\n---keys()---")
for key in dict_1:
    print("KEY :", key)

# 순회 시 기본적으로 key 만 순회함
for name in dict_1:
    print(name)

# 순회 중 key를 통해 값에 접근
names = {
    'arthur' : 'c',
    'bell' : 'python',
    'edward' : 'ruby',
    'x' : 'assembly',
    'cavin' : 'c'
}

name_list = ['arthur', 'bell', 'carl', 'david']
for key in name_list:
    print(f"Hello, {name.title()}")

    if key in names:
        print(f"\t{key.title()} is in the names list. He(She) uses {names[key]}")

if 'carl' not in names.keys():
    print("Carl is not in the names list.")

# 순서에 따라 정렬 - 알파벳
print("\n---sorted()---")
for key in sorted(names.keys()):
    print(f"key's name : {key.title()}")

# 값 순회 - values() 메서드
print("\n---values()---")
for value in names.values():
    print(value.title())

# set(세트) - 중복이 없는 컬렉션, set()
    # set_name = {'a', 'b', 'c'} 의 형태로 세트 직접 생성 가능
print("\n---SET---")
for value in set(names.values()):
    print(value.title())