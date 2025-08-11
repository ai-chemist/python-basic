class Restaurant:
    """Restaurant class docstring"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}\nRestaurant cuisine_type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.name} is open")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increase_number_served(self, number_served):
        self.number_served += number_served



res_0 = Restaurant("Chicken", "Soft")
res_1 = Restaurant("Beef", "Hard")
res_2 = Restaurant("Pork", "Soft")

res_0.describe_restaurant()
res_1.describe_restaurant()
res_2.describe_restaurant()

# practice 9-4
restaurant = Restaurant("Chicken", "Hard")

print(restaurant.number_served)

restaurant.set_number_served(30)
print(restaurant.number_served)

restaurant.increase_number_served(70)
print(restaurant.number_served)