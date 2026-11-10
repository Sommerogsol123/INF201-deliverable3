# Dice class for the battle simulator
# INF201 Deliverable 3, Task 2

import random


class Dice:
    """Represents an n-sided dice used to add randomness to the game"""

    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the Dice

        Args:
            sides (int): Number of sides on the dice, must be at least 2 (default = 6)

        Raises:
            TypeError: If sides is not an integer.
            ValueError: If sides is less than 2.
        """
        if not isinstance(sides, int):
            raise TypeError(f"sides must be an integer, got {type(sides).__name__}")
        if sides < 2:
            raise ValueError(f"A dice must have at least 2 sides, got {sides}")
        self._sides = sides  # Protected, so sides cannot be changed to an invalid value later

    @property
    def sides(self) -> int:
        """Public read-only property to inspect the number of sides."""
        return self._sides

    def roll(self) -> int:
        """Roll the dice and return a random integer from 1 to sides (both included)."""
        return random.randint(1, self.sides)

    def __call__(self) -> int:
        """Roll the dice by calling the object directly, so d20() does the same as d20.roll()."""
        return self.roll()

    def __repr__(self) -> str:
        """Representation of dice object"""
        return f"Dice(sides={self.sides})"


if __name__ == "__main__":
    d6 = Dice()
    d20 = Dice(sides=20)

    print(d6, d20)                       # expect Dice(sides=6) Dice(sides=20)
    print(d6.roll(), d20.roll())         # expect a number 1-6 and a number 1-20
    print(d20())                         # __call__: expect a number 1-20
