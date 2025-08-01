# 튜플 내부의 값은 변하지 않는다

dimensions = (200, 300)
print(dimensions[0])
print(dimensions[1])
print(dimensions)

for dimension in dimensions:
    print(dimension)

# 튜플 전체의 값을 재정의하여 값 변경 - tuple[0] = 123 같은 형태는 불가
dimensions = (500, 600)
print("It's changed")
for dimension in dimensions:
    print(dimension)