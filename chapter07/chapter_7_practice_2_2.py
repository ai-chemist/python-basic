while True:
    age = int(input("Enter your age : "))
    if age == 0:
        break
    elif age < 3:
        print("Free")
    elif age < 12:
        print("$10")
    elif age >= 12:
        print("$15")