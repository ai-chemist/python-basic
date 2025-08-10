class Restaurant:
    """Restaurant class docstring"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}\nRestaurant cuisine_type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.name} is open")

res_0 = Restaurant("Chicken", "Soft")
res_1 = Restaurant("Beef", "Hard")
res_2 = Restaurant("Pork", "Soft")

res_0.describe_restaurant()
res_1.describe_restaurant()
res_2.describe_restaurant()