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
        self.secret_word = random.choice(self.word_list).upper()
        self.guessed_letters = set()
        self.attempts_left = max_attempts
        self.word_mask = ['_' for _ in self.secret_word]
        self.game_over = False

    def display_board(self):
        """
        Displays the current state of the game to the console.
        """
        print("\n" + "=" * 20)
        print("Word:", " ".join(self.word_mask))
        print("Guessed letters:", ", ".join(sorted(self.guessed_letters)))
        print("Attempts left:", self.attempts_left)
        print("=" * 20 + "\n")

    def get_guess(self):
        """
        Prompts the user to enter a guess and validates the input.

        Returns:
            str: The user's guess (a single uppercase letter).
        """
        while True:
            guess = input("Guess a letter: ").upper()
            if not guess.isalpha():
                print("Invalid input. Please enter a letter.")
            elif len(guess) != 1:
                print("Please guess only one letter at a time.")
            elif guess in self.guessed_letters:
                print("You already guessed that letter.")
            else:
                return guess

    def update_game_state(self, guess):
        """
        Updates the game state based on the user's guess.

        Args:
            guess (str): The user's guess.
        """
        self.guessed_letters.add(guess)
        if guess in self.secret_word:
            for i, letter in enumerate(self.secret_word):
                if letter == guess:
                    self.word_mask[i] = guess
            if "_" not in self.word_mask:
                self.game_over = True
                print("Congratulations! You guessed the word:", self.secret_word)
        else:
            self.attempts_left -= 1
            print("Incorrect guess.")
            if self.attempts_left == 0:
                self.game_over = True
                print("You ran out of attempts. The word was:", self.secret_word)

    def play(self):
        """
        Runs the main game loop.
        """
        print("Welcome to Hangman!")
        while not self.game_over:
            self.display_board()
            guess = self.get_guess()
            self.update_game_state(guess)
        print("Game Over.")


if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
    game = Hangman(word_list)
    game.play()