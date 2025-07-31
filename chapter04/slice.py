# 슬라이스 - 리스트의 일부분, a to b-1
names = ['arthur', 'bob', 'carl', 'daren', 'east']
print(names[0:3])
print(names[1:4])

# 첫 인덱스 생략 시 0
print(names[:4])

# 마지막 인덱스 생략 시 끝까지
print(names[2:])

# 음수 인덱스 - -n to last
print(names[-2:])

# 슬라이스 for 문
for name in names[:4]:
    print(name.title())

# 리스트 복사 - [:]
drinks = ['coke', 'jack daniels', 'milk', 'coffee']
favorite = drinks[:]

drinks.append('water')
favorite.append('ade')

print(drinks)
print(favorite)

# 복사가 아닌 경우 - 직접 할당 시 같은 주소를 참조하여 값 변환이 같이 이루어짐
foods = ['pork', 'beef', 'chicken']
steaks = foods

foods.append('duck')
steaks.append('sheep')

print(foods)
print(steaks)