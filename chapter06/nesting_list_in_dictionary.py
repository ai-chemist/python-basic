cake = {
    'base' : 'white',
    'toppings' : ['strawberry', 'blueberry'],
}

print(f"Ordered Cake : {cake['base'].title()}")

for topping in cake['toppings']:
    print(f"\ttopping : {topping}")

print("---")
bread_orders = {
    'john' : ['white', 'chocolate', 'green been', 'mushroom'],
    'mac' : ['truffle', 'chocolate', 'plain'],
    'arthur' : ['truffle', 'rice', 'shio butter'],
    'x' : ['chocolate'],
}
for order, breads in bread_orders.items():
    print(f"Orderer : {order}")
    if len(breads) <= 1:
        print(f"\tA bread : {breads[0]}")
    else:
        for bread in breads:
            print(f"\tbreads : {bread}")