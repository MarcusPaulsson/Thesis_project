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
        :param hp: int, the health points of the character.
        :param attack_power: int, the attack power of the character.
        :param defense: int, the defense points of the character.
        :param level: int, the level of the character. Default is 1.
        """
        self.name = name
        self.hp = min(hp, self.MAX_HP)  # Ensure initial HP does not exceed max HP
        self.attack_power = attack_power
        self.defense = defense
        self.level = min(level, self.MAX_LEVEL)  # Ensure level does not exceed max level
        self.exp = 0

    def attack(self, other_character):
        """
        Attack another character. The damage caused needs to offset the defense value.
        :param other_character: RPGCharacter, The character being attacked.
        """
        if not isinstance(other_character, RPGCharacter):
            raise ValueError("other_character must be an instance of RPGCharacter")
        
        damage = max(0, self.attack_power - other_character.defense)
        other_character.hp = max(0, other_character.hp - damage)

    def heal(self):
        """
        Heal the character with 10 hp and the max hp is 100.
        :return: int, the current health points after healing.
        """
        self.hp = min(self.MAX_HP, self.hp + 10)
        return self.hp

    def gain_exp(self, amount):
        """
        Gain experience points for the character and level up when the exp has reached the values that is 100 times the current level.
        The experience that overflows should be used to calculate the next level up until exhausted.
        :param amount: int, the amount of experience points to gain.
        """
        self.exp += amount
        while self.exp >= 100 * self.level and self.level < self.MAX_LEVEL:
            self.exp -= 100 * self.level
            self.level_up()

    def level_up(self):
        """
        Level up the character and return to zero experience points, increase hp by 20 points, attack power and defense points by 5 points.
        Max level is 100.
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        """
        if self.level < self.MAX_LEVEL:
            self.level += 1
            self.hp = min(self.MAX_HP, self.hp + 20)  # Ensure HP does not exceed max HP
            self.attack_power += 5
            self.defense += 5
        return (self.level, self.hp, self.attack_power, self.defense)

    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        """
        return self.hp > 0