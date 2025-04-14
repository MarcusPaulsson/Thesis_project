class RPGCharacter:
    """
    The class represents a role-playing game character, which allows to attack other characters, heal, gain experience, level up, and check if the character is alive.
    """

    MAX_HP = 100
    LEVEL_UP_THRESHOLD = 100
    MAX_LEVEL = 100
    HEAL_AMOUNT = 10
    LEVEL_UP_HP_INCREASE = 20
    LEVEL_UP_STAT_INCREASE = 5

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
        damage = self.attack_power - other_character.defense
        if damage > 0:
            other_character.hp -= damage

    def heal(self):
        """
        Heal the character.
        :return: int, the current health points after healing.
        """
        self.hp = min(self.hp + self.HEAL_AMOUNT, self.MAX_HP)
        return self.hp

    def gain_exp(self, amount):
        """
        Gain experience points for the character and level_up when the exp has reached the values that is 100 times the current level
        The experience that overflows should be used to calculate the next leve up untill exhausts
        :param amount: int, the amount of experience points to gain.
        """
        self.exp += amount
        while self.exp >= self.LEVEL_UP_THRESHOLD * self.level:
            if self.level < self.MAX_LEVEL:
                self.level_up()
            else:
                self.exp = 0
                break

    def level_up(self):
        """
        Level up the character and return to zero experience points, increase hp by 20 points, attack power and defense points by 5 points.
        """
        if self.level < self.MAX_LEVEL:
            self.level += 1
            self.hp += self.LEVEL_UP_HP_INCREASE
            self.attack_power += self.LEVEL_UP_STAT_INCREASE
            self.defense += self.LEVEL_UP_STAT_INCREASE
            self.exp = 0

    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        """
        return self.hp > 0