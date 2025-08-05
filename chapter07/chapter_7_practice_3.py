sandwich_orders = ['avocado', 'tuna', 'fried', 'chicken', 'fried', 'fried']
finished = []

while 'fried' in sandwich_orders:
    sandwich_orders.remove('fried')
    print("No fried")

while sandwich_orders:
    order = sandwich_orders.pop()
    print("Ordered :", order)
    finished.append(order)