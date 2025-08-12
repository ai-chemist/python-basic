while True:
    print("Enter 'q' to quit")
    number = input("Enter your number")
    if number == 'q':
        break
    try:
        number = int(number)
    except ValueError:
        print("Please enter a number")
    else:
        print("You entered", number)