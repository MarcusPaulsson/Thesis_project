import random

class Mastermind:
    """
    A class to represent the Mastermind game.
    """

    def __init__(self, code_length=4, colors=6, max_guesses=10):
        """
        Initializes the Mastermind game.

        Args:
            code_length (int): The length of the code to guess.
            colors (int): The number of possible colors (represented by integers).
            max_guesses (int): The maximum number of guesses allowed.
        """
        self.code_length = code_length
        self.colors = colors
        self.max_guesses = max_guesses
        self.secret_code = self._generate_code()
        self.guesses = []
        self.feedback = []
        self.game_over = False
        self.won = False

    def _generate_code(self):
        """
        Generates a random secret code.

        Returns:
            list: A list of integers representing the secret code.
        """
        return [random.randint(1, self.colors) for _ in range(self.code_length)]

    def guess(self, guess):
        """
        Takes a guess from the player and provides feedback.

        Args:
            guess (list): A list of integers representing the player's guess.

        Returns:
            tuple: A tuple containing:
                - bool: True if the guess is valid, False otherwise.
                - str: A message indicating the validity of the guess.
        """
        if len(guess) != self.code_length:
            return False, f"Invalid guess: Must be {self.code_length} digits long."
        if not all(1 <= digit <= self.colors for digit in guess):
            return False, f"Invalid guess: Digits must be between 1 and {self.colors}."

        self.guesses.append(guess)
        feedback = self._evaluate_guess(guess)
        self.feedback.append(feedback)

        if guess == self.secret_code:
            self.game_over = True
            self.won = True
            return True, "Congratulations! You cracked the code!"

        if len(self.guesses) >= self.max_guesses:
            self.game_over = True
            return True, f"You ran out of guesses. The code was {self.secret_code}"

        return True, self._feedback_to_string(feedback)

    def _evaluate_guess(self, guess):
        """
        Evaluates a guess against the secret code.

        Args:
            guess (list): The player's guess.

        Returns:
            list: A list of strings representing the feedback.  "B" for black (correct position),
                   "W" for white (correct color, wrong position), "" for incorrect.
        """
        feedback = []
        temp_secret = self.secret_code[:]  # Create a copy to avoid modifying the original
        temp_guess = guess[:]

        # First, check for correct positions (black pegs)
        for i in range(self.code_length):
            if temp_guess[i] == temp_secret[i]:
                feedback.append("B")
                temp_secret[i] = None  # Mark as used
                temp_guess[i] = None  # Mark as used

        # Then, check for correct colors in wrong positions (white pegs)
        for i in range(self.code_length):
            if temp_guess[i] is not None:
                try:
                    j = temp_secret.index(temp_guess[i])
                    feedback.append("W")
                    temp_secret[j] = None  # Mark as used
                except ValueError:
                    pass  # Color not found in secret code

        # Sort the feedback to have black pegs first
        feedback.sort(reverse=True)
        return feedback

    def _feedback_to_string(self, feedback):
        """
        Converts the feedback list to a string.

        Args:
            feedback (list): The feedback list.

        Returns:
            str: A string representation of the feedback.
        """
        return "".join(feedback)

    def display_guesses(self):
        """
        Displays the previous guesses and their feedback.
        """
        print("\nPrevious Guesses:")
        for i in range(len(self.guesses)):
            print(f"Guess {i+1}: {self.guesses[i]} - Feedback: {self._feedback_to_string(self.feedback[i])}")

    def play(self):
        """
        Plays the Mastermind game through the command line.
        """
        print("Welcome to Mastermind!")
        print(f"I've generated a secret code with {self.code_length} digits, each between 1 and {self.colors}.")
        print(f"You have {self.max_guesses} guesses to crack the code.")

        while not self.game_over:
            try:
                guess_str = input(f"Enter your guess (separated by spaces, e.g., {' '.join(['1'] * self.code_length)}): ")
                guess = [int(x) for x in guess_str.split()]
            except ValueError:
                print("Invalid input. Please enter numbers separated by spaces.")
                continue

            valid, message = self.guess(guess)
            if not valid:
                print(message)
            else:
                print(message)
                self.display_guesses()

        if self.won:
            print("You won!")
        else:
            print(f"You lost! The secret code was {self.secret_code}")


if __name__ == "__main__":
    game = Mastermind()  # You can customize the game by passing arguments to the constructor
    game.play()