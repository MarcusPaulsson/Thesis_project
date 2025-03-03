import random

class Mastermind:
    """
    A class to represent the Mastermind game.
    """

    def __init__(self, code_length=4, colors=('R', 'G', 'B', 'Y', 'O', 'P'), max_guesses=10):
        """
        Initializes a new Mastermind game.

        Args:
            code_length (int): The length of the secret code.
            colors (tuple): The possible colors to choose from.
            max_guesses (int): The maximum number of guesses allowed.
        """
        self.code_length = code_length
        self.colors = colors
        self.max_guesses = max_guesses
        self.secret_code = self._generate_secret_code()
        self.guesses = []
        self.results = []
        self.game_over = False
        self.won = False

    def _generate_secret_code(self):
        """
        Generates a random secret code.

        Returns:
            str: The secret code.
        """
        return ''.join(random.choice(self.colors) for _ in range(self.code_length))

    def guess(self, guess):
        """
        Makes a guess and evaluates it.

        Args:
            guess (str): The player's guess.

        Returns:
            tuple: A tuple containing the number of correct positions and correct colors.
        """
        if self.game_over:
            return None  # Game is already over

        if len(guess) != self.code_length:
            raise ValueError(f"Guess must be {self.code_length} characters long.")

        for char in guess:
            if char not in self.colors:
                raise ValueError(f"Invalid color: {char}.  Allowed colors are: {self.colors}")


        correct_position = 0
        correct_color = 0
        temp_secret = list(self.secret_code)  # Create a mutable copy of the secret code
        temp_guess = list(guess)  # Create a mutable copy of the guess
        
        # First, check for correct positions
        for i in range(self.code_length):
            if temp_guess[i] == temp_secret[i]:
                correct_position += 1
                temp_guess[i] = None  # Mark as used
                temp_secret[i] = None  # Mark as used

        # Then, check for correct colors in the remaining positions
        for i in range(self.code_length):
            if temp_guess[i] is not None:
                if temp_guess[i] in temp_secret:
                    correct_color += 1
                    temp_secret[temp_secret.index(temp_guess[i])] = None #Mark as used
                    
        self.guesses.append(guess)
        self.results.append((correct_position, correct_color))

        if correct_position == self.code_length:
            self.game_over = True
            self.won = True
        elif len(self.guesses) >= self.max_guesses:
            self.game_over = True
            self.won = False

        return (correct_position, correct_color)

    def is_game_over(self):
        """
        Checks if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.game_over

    def has_won(self):
        """
        Checks if the player has won.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        return self.won

    def get_guesses(self):
        """
        Returns the list of guesses made by the player.

        Returns:
            list: The list of guesses.
        """
        return self.guesses

    def get_results(self):
        """
        Returns the list of results for each guess.

        Returns:
            list: The list of results.
        """
        return self.results

    def get_secret_code(self):
        """
        Returns the secret code.  Only use this after game over.

        Returns:
            str: The secret code.
        """
        return self.secret_code


def play_mastermind():
    """
    Plays a game of Mastermind through the command line.
    """
    code_length = 4
    colors = ('R', 'G', 'B', 'Y', 'O', 'P')
    max_guesses = 10

    game = Mastermind(code_length, colors, max_guesses)

    print("Welcome to Mastermind!")
    print(f"I've generated a secret code with {code_length} colors.")
    print(f"The possible colors are: {', '.join(colors)}")
    print(f"You have {max_guesses} guesses to crack the code.")

    while not game.is_game_over():
        print("\nGuesses so far:")
        for i, guess in enumerate(game.get_guesses()):
            pos, color = game.get_results()[i]
            print(f"  {guess}: {pos} correct position(s), {color} correct color(s)")

        while True:
            try:
                guess = input("Enter your guess: ").upper()
                result = game.guess(guess)
                break # Exit the inner loop if the guess is valid
            except ValueError as e:
                print(f"Invalid guess: {e}")

    if game.has_won():
        print("\nCongratulations! You cracked the code!")
    else:
        print("\nYou ran out of guesses.")

    print(f"The secret code was: {game.get_secret_code()}")


if __name__ == "__main__":
    play_mastermind()