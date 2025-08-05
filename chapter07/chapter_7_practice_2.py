active = True
toppings = []

prompt = "What do you want?"
prompt += "\nEnter '0' to end the loop.\n"

while active:
    topping = input(prompt)
    if topping == '0':
        active = False
    else:
        toppings.append(topping)

for topping in toppings:
    print("Topping :", topping)