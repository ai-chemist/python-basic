print("A / B\n Enter 'q' to Quit")

while True:
    first = input("First: ")
    if first == 'q':
        break
    second = input("Second: ")
    if second == 'q':
        break
    try:
        answer = int(first) / int(second)
    except ZeroDivisionError:
        print("You can't divide by 0")
    # try 성공 시 else로 넘어옴
    else:
        print(answer)