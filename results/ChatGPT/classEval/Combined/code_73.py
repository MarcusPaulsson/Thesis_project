class RPGCharacter:
    """
    Represents a role-playing game character capable of attacking, healing, gaining experience,
    leveling up, and checking if the character is alive.
    """

    MAX_HP = 100
    MAX_LEVEL = 100
    EXP_PER_LEVEL = 100

    def __init__(self, name, hp, attack_power, defense, level=1):
        """
        Initialize an RPG character object.
        :param name: str, the name of the character.
        :param hp: int, initial health points of the character.
        :param attack_power: int, attack power of the character.
        :param defense: int, defense points of the character.
        :param level: int, level of the character, default is 1.
        """
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = 0

    def attack(self, other_character):
        """
        Attack another character, calculating damage based on defense.
        :param other_character: RPGCharacter, the character being attacked.
        """
        damage = max(0, self.attack_power - other_character.defense)
        other_character.hp = max(0, other_character.hp - damage)

    def heal(self):
        """
        Heal the character by 10 HP with a maximum HP cap of 100.
        :return: int, the current health points after healing.
        """
        self.hp = min(self.MAX_HP, self.hp + 10)
        return self.hp

    def gain_exp(self, amount):
        """
        Gain experience points and level up when the experience exceeds threshold.
        :param amount: int, the amount of experience points to gain.
        """
        self.exp += amount
        while self.exp >= self.EXP_PER_LEVEL * self.level and self.level < self.MAX_LEVEL:
            self.level_up()

    def level_up(self):
        """
        Level up the character, resetting experience and increasing stats.
        :return: tuple[int, int, int, int], new level, health points, attack power, defense points after leveling up.
        """
        if self.level < self.MAX_LEVEL:
            self.level += 1
            self.hp = min(self.MAX_HP, self.hp + 20)
            self.attack_power += 5
            self.defense += 5
            self.exp = 0
        return self.level, self.hp, self.attack_power, self.defense

    def is_alive(self):
        """
        Check if the character is alive.
        :return: True if health points are greater than 0, False otherwise.
        """
        return self.hp > 0