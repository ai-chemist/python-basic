from name_function import get_upper_name

print("Enter 'q' to quit")
while True:
    first = input("Enter your first name: ")
    if first == "q":
        break
    last = input("Enter your last name: ")
    if last == "q":
        break

    upper_name = get_upper_name(first, last)
    print(f"Upper Name: {upper_name}")