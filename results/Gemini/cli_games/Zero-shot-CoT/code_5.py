import random

class Mastermind:
    """
    A class to represent the Mastermind game.
    """

    def __init__(self, code_length=4, colors=6, max_guesses=10):
        """
        Initializes the Mastermind game.

        Args:
            code_length (int): The length of the secret code.
            colors (int): The number of different colors to choose from (1 to colors).
            max_guesses (int): The maximum number of guesses allowed.
        """
        self.code_length = code_length
        self.colors = colors
        self.max_guesses = max_guesses
        self.secret_code = self.generate_secret_code()
        self.guesses = []
        self.feedback = []
        self.game_over = False
        self.won = False

    def generate_secret_code(self):
        """
        Generates a random secret code.

        Returns:
            list: A list of integers representing the secret code.
        """
        return [random.randint(1, self.colors) for _ in range(self.code_length)]

    def get_guess(self):
        """
        Gets a guess from the player through the command line.

        Returns:
            list: A list of integers representing the player's guess, or None if the input is invalid.
        """
        while True:
            try:
                guess_str = input(f"Enter your guess (separated by spaces, {self.code_length} numbers from 1 to {self.colors}): ")
                guess = [int(x) for x in guess_str.split()]
                if len(guess) != self.code_length:
                    print(f"Invalid guess: You must enter {self.code_length} numbers.")
                elif any(x < 1 or x > self.colors for x in guess):
                    print(f"Invalid guess: Numbers must be between 1 and {self.colors}.")
                else:
                    return guess
            except ValueError:
                print("Invalid input: Please enter numbers separated by spaces.")

    def check_guess(self, guess):
        """
        Checks the player's guess against the secret code and provides feedback.

        Args:
            guess (list): A list of integers representing the player's guess.

        Returns:
            tuple: A tuple containing the number of correct positions and the number of correct colors.
        """
        correct_position = 0
        correct_color = 0
        temp_secret = self.secret_code[:]  # Create a copy to avoid modifying the original
        temp_guess = guess[:]  # Create a copy to avoid modifying the original

        # Check for correct positions first
        for i in range(self.code_length):
            if temp_guess[i] == temp_secret[i]:
                correct_position += 1
                temp_guess[i] = None  # Mark as matched
                temp_secret[i] = None  # Mark as matched

        # Check for correct colors
        for i in range(self.code_length):
            if temp_guess[i] is not None:
                try:
                    index = temp_secret.index(temp_guess[i])
                    correct_color += 1
                    temp_secret[index] = None  # Mark as matched
                except ValueError:
                    pass  # Color not found in secret code

        return correct_position, correct_color

    def play_round(self):
        """
        Plays a single round of the game.
        """
        guess = self.get_guess()
        if guess is None:
            return  # Invalid guess, don't proceed

        self.guesses.append(guess)
        correct_position, correct_color = self.check_guess(guess)
        self.feedback.append((correct_position, correct_color))

        print(f"Feedback: Correct Position: {correct_position}, Correct Color: {correct_color}")

        if correct_position == self.code_length:
            self.game_over = True
            self.won = True
            print("Congratulations! You cracked the code!")
        elif len(self.guesses) >= self.max_guesses:
            self.game_over = True
            print(f"You ran out of guesses. The secret code was: {self.secret_code}")

    def play_game(self):
        """
        Plays the entire Mastermind game.
        """
        print("Welcome to Mastermind!")
        print(f"I've generated a secret code with {self.code_length} numbers, each from 1 to {self.colors}.")
        print(f"You have {self.max_guesses} guesses to crack the code.")

        while not self.game_over:
            self.play_round()


if __name__ == "__main__":
    game = Mastermind()
    game.play_game()