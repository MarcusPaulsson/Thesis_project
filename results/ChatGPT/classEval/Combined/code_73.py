class RPGCharacter:
    """
    The class represents a role-playing game character, allowing to attack other characters,
    heal, gain experience, level up, and check if the character is alive.
    """
    
    MAX_HP = 100
    LEVEL_UP_EXP_MULTIPLIER = 100
    HP_INCREASE = 20
    ATTACK_POWER_INCREASE = 5
    DEFENSE_INCREASE = 5
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
        self.hp = min(hp, self.MAX_HP)
        self.attack_power = attack_power
        self.defense = defense
        self.level = min(level, self.MAX_LEVEL)
        self.exp = 0

    def attack(self, other_character):
        """
        Attack another character. The damage caused needs to offset the defense value.
        :param other_character: RPGCharacter, the character being attacked.
        """
        damage = max(self.attack_power - other_character.defense, 0)
        other_character.hp = max(other_character.hp - damage, 0)

    def heal(self):
        """
        Heal the character with 10 hp and the max hp is 100.
        :return: int, the current health points after healing.
        """
        self.hp = min(self.hp + 10, self.MAX_HP)
        return self.hp

    def gain_exp(self, amount):
        """
        Gain experience points for the character and level up when the exp has reached
        the values that is 100 times the current level.
        :param amount: int, the amount of experience points to gain.
        """
        self.exp += amount
        while self.exp >= self.level * self.LEVEL_UP_EXP_MULTIPLIER and self.level < self.MAX_LEVEL:
            self.exp -= self.level * self.LEVEL_UP_EXP_MULTIPLIER
            self.level_up()

    def level_up(self):
        """
        Level up the character and reset experience points, increase hp, attack power and defense points.
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        """
        if self.level < self.MAX_LEVEL:
            self.level += 1
            self.hp = min(self.hp + self.HP_INCREASE, self.MAX_HP)
            self.attack_power += self.ATTACK_POWER_INCREASE
            self.defense += self.DEFENSE_INCREASE
        return self.level, self.hp, self.attack_power, self.defense

    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        """
        return self.hp > 0