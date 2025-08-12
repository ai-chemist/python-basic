# 원주율 내부에 생일 찾기
from pathlib import Path

birthday = input("Enter birthday: ")

path = Path('pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for c in contents:
    pi_string += c

message = ''
if birthday in pi_string:
    message = "Your birthday is in the pi"
else:
    message = "Your birthday is not in the pi"

# replace() - _old to _new 로 변경하는 메서드
message = message.replace('pi', 'PI')

print(message)