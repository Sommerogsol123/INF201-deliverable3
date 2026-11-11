# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

from items import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon | None): Equipped weapon (default = None, no weapon)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, amount: int) -> None:
        """Reduce own HP by amount. HP cannot go below 0."""
        amount = max(amount, 0)              # Negative damage should not heal
        self._hp = max(self._hp - amount, 0)

    def heal(self, amount: int) -> None:
        """Increase own HP by amount. HP cannot exceed hp_max."""
        amount = max(amount, 0)                          # Negative healing should not hurt
        self._hp = min(self._hp + amount, self.hp_max)

    def attack(self, target) -> None:
        """Attack target. Uses the weapon's dice if a weapon is equipped, otherwise base damage."""
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.damage
        target.take_damage(damage)

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage} weapon={self.weapon}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only property: True if the character has HP left, otherwise False."""
        return self._hp > 0


if __name__ == "__main__":
    from dice import Dice

    sword = Weapon("Sword", Dice(sides=12))
    knight = Character("Knight", weapon=sword)
    farmer = Character("Farmer")

    print(repr(knight))
    print(repr(farmer))

    # Knight uses the sword: damage varies between 1 and 12
    for _ in range(5):
        target = Character("Dummy")
        knight.attack(target)
        print("Knight deals", 100 - target.hp, "damage")

    # Farmer has no weapon: damage is always 10
    target = Character("Dummy")
    farmer.attack(target)
    print("Farmer deals", 100 - target.hp, "damage")