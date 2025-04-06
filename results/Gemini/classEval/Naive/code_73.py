class RPGCharacter:
    """
    The class represents a role-playing game character, which allows to attack other characters, heal, gain experience, level up, and check if the character is alive.
    """

    MAX_HP = 100
    MAX_LEVEL = 100

    def __init__(self, name, hp, attack_power, defense, level=1):
        """
        Initialize an RPG character object.
        :param name: str, the name of the character.
        :param hp: int, The health points of the character.
        :param attack_power: int, the attack power of the character.
        :param defense: int, the defense points of the character.
        :param level: int, the level of the character. Default is 1.
        """
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = 0

    def attack(self, other_character):
        """
        Attack another character. The damage caused needs to offset the defense value.
        :param other_character: RPGCharacter, The character being attacked.
        """
        damage = max(0, self.attack_power - other_character.defense)
        other_character.hp = max(0, other_character.hp - damage)

    def heal(self):
        """
        Heal the character with 10 hp and the max hp is 100.
        :return: int, the current health points after healing.
        """
        self.hp = min(RPGCharacter.MAX_HP, self.hp + 10)
        return self.hp

    def gain_exp(self, amount):
        """
        Gain experience points for the character and level_up when the exp has reached the values that is 100 times the current level
        The experience that overflows should be used to calculate the next leve up untill exhausts
        :param amount: int, the amount of experience points to gain.
        """
        self.exp += amount
        threshold = self.level * 100
        while self.exp >= threshold and self.level < RPGCharacter.MAX_LEVEL:
            self.exp -= threshold
            self.level_up()
            threshold = self.level * 100

    def level_up(self):
        """
        Level up the character and return to zero experience points, increase hp by 20 points, attack power and defense points by 5 points.
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        """
        if self.level < RPGCharacter.MAX_LEVEL:
            self.level += 1
            self.hp += 20
            self.attack_power += 5
            self.defense += 5
        return (self.level, self.hp, self.attack_power, self.defense)

    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        """
        return self.hp > 0


if __name__ == '__main__':
    # Example Usage and Docstring Tests (using doctest)
    import doctest

    doctest.testmod()

    # Example Usage (Manual)
    player_1 = RPGCharacter('Hero', 100, 20, 10)
    player_2 = RPGCharacter('Villain', 80, 15, 5)

    print(f"{player_1.name}: HP = {player_1.hp}, Level = {player_1.level}")
    print(f"{player_2.name}: HP = {player_2.hp}, Level = {player_2.level}")

    player_1.attack(player_2)
    print(f"{player_2.name} HP after attack: {player_2.hp}")

    player_1.gain_exp(150)
    print(f"{player_1.name} Level after gaining experience: {player_1.level}, EXP: {player_1.exp}")

    player_1.heal()
    print(f"{player_1.name} HP after healing: {player_1.hp}")

    print(f"{player_1.name} is alive: {player_1.is_alive()}")
    player_2.hp = 0
    print(f"{player_2.name} is alive: {player_2.is_alive()}")