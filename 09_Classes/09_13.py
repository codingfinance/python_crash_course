# Dice

from random import randint, choice

class Dice:
    def __init__(self, sides):

        self.sides = sides

    def roll_die(self):

        side = choice(self.sides)
        return side


d1 = Dice(sides=[1,2,3,4,5,6])
for i in range(10):
    print(f"Die roll is {d1.roll_die()}")

