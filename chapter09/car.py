class Car:
    """Car class docstring"""

    def __init__(self, make, model, year):
        """생성자"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """설명 반환"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_car = Car("ford", "mustang", 1999)
print(my_car.get_descriptive_name())