current = 1

# while 조건 - while 문으로 조건에 맞는 한 반복
while current <= 7:
    print(current)
    current += 1

prompt = "\nHello! What are you doing?"
prompt += "\nEnter '0' to end the program.\n"

message = ""
while message != "0":
    message = input(prompt)
    if message != "0":
        print("Typed : ", message)