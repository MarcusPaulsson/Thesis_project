import random

class Mastermind:
    def __init__(self, code_length=4, colors=6, max_guesses=10):
        """
        Initializes a Mastermind game.

        Args:
            code_length (int): The length of the code to be guessed.
            colors (int): The number of different colors available.
            max_guesses (int): The maximum number of guesses allowed.
        """
        self.code_length = code_length
        self.colors = colors
        self.max_guesses = max_guesses
        self.secret_code = self._generate_secret_code()
        self.guesses_remaining = max_guesses
        self.history = []  # Store guesses and feedback
        self.game_over = False

    def _generate_secret_code(self):
        """
        Generates a random secret code.

        Returns:
            list: A list representing the secret code.
        """
        return [random.randint(1, self.colors) for _ in range(self.code_length)]

    def _get_feedback(self, guess):
        """
        Provides feedback on a guess.

        Args:
            guess (list): The player's guess.

        Returns:
            tuple: A tuple containing the number of exact matches and partial matches.
        """
        exact_matches = 0
        partial_matches = 0
        temp_secret = self.secret_code[:]  # Create a copy to avoid modifying the original
        temp_guess = guess[:]

        # Count exact matches first
        for i in range(self.code_length):
            if temp_guess[i] == temp_secret[i]:
                exact_matches += 1
                temp_secret[i] = None  # Mark as matched
                temp_guess[i] = None

        # Count partial matches
        for i in range(self.code_length):
            if temp_guess[i] is not None:
                try:
                    index = temp_secret.index(temp_guess[i])
                    partial_matches += 1
                    temp_secret[index] = None  # Mark as matched
                except ValueError:
                    pass  # Color not found in the secret code

        return exact_matches, partial_matches

    def make_guess(self, guess):
        """
        Processes a player's guess.

        Args:
            guess (list): The player's guess.

        Returns:
            tuple: A tuple containing the number of exact matches and partial matches,
                   or None if the game is over or the guess is invalid.
        """
        if self.game_over:
            print("Game is over. You can't make more guesses.")
            return None

        if len(guess) != self.code_length:
            print(f"Invalid guess length.  Must be {self.code_length} digits.")
            return None

        for color in guess:
            if not isinstance(color, int) or color < 1 or color > self.colors:
                print(f"Invalid color. Colors must be integers between 1 and {self.colors}.")
                return None

        self.guesses_remaining -= 1
        exact_matches, partial_matches = self._get_feedback(guess)
        self.history.append((guess, exact_matches, partial_matches))

        if exact_matches == self.code_length:
            print("Congratulations! You cracked the code.")
            self.game_over = True
        elif self.guesses_remaining == 0:
            print("You ran out of guesses. Game over.")
            print(f"The secret code was: {self.secret_code}")
            self.game_over = True
        else:
            print(f"Exact matches: {exact_matches}, Partial matches: {partial_matches}")
            print(f"Guesses remaining: {self.guesses_remaining}")

        return exact_matches, partial_matches

    def display_history(self):
        """
        Displays the guess history.
        """
        print("\nGuess History:")
        for guess, exact, partial in self.history:
            print(f"Guess: {guess}, Exact: {exact}, Partial: {partial}")

    def play(self):
        """
        Plays the Mastermind game.
        """
        print(f"Welcome to Mastermind!")
        print(f"I have generated a secret code of length {self.code_length} using colors 1 to {self.colors}.")
        print(f"You have {self.max_guesses} guesses to crack the code.")

        while not self.game_over:
            try:
                guess_str = input(f"Enter your guess (separated by spaces, e.g., '1 2 3 4'): ")
                guess = [int(x) for x in guess_str.split()]
            except ValueError:
                print("Invalid input. Please enter numbers separated by spaces.")
                continue

            self.make_guess(guess)
            self.display_history()


if __name__ == "__main__":
    game = Mastermind()  # You can customize the game by passing arguments
    game.play()