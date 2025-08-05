# 프로그램의 실행 여부를 결정하는 변수 - 플래스(Flag)

prompt = f"It's time.\n"
prompt += "Enter '0' to end the program.\n"

# Flag로 사용할 active
active = True

while active:
    message = input(prompt)

    if message == '0':
        active = False
    else:
        print(message)