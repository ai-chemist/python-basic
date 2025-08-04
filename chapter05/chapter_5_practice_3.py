users = ['admin', 'bob', 'carl', 'damon', 'edwin']
current_users = ['allan', 'BOB', 'cake', 'dragon', 'el grande americano']
currents = []

for current_user in current_users:
    currents.append(current_user.lower())
if users:
    for user in users:
        if user.lower() in currents:
            print(f"You can't use this name : {user}")
        else:
            if user == 'admin':
                print(f"{user} is an admin")
            else:
                print(f"hello {user}!")
else:
    print("empty list")