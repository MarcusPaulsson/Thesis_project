import random

class Mastermind:
    """
    A class representing the Mastermind game.
    """

    def __init__(self, code_length=4, colors=('R', 'G', 'B', 'Y', 'O', 'P'), max_guesses=10):
        """
        Initializes the Mastermind game.

        Args:
            code_length (int): The length of the code (default: 4).
            colors (tuple): The possible colors (default: ('R', 'G', 'B', 'Y', 'O', 'P')).
            max_guesses (int): The maximum number of guesses allowed (default: 10).
        """
        self.code_length = code_length
        self.colors = colors
        self.max_guesses = max_guesses
        self.secret_code = self._generate_secret_code()
        self.guesses_remaining = max_guesses
        self.game_over = False
        self.won = False

    def _generate_secret_code(self):
        """
        Generates a random secret code.

        Returns:
            str: The secret code.
        """
        return ''.join(random.choices(self.colors, k=self.code_length))

    def _evaluate_guess(self, guess):
        """
        Evaluates a guess and returns feedback.

        Args:
            guess (str): The player's guess.

        Returns:
            tuple: A tuple containing the number of exact matches and partial matches.
        """
        exact_matches = 0
        partial_matches = 0
        temp_secret_code = list(self.secret_code)
        temp_guess = list(guess)

        # Find exact matches
        for i in range(self.code_length):
            if temp_guess[i] == temp_secret_code[i]:
                exact_matches += 1
                temp_secret_code[i] = None  # Mark as matched
                temp_guess[i] = None        # Mark as matched

        # Find partial matches
        for i in range(self.code_length):
            if temp_guess[i] is not None:
                for j in range(self.code_length):
                    if temp_guess[i] == temp_secret_code[j]:
                        partial_matches += 1
                        temp_secret_code[j] = None  # Mark as matched
                        break

        return exact_matches, partial_matches

    def play_round(self, guess):
        """
        Plays a single round of the game.

        Args:
            guess (str): The player's guess.

        Returns:
            tuple: A tuple containing the number of exact matches, partial matches,
                   and a boolean indicating if the game is over.
        """
        if self.game_over:
            return None, None, True

        self.guesses_remaining -= 1

        exact_matches, partial_matches = self._evaluate_guess(guess)

        if exact_matches == self.code_length:
            self.game_over = True
            self.won = True
        elif self.guesses_remaining == 0:
            self.game_over = True

        return exact_matches, partial_matches, self.game_over

    def print_game_state(self):
        """
        Prints the current game state (guesses remaining).
        """
        print(f"Guesses remaining: {self.guesses_remaining}")

    def get_secret_code(self):
        """
        Returns the secret code (used for revealing at the end of the game).

        Returns:
            str: The secret code.
        """
        return self.secret_code

    def is_valid_guess(self, guess):
        """
        Checks if a guess is valid.

        Args:
            guess (str): The player's guess.

        Returns:
            bool: True if the guess is valid, False otherwise.
        """
        if len(guess) != self.code_length:
            return False
        for char in guess:
            if char not in self.colors:
                return False
        return True


def play_mastermind():
    """
    Plays a game of Mastermind through the command line.
    """
    code_length = 4
    colors = ('R', 'G', 'B', 'Y', 'O', 'P')
    max_guesses = 10

    print("Welcome to Mastermind!")
    print(f"Code length: {code_length}")
    print(f"Available colors: {', '.join(colors)}")
    print(f"You have {max_guesses} guesses.")

    game = Mastermind(code_length, colors, max_guesses)

    while not game.game_over:
        game.print_game_state()
        guess = input("Enter your guess (e.g., RGBY): ").upper()

        if not game.is_valid_guess(guess):
            print("Invalid guess. Please enter a guess with the correct length and using only the available colors.")
            continue

        exact_matches, partial_matches, game_over = game.play_round(guess)

        print(f"Exact matches: {exact_matches}")
        print(f"Partial matches: {partial_matches}")

    if game.won:
        print("Congratulations! You cracked the code!")
    else:
        print("You ran out of guesses.  The secret code was:", game.get_secret_code())

if __name__ == "__main__":
    play_mastermind()