from random import randint

class Lottery:
    """Lottery docstring"""

    def __init__(self):
        """Constructor"""
        self.correct_nums = [randint(1, 5) for i in range(1, 5)]

    def spin(self, num):
        if num in self.correct_nums:
            result = 's'
        else:
            result = 'n'
        return result

lotto = Lottery()
count = 0
while True:
    count += 1
    spin_nums = randint(1, 5)
    res = lotto.spin(spin_nums)

    if res == 's':
        print("Congratulations! You win!")
        break
    elif res == 'n':
        print("Sorry, you lose!")

print(f"You tried {count} times!")