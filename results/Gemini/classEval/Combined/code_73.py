class RPGCharacter:
    """
    The class represents a role-playing game character, which allows to attack other characters, heal, gain experience, level up, and check if the character is alive.
    """

    MAX_HP = 100
    MAX_LEVEL = 100
    EXP_THRESHOLD = 100

    def __init__(self, name, hp, attack_power, defense, level=1):
        """
        Initialize an RPG character object.

        :param name: str, the name of the character.
        :param hp: int, The health points of the character.
        :param attack_power: int, the attack power of the character.
        :param defense: int, the defense points of the character.
        :param level: int, the level of the character. Default is 1.

        :raises ValueError: if hp, attack_power, defense, or level are negative.
        """
        if any(arg < 0 for arg in [hp, attack_power, defense, level]):
            raise ValueError("Character stats cannot be negative.")

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
        :raises TypeError: if other_character is not an RPGCharacter instance.
        """
        if not isinstance(other_character, RPGCharacter):
            raise TypeError("Can only attack other RPGCharacter instances.")

        damage = max(0, self.attack_power - other_character.defense)
        other_character.hp -= damage

    def heal(self):
        """
        Heal the character, increasing hp by 10, up to a maximum of 100.

        :return: int, the current health points after healing.
        """
        self.hp = min(self.MAX_HP, self.hp + 10)
        return self.hp

    def gain_exp(self, amount):
        """
        Gain experience points for the character and level_up when the exp has reached the values that is 100 times the current level.
        The experience that overflows should be used to calculate the next level up until exhausted.

        :param amount: int, the amount of experience points to gain.
        :raises ValueError: if amount is negative.
        """
        if amount < 0:
            raise ValueError("Experience gain must be non-negative.")

        self.exp += amount
        while self.exp >= self.level * self.EXP_THRESHOLD:
            if self.level < self.MAX_LEVEL:
                self.level_up()
                self.exp -= self.level * self.EXP_THRESHOLD
            else:
                self.exp = 0  # Reset exp if max level is reached
                break

    def level_up(self):
        """
        Level up the character, increasing hp by 20, attack power and defense points by 5 points.
        The maximum level is 100.

        :return: None
        """
        if self.level < self.MAX_LEVEL:
            self.level += 1
            self.hp += 20
            self.attack_power += 5
            self.defense += 5

    def is_alive(self):
        """
        Check if player is alive.

        :return: bool, True if the hp is larger than 0, or False otherwise.
        """
        return self.hp > 0