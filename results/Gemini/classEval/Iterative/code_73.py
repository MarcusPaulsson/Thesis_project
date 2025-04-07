class RPGCharacter:
    """
    Represents a role-playing game character with abilities to attack, heal, gain experience, level up, and check life status.
    """

    MAX_HP = 100
    MAX_LEVEL = 100
    EXP_PER_LEVEL = 100
    HEAL_AMOUNT = 10
    LEVEL_UP_HP_INCREASE = 20
    LEVEL_UP_STAT_INCREASE = 5

    def __init__(self, name, hp, attack_power, defense, level=1):
        """
        Initializes an RPG character.

        Args:
            name (str): The character's name.
            hp (int): The character's health points.
            attack_power (int): The character's attack power.
            defense (int): The character's defense points.
            level (int): The character's level (default: 1).
        """
        if not all(isinstance(arg, int) and arg > 0 for arg in [hp, attack_power, defense, level]):
            raise ValueError("HP, attack_power, defense, and level must be positive integers.")
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = 0

    def attack(self, other_character):
        """
        Attacks another character, reducing their HP based on the attacker's attack power and the defender's defense.

        Args:
            other_character (RPGCharacter): The character being attacked.
        """
        if not isinstance(other_character, RPGCharacter):
            raise TypeError("Target must be an RPGCharacter instance.")

        damage = max(0, self.attack_power - other_character.defense)  # Ensure damage is not negative
        other_character.hp = max(0, other_character.hp - damage)  # Ensure HP doesn't go below 0

    def heal(self):
        """
        Heals the character, increasing their HP up to a maximum value.

        Returns:
            int: The character's current health points after healing.
        """
        self.hp = min(RPGCharacter.MAX_HP, self.hp + RPGCharacter.HEAL_AMOUNT)
        return self.hp

    def gain_exp(self, amount):
        """
        Gains experience points, potentially leveling up the character.

        Args:
            amount (int): The amount of experience points gained.
        """
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("Experience amount must be a non-negative integer.")

        self.exp += amount
        while self.exp >= RPGCharacter.EXP_PER_LEVEL * self.level and self.level < RPGCharacter.MAX_LEVEL:
            self.level_up()
            self.exp -= RPGCharacter.EXP_PER_LEVEL * self.level
        #cap experience at 100
        if self.exp > RPGCharacter.EXP_PER_LEVEL:
            self.exp = RPGCharacter.EXP_PER_LEVEL

    def level_up(self):
        """
        Levels up the character, increasing their stats.
        """
        if self.level < RPGCharacter.MAX_LEVEL:
            self.level += 1
            self.hp += RPGCharacter.LEVEL_UP_HP_INCREASE
            self.attack_power += RPGCharacter.LEVEL_UP_STAT_INCREASE
            self.defense += RPGCharacter.LEVEL_UP_STAT_INCREASE
            # Optionally cap HP at MAX_HP after level up
            self.hp = min(self.hp, RPGCharacter.MAX_HP)
        return (self.level, self.hp, self.attack_power, self.defense)

    def is_alive(self):
        """
        Checks if the character is alive.

        Returns:
            bool: True if the character's HP is greater than 0, False otherwise.
        """
        return self.hp > 0