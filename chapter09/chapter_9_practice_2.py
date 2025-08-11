from random import randint

class Dice:
    """Dice Class"""

    def __init__(self, sides=6):
        """Dice constructor"""
        self.sides = sides

    def roll(self):
        """Roll dice"""
        print(randint(1, self.sides))


dice_8 = Dice(8)
dice_20 = Dice(20)

dice_8.roll()
dice_20.roll()