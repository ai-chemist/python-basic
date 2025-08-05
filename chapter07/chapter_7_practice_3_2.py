prompt = "If you can visit one city, where would you go? :"
prompt += "\n(press 'n' to stop)"

active = True

while active:
    response = input(prompt)
    if response == 'n':
        active = False
    else:
        print("Good City :", response)