# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage

    def take_damage(self, amount: int) -> None:
        """Reduce own HP by amount. HP cannot go below 0."""
        amount = max(amount, 0)              # Negative damage should not heal
        self._hp = max(self._hp - amount, 0)

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        target._hp -= self.damage
        target._hp = max(target._hp, 0)  # Target hp cannot end up lower than 0

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp


if __name__ == "__main__":
    c = Character("Test")
    c.take_damage(30)
    print(c.hp)          # forventer 70
    c.take_damage(500)
    print(c.hp)          # forventer 0
    c.take_damage(-10)
    print(c.hp)          # forventer 0