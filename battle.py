# Turn-based battles between two characters

from character import Character


class Battle:
    """Manages a turn-based battle between two characters"""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Initialise the Battle

        Args:
            hero (Character): The character that attacks first in each round.
            enemy (Character): The character that attacks second in each round.
        """
        self.hero = hero
        self.enemy = enemy
        self.rounds = 0

    def play_round(self) -> None:
        """Hero attacks enemy. If the enemy is still alive, the enemy attacks back."""
        self.rounds += 1
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self, max_rounds: int = 1000, verbose: bool = False) -> Character | None:
        """
        Play rounds until one of the characters is no longer alive.

        Args:
            max_rounds (int): Stop after this many rounds, in case neither character
                can hurt the other (default = 1000)
            verbose (bool): Print the HP of both characters after each round (default = False)

        Returns:
            Character | None: The winner, or None if the battle was stopped at max_rounds.
        """
        while self.hero.is_alive and self.enemy.is_alive and self.rounds < max_rounds:
            self.play_round()
            if verbose:
                print(f"Round {self.rounds}: {self.hero.name} {self.hero.hp} HP, "
                      f"{self.enemy.name} {self.enemy.hp} HP")
        return self.winner

    @property
    def winner(self) -> Character | None:
        """The character still alive when the other is dead, or None if both are alive."""
        if not self.enemy.is_alive:
            return self.hero
        if not self.hero.is_alive:
            return self.enemy
        return None

    def __repr__(self) -> str:
        """Representation of battle object"""
        return f"<Battle hero={self.hero.name} enemy={self.enemy.name} rounds={self.rounds}>"


if __name__ == "__main__":
    from character import Warrior, Mage

    hero = Warrior("Conan")
    enemy = Mage("Merlin")
    battle = Battle(hero, enemy)

    winner = battle.simulate_battle(verbose=True)
    print(f"\n{winner.name} wins after {battle.rounds} rounds!")