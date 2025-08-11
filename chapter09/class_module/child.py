"""Human 상속"""
from human import Human

class Child(Human):
    """Child Class"""

    def __init__(self, name, age, gender, parent='No'):
        super().__init__(name, age, gender)
        self.parent = parent

    def get_parent(self):
        return self.parent