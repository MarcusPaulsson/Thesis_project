import random

class Mastermind:
    """
    A class representing the Mastermind game.
    """

    def __init__(self, code_length=4, colors=6, max_guesses=10):
        """
        Initializes a new Mastermind game.

        Args:
            code_length (int): The length of the secret code.
            colors (int): The number of different colors to choose from (1 to colors).
            max_guesses (int): The maximum number of guesses allowed.
        """
        self.code_length = code_length
        self.colors = colors
        self.max_guesses = max_guesses
        self.secret_code = self._generate_secret_code()
        self.guesses = []
        self.feedback = []
        self.game_over = False
        self.won = False

    def _generate_secret_code(self):
        """
        Generates a random secret code.

        Returns:
            list: A list of integers representing the secret code.
        """
        return [random.randint(1, self.colors) for _ in range(self.code_length)]

    def guess(self, guess):
        """
        Processes a player's guess.

        Args:
            guess (list): A list of integers representing the player's guess.

        Returns:
            tuple: A tuple containing the feedback (list of strings) and a boolean indicating if the guess was correct.
        """
        if self.game_over:
            return None, False

        if len(guess) != self.code_length:
            raise ValueError(f"Guess must be of length {self.code_length}")

        for color in guess:
            if not (1 <= color <= self.colors):
                raise ValueError(f"Colors must be between 1 and {self.colors}")

        self.guesses.append(guess)
        feedback = self._get_feedback(guess)
        self.feedback.append(feedback)

        if guess == self.secret_code:
            self.game_over = True
            self.won = True
            return feedback, True

        if len(self.guesses) >= self.max_guesses:
            self.game_over = True
            self.won = False
            return feedback, False

        return feedback, False

    def _get_feedback(self, guess):
        """
        Calculates the feedback for a given guess.

        Args:
            guess (list): A list of integers representing the player's guess.

        Returns:
            list: A list of strings representing the feedback.  "black" for correct color and position, "white" for correct color but wrong position.
        """
        feedback = []
        temp_secret_code = self.secret_code[:]
        temp_guess = guess[:]

        # Check for black pegs (correct color and position)
        for i in range(self.code_length):
            if temp_guess[i] == temp_secret_code[i]:
                feedback.append("black")
                temp_guess[i] = None  # Mark as used
                temp_secret_code[i] = None  # Mark as used

        # Check for white pegs (correct color, wrong position)
        for i in range(self.code_length):
            if temp_guess[i] is not None:
                for j in range(self.code_length):
                    if temp_secret_code[j] is not None and temp_guess[i] == temp_secret_code[j]:
                        feedback.append("white")
                        temp_guess[i] = None  # Mark as used
                        temp_secret_code[j] = None  # Mark as used
                        break

        return feedback

    def print_board(self):
        """
        Prints the current state of the game board.
        """
        print("\n--- Game Board ---")
        for i in range(len(self.guesses)):
            print(f"Guess {i + 1}: {self.guesses[i]}  Feedback: {self.feedback[i]}")
        print("------------------\n")

    def play(self):
        """
        Plays the Mastermind game in the command line.
        """
        print(f"Welcome to Mastermind!\n")
        print(f"I have generated a secret code of length {self.code_length} using colors 1 to {self.colors}.")
        print(f"You have {self.max_guesses} guesses to crack the code.")

        while not self.game_over:
            self.print_board()
            try:
                guess_str = input(f"Enter your guess (separated by spaces, e.g., '1 2 3 4'): ")
                guess = [int(x) for x in guess_str.split()]
                feedback, correct = self.guess(guess)

                if correct:
                    self.print_board()
                    print("Congratulations! You cracked the code!")
                elif self.game_over:
                    self.print_board()
                    print(f"You ran out of guesses. The secret code was: {self.secret_code}")
                else:
                    print(f"Feedback: {feedback}")

            except ValueError as e:
                print(f"Invalid input: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    game = Mastermind()  # You can customize the parameters here
    game.play()