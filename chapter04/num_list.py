# range(a, b) - a to b-1
for value in range(1, 11):
    print(value)

# list() - 내부 값을 리스트로 반환
num_list = list(range(1, 9))
print(num_list)

# range() - 3번째 인수는 건너뛰는 값
# 2 to 10 - 2씩 증가
even_list = list(range(2, 11, 2))
print(even_list)

# 제곱수 리스트
squares = []
for value in range(1, 11):
    # square = value ** 2
    # squares.append(square)
    squares.append(value ** 2)

print(squares)

# 리스트 내포 [표현식 for a in 범위]
square_list = [value ** 2 for value in range(1, 11)]
print(square_list)

# min, max, sum 함수
print(min(square_list))
print(max(square_list))
print(sum(square_list))