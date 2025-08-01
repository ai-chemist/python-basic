cars = ['audi', 'benz', 'porsche', 'bmw']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 동등 연산자 '==' 는 대소문자 구분
if 'a' == 'A':
    print("True")
else:
    print("False")

# 불일치 연산자 '!='
if 'a' != 'b':
    print("a is not b")

# 비교 연산자
print("<, >, <=, >= 연산자로 숫자 값 비교")

# 여러 조건 모두 True 일 때 - & 가 아닌 and 를 사용
if 'a' == 'a' and 'b' == 'b':
    print("AND")

# 여러 조건 중 하나만 True 여도 되는 경우 - | 가 아닌 or 사용
if 'a' == 'a' or 'b' != 'b':
    print("OR")

# 리스트 내부에 값이 존재하는지 확인 - in
print('bmw' in cars)

# 리스트 내부에 값이 없는지 확인 - not in
print('kia' not in cars)