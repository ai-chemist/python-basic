responses = {}

active = True

while active:
    name = input("Name: ")
    response = input("Response: ")

    responses[name] = response

    repeat = input("If you want stop, please type 'n': ")
    if repeat == 'n':
        active = False

print("------")
for name, response in responses.items():
    print(name," : ", response)