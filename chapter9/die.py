from random import randint


class Die:
    """Simple attempt to roll a dice"""

    def __init__(self, sides=6):
        """Initialize class attributes"""
        self.sides = sides

    def roll_die(self):
        """Prints a random number between 1 and n"""
        rand_number = randint(1, self.sides)
        print("\nRolling dice..")
        print(f"Number is {rand_number}")


# rolling_dice = Die()
# rolling_dice.roll_die()
# rolling_dice.roll_die()
# rolling_dice.roll_die()
# rolling_dice.roll_die()
# rolling_dice.roll_die()
# rolling_dice.roll_die()

print("\n10-sided die")
rolling_dice_10 = Die(10)
for side in range(1,21):
    rolling_dice_10.roll_die()

