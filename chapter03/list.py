# List : [대괄호] 로 표현, 요소를 콤마로 구분

# List 이름은 복수형으로 짓는 관례
vehicles = ['car', 'bicycle', 'airplane']

# 출력 시 [대괄호] 포함된 형태로 출력
print(vehicles)

# 요소에 접근 시에는 [index] 를 사용하여 접근
print(vehicles[0].title())

# 음수를 활용 해 List 마지막부터 요소 접근
print(vehicles[-1].upper())

# f"{}" 사용 가능
print(f"This is Vehicle : {vehicles[-3].title()}")