import random

class Mastermind:
    def __init__(self, code_length=4, color_range=6, max_guesses=10):
        """
        Initializes the Mastermind game.

        Args:
            code_length (int): The length of the code to guess. Default is 4.
            color_range (int): The number of possible colors (1 to color_range). Default is 6.
            max_guesses (int): The maximum number of guesses allowed. Default is 10.
        """
        self.code_length = code_length
        self.color_range = color_range
        self.max_guesses = max_guesses
        self.secret_code = self.generate_secret_code()
        self.guesses_remaining = max_guesses
        self.history = []  # List to store guesses and feedback

    def generate_secret_code(self):
        """
        Generates a random secret code.

        Returns:
            list: A list of integers representing the secret code.
        """
        return [random.randint(1, self.color_range) for _ in range(self.code_length)]

    def get_guess(self):
        """
        Prompts the user for a guess and validates the input.

        Returns:
            list: A list of integers representing the user's guess, or None if input is invalid.
        """
        while True:
            try:
                guess_str = input(f"Enter your guess ({self.code_length} numbers, 1-{self.color_range}, separated by spaces): ")
                guess = [int(x) for x in guess_str.split()]

                if len(guess) != self.code_length:
                    print(f"Invalid guess: Must be {self.code_length} numbers long.")
                    continue

                if any(not (1 <= x <= self.color_range) for x in guess):
                    print(f"Invalid guess: Numbers must be between 1 and {self.color_range}.")
                    continue

                return guess
            except ValueError:
                print("Invalid input: Please enter numbers separated by spaces.")

    def check_guess(self, guess):
        """
        Checks the user's guess against the secret code and provides feedback.

        Args:
            guess (list): A list of integers representing the user's guess.

        Returns:
            tuple: A tuple containing the number of "exact" matches (correct color and position) and
                   the number of "partial" matches (correct color, wrong position).
        """
        exact_matches = 0
        partial_matches = 0
        temp_secret_code = self.secret_code[:]  # Create a copy to avoid modifying the original
        temp_guess = guess[:]

        # First, check for exact matches
        for i in range(self.code_length):
            if temp_guess[i] == temp_secret_code[i]:
                exact_matches += 1
                temp_guess[i] = None  # Mark as matched to avoid double-counting
                temp_secret_code[i] = None

        # Then, check for partial matches
        for i in range(self.code_length):
            if temp_guess[i] is not None:
                if temp_guess[i] in temp_secret_code:
                    partial_matches += 1
                    # Remove the first occurrence of the matching color from the secret code
                    temp_secret_code[temp_secret_code.index(temp_guess[i])] = None

        return exact_matches, partial_matches

    def play_round(self):
        """
        Plays a single round of the game.

        Returns:
            bool: True if the user guessed the code correctly, False otherwise.
        """
        guess = self.get_guess()
        if guess is None:
            return False  # Invalid guess, but continue the game

        exact_matches, partial_matches = self.check_guess(guess)
        self.history.append((guess, exact_matches, partial_matches))
        self.guesses_remaining -= 1

        print(f"Feedback: Exact matches: {exact_matches}, Partial matches: {partial_matches}")

        return exact_matches == self.code_length

    def print_history(self):
        """
        Prints the history of guesses and feedback.
        """
        print("\n--- Guess History ---")
        for guess, exact, partial in self.history:
            print(f"Guess: {guess}, Exact: {exact}, Partial: {partial}")
        print("---------------------")

    def play_game(self):
        """
        Plays the entire Mastermind game.
        """
        print("Welcome to Mastermind!")
        print(f"I have generated a secret code of length {self.code_length} with numbers from 1 to {self.color_range}.")
        print(f"You have {self.max_guesses} guesses to crack the code.")

        while self.guesses_remaining > 0:
            print(f"\nGuesses remaining: {self.guesses_remaining}")
            if self.play_round():
                print("Congratulations! You cracked the code!")
                self.print_history()
                return

        print("\nYou ran out of guesses.")
        print(f"The secret code was: {self.secret_code}")
        self.print_history()


if __name__ == "__main__":
    game = Mastermind()  # You can customize code_length, color_range, and max_guesses
    game.play_game()