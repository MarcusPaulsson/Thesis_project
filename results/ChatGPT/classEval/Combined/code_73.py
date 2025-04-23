class RPGCharacter:
    """
    Represents a role-playing game character capable of attacking, healing, gaining experience, leveling up, and checking if alive.
    """

    MAX_HP = 100
    LEVEL_UP_EXP_MULTIPLIER = 100
    HP_INCREASE_PER_LEVEL = 20
    ATTACK_POWER_INCREASE_PER_LEVEL = 5
    DEFENSE_INCREASE_PER_LEVEL = 5
    MAX_LEVEL = 100

    def __init__(self, name, hp, attack_power, defense, level=1):
        """
        Initialize an RPG character object.
        :param name: str, the name of the character.
        :param hp: int, initial health points of the character.
        :param attack_power: int, initial attack power of the character.
        :param defense: int, initial defense points of the character.
        :param level: int, initial level of the character. Default is 1.
        """
        self.name = name
        self.hp = min(hp, self.MAX_HP)  # Ensure HP does not exceed MAX_HP
        self.attack_power = attack_power
        self.defense = defense
        self.level = min(level, self.MAX_LEVEL)  # Ensure level does not exceed MAX_LEVEL
        self.exp = 0

    def attack(self, other_character):
        """
        Attack another character, calculating damage based on attack power and defense.
        :param other_character: RPGCharacter, the character being attacked.
        """
        damage = max(0, self.attack_power - other_character.defense)
        other_character.hp = max(0, other_character.hp - damage)

    def heal(self):
        """
        Heal the character by 10 HP, not exceeding MAX_HP.
        :return: int, current health points after healing.
        """
        self.hp = min(self.MAX_HP, self.hp + 10)
        return self.hp

    def gain_exp(self, amount):
        """
        Gain experience points and level up if enough experience is accumulated.
        :param amount: int, the amount of experience points to gain.
        """
        self.exp += amount
        while self.exp >= self.LEVEL_UP_EXP_MULTIPLIER * self.level and self.level < self.MAX_LEVEL:
            self.exp -= self.LEVEL_UP_EXP_MULTIPLIER * self.level
            self.level_up()

    def level_up(self):
        """
        Level up the character, increasing HP, attack power, and defense.
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense after leveling up.
        """
        if self.level < self.MAX_LEVEL:
            self.level += 1
            self.hp = min(self.MAX_HP, self.hp + self.HP_INCREASE_PER_LEVEL)
            self.attack_power += self.ATTACK_POWER_INCREASE_PER_LEVEL
            self.defense += self.DEFENSE_INCREASE_PER_LEVEL
        self.exp = 0
        return self.level, self.hp, self.attack_power, self.defense

    def is_alive(self):
        """
        Check if the character is alive.
        :return: True if HP is greater than 0, False otherwise.
        """
        return self.hp > 0