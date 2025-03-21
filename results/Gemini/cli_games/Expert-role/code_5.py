import random

class Mastermind:
    """
    A class to represent the Mastermind game.
    """

    def __init__(self, code_length=4, color_range=6, max_guesses=10):
        """
        Initializes the Mastermind game.

        Args:
            code_length (int): The length of the secret code.
            color_range (int): The number of possible colors (1 to color_range).
            max_guesses (int): The maximum number of guesses allowed.
        """
        self.code_length = code_length
        self.color_range = color_range
        self.max_guesses = max_guesses
        self.secret_code = self._generate_secret_code()
        self.guesses_remaining = max_guesses
        self.history = []  # Store guesses and feedback
        self.game_over = False

    def _generate_secret_code(self):
        """
        Generates a random secret code.

        Returns:
            list: A list of integers representing the secret code.
        """
        return [random.randint(1, self.color_range) for _ in range(self.code_length)]

    def _get_feedback(self, guess):
        """
        Provides feedback for a given guess.

        Args:
            guess (list): A list of integers representing the player's guess.

        Returns:
            tuple: A tuple containing the number of correct positions and correct colors.
        """
        correct_position = 0
        correct_color = 0
        temp_secret = self.secret_code[:]  # Create a copy to avoid modifying the original
        temp_guess = guess[:]

        # Check for correct positions first
        for i in range(self.code_length):
            if temp_guess[i] == temp_secret[i]:
                correct_position += 1
                temp_guess[i] = None  # Mark as matched
                temp_secret[i] = None  # Mark as matched

        # Check for correct colors in incorrect positions
        for i in range(self.code_length):
            if temp_guess[i] is not None:
                for j in range(self.code_length):
                    if temp_secret[j] is not None and temp_guess[i] == temp_secret[j]:
                        correct_color += 1
                        temp_secret[j] = None  # Mark as matched
                        break

        return correct_position, correct_color

    def make_guess(self, guess):
        """
        Processes a player's guess.

        Args:
            guess (list): A list of integers representing the player's guess.

        Returns:
            tuple: A tuple containing a boolean indicating if the guess was correct,
                   a tuple with the feedback (correct_position, correct_color),
                   and a boolean indicating if the game is over.
        """
        if self.game_over:
            return False, (0, 0), True

        if len(guess) != self.code_length:
            raise ValueError(f"Guess must be {self.code_length} digits long.")

        for digit in guess:
            if not 1 <= digit <= self.color_range:
                raise ValueError(f"Digits must be between 1 and {self.color_range}.")

        self.guesses_remaining -= 1
        correct_position, correct_color = self._get_feedback(guess)
        self.history.append((guess, (correct_position, correct_color)))

        if correct_position == self.code_length:
            self.game_over = True
            return True, (correct_position, correct_color), True

        if self.guesses_remaining == 0:
            self.game_over = True
            return False, (correct_position, correct_color), True

        return False, (correct_position, correct_color), False

    def display_history(self):
        """
        Displays the game history to the player.
        """
        print("\n--- Game History ---")
        for guess, feedback in self.history:
            print(f"Guess: {guess}, Feedback: {feedback}")
        print("--------------------")

    def play(self):
        """
        Plays the Mastermind game.
        """
        print(f"Welcome to Mastermind!")
        print(f"I've generated a secret code with {self.code_length} digits, each between 1 and {self.color_range}.")
        print(f"You have {self.max_guesses} guesses to crack the code.")

        while not self.game_over:
            try:
                guess_str = input(f"\nGuess ({self.guesses_remaining} remaining): ")
                guess = [int(digit) for digit in guess_str]

                is_correct, feedback, game_over = self.make_guess(guess)

                print(f"Feedback: {feedback[0]} correct position(s), {feedback[1]} correct color(s).")

                if is_correct:
                    print("\nCongratulations! You cracked the code!")
                    self.display_history()
                elif game_over:
                    print("\nYou ran out of guesses. Game over!")
                    print(f"The secret code was: {self.secret_code}")
                    self.display_history()

            except ValueError as e:
                print(f"Invalid input: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    game = Mastermind()
    game.play()