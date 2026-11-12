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


class Warrior(Character):
    """A defensive specialist whose armor reduces all incoming damage"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None, armor: int = 5) -> None:
        """
        Initialise the Warrior

        Args:
            name, hp_max, damage, weapon: Same as for Character.
            armor (int): Amount subtracted from all incoming damage (default = 5)

        Raises:
            ValueError: If armor is negative.
        """
        if armor < 0:
            raise ValueError(f"armor cannot be negative, got {armor}")
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """Reduce the incoming damage by armor, then take the rest as normal."""
        super().take_damage(amount - self.armor)  # Character.take_damage turns negative damage into 0

    def __repr__(self) -> str:
        """Representation of warrior object"""
        return (f"<Warrior name={self.name} hp={self.hp} damage={self.damage} "
                f"weapon={self.weapon} armor={self.armor}>")

    def __str__(self) -> str:
        """String representation of warrior object"""
        return f"Warrior: {self.name} with {self.hp} HP, {self.damage} damage and {self.armor} armor"


class Mage(Character):
    """A resource-based attacker who uses mana to cast spells"""

    SPELL_COST = 10     # Mana spent on one spell
    MANA_RESTORE = 5    # Mana restored by a base attack

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None, mana: int = 30, mana_max: int = 30) -> None:
        """
        Initialise the Mage

        Args:
            name, hp_max, damage, weapon: Same as for Character.
            mana (int): Mana the mage starts with (default = 30)
            mana_max (int): Max mana (default = 30)

        Raises:
            ValueError: If mana is not between 0 and mana_max.
        """
        if not 0 <= mana <= mana_max:
            raise ValueError(f"mana must be between 0 and mana_max ({mana_max}), got {mana}")
        super().__init__(name, hp_max, damage, weapon)
        self._mana = mana  # Protected, like _hp, so mana stays between 0 and mana_max
        self.mana_max = mana_max

    def attack(self, target) -> None:
        """
        Cast a spell if there is enough mana, otherwise use the base attack.

        Spell (mana >= 10): spend 10 mana and deal double base damage. Weapons are not used.
        Base attack (mana < 10): attack as a normal Character (with weapon if equipped),
        and restore 5 mana.
        """
        if self._mana >= self.SPELL_COST:
            self._mana -= self.SPELL_COST
            target.take_damage(2 * self.damage)
        else:
            super().attack(target)
            self._mana = min(self._mana + self.MANA_RESTORE, self.mana_max)

    @property
    def mana(self) -> int:
        """Public read-only property to inspect mana."""
        return self._mana

    def __repr__(self) -> str:
        """Representation of mage object"""
        return (f"<Mage name={self.name} hp={self.hp} damage={self.damage} "
                f"weapon={self.weapon} mana={self.mana}/{self.mana_max}>")

    def __str__(self) -> str:
        """String representation of mage object"""
        return (f"Mage: {self.name} with {self.hp} HP, {self.damage} damage "
                f"and {self.mana}/{self.mana_max} mana")


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