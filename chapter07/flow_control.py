prompt = "\nHello! What are you doing?"
prompt += "\nEnter '0' to end the loop.\n"

# break 사용을 위해 무한 루프 생성
while True:
    message = input(prompt)

    if message == '0':
        break
    else:
        print(message)


# continue - 다음 루프로 이동
number = 0
while number < 20:
    number += 1
    if number % 2 == 0:
        continue
    else:
        print(number)