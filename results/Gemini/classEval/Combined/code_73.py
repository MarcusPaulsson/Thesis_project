class RPGCharacter:
    """
    Represents a role-playing game character with capabilities for attacking, healing, gaining experience, leveling up, and checking life status.
    """

    MAX_HP = 100
    LEVEL_UP_HP_INCREASE = 20
    LEVEL_UP_STAT_INCREASE = 5
    EXP_PER_LEVEL = 100
    MAX_LEVEL = 100

    def __init__(self, name, hp, attack_power, defense, level=1):
        """
        Initializes a new RPG character.

        Args:
            name (str): The character's name.
            hp (int): The character's initial health points.
            attack_power (int): The character's attack power.
            defense (int): The character's defense.
            level (int, optional): The character's starting level. Defaults to 1.
        """
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = 0

    def attack(self, other_character):
        """
        Attacks another character, reducing their health based on the attacker's attack power and the defender's defense.

        Args:
            other_character (RPGCharacter): The character being attacked.
        """
        damage = max(0, self.attack_power - other_character.defense)
        other_character.hp -= damage

    def heal(self):
        """
        Heals the character, restoring up to 10 health points, but not exceeding the maximum health.
        """
        self.hp = min(self.MAX_HP, self.hp + 10)

    def gain_exp(self, amount):
        """
        Gains experience points and levels up the character if enough experience is accumulated.

        Args:
            amount (int): The amount of experience points to gain.
        """
        self.exp += amount
        while self.exp >= self.EXP_PER_LEVEL * self.level and self.level < self.MAX_LEVEL:
            self.exp -= self.EXP_PER_LEVEL * self.level
            self.level_up()

    def level_up(self):
        """
        Levels up the character, increasing their level, health, attack power, and defense.
        """
        if self.level < self.MAX_LEVEL:
            self.level += 1
            self.hp += self.LEVEL_UP_HP_INCREASE
            self.attack_power += self.LEVEL_UP_STAT_INCREASE
            self.defense += self.LEVEL_UP_STAT_INCREASE
            self.exp = 0

    def is_alive(self):
        """
        Checks if the character is alive.

        Returns:
            bool: True if the character's health is greater than 0, False otherwise.
        """
        return self.hp > 0