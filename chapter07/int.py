age = input("Please Enter Your Age : ")

# print(age > 10) - TypeError 발생

# int() 메서드를 통해 문자열을 정수형으로 바꿀 수 있음
age = int(age)

print(age > 10)

# int(input()) 같은 중첩 형태로 사용 가능
height = int(input("Please Enter Your Height : "))
print(height > 160)