# Items that characters can hold

from dice import Dice


class Weapon:
    """A weapon that deals damage based on a dice roll"""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon

        Args:
            name (str): The name of the weapon.
            damage_dice (Dice): The dice that is rolled to decide the damage.
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the weapon's dice and return the damage"""
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        """Representation of weapon object"""
        return f"Weapon(name={self.name}, damage_dice={self.damage_dice})"


if __name__ == "__main__":
    sword = Weapon("Sword", Dice(sides=12))
    print(sword)
    print([sword.roll_damage() for _ in range(10)])