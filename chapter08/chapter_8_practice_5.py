def make_sandwich(bread, *args):
    print(f"Bread: {bread}")
    for arg in args:
        print(f"topping: {arg}")

make_sandwich('milk', 'bacon')
make_sandwich('milk', 'bacon', 'cheese')
make_sandwich('shio butter')