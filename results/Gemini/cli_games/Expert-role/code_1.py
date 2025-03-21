import random

class Hangman:
    """
    A class to represent the Hangman game.
    """

    def __init__(self, word_list, max_attempts=6):
        """
        Initializes the Hangman game.

        Args:
            word_list (list): A list of words to choose from.
            max_attempts (int): The maximum number of incorrect guesses allowed.
        """
        self.word_list = word_list
        self.word_to_guess = random.choice(self.word_list).upper()
        self.guessed_letters = set()
        self.attempts_remaining = max_attempts
        self.game_over = False
        self.word_display = ['_'] * len(self.word_to_guess) # Initialize with underscores

    def display_game_state(self):
        """
        Displays the current state of the game to the user.
        """
        print("\n" + "=" * 30)
        print("Word:", " ".join(self.word_display))
        print("Guessed letters:", ", ".join(sorted(self.guessed_letters)))
        print("Attempts remaining:", self.attempts_remaining)
        print("=" * 30)

    def get_user_guess(self):
        """
        Gets a letter guess from the user.

        Returns:
            str: The user's guess (a single uppercase letter).
        """
        while True:
            guess = input("Guess a letter: ").upper()
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid input. Please enter a single letter.")
            elif guess in self.guessed_letters:
                print("You already guessed that letter.")
            else:
                return guess

    def update_game_state(self, guess):
        """
        Updates the game state based on the user's guess.

        Args:
            guess (str): The letter guessed by the user.
        """
        self.guessed_letters.add(guess)

        if guess in self.word_to_guess:
            for i, letter in enumerate(self.word_to_guess):
                if letter == guess:
                    self.word_display[i] = guess
        else:
            self.attempts_remaining -= 1
            print("Incorrect guess.")

        if self.attempts_remaining == 0:
            self.game_over = True
            print("You ran out of attempts!")
            print("The word was:", self.word_to_guess)
        elif "_" not in self.word_display:
            self.game_over = True
            print("Congratulations! You guessed the word:", self.word_to_guess)

    def play_game(self):
        """
        Runs the main game loop.
        """
        print("Welcome to Hangman!")

        while not self.game_over:
            self.display_game_state()
            guess = self.get_user_guess()
            self.update_game_state(guess)

        print("Game over.")


if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    game = Hangman(word_list)
    game.play_game()