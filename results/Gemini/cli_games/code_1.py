import random

class Hangman:
    def __init__(self, word_list, max_attempts=6):
        """
        Initializes the Hangman game.

        Args:
            word_list (list): A list of strings representing possible words to guess.
            max_attempts (int): The maximum number of incorrect guesses allowed.
        """
        self.word_list = word_list
        self.word_to_guess = random.choice(word_list).upper()
        self.guessed_letters = set()
        self.attempts_left = max_attempts
        self.word_display = ['_'] * len(self.word_to_guess)
        self.game_over = False
        self.max_attempts = max_attempts

    def display_game_state(self):
        """
        Prints the current state of the game to the console.
        """
        print("\n" + "=" * 30)
        print("Word:", " ".join(self.word_display))
        print("Guessed letters:", ", ".join(sorted(self.guessed_letters)))
        print("Attempts left:", self.attempts_left)
        print("=" * 30)

    def get_player_guess(self):
        """
        Prompts the player to enter a guess and validates the input.

        Returns:
            str: The player's guess (single uppercase letter).  Returns None if input is invalid.
        """
        while True:
            guess = input("Guess a letter: ").upper()
            if len(guess) != 1:
                print("Please enter only one letter.")
            elif not guess.isalpha():
                print("Please enter a letter (A-Z).")
            elif guess in self.guessed_letters:
                print("You already guessed that letter.")
            else:
                return guess
            
            if self.attempts_left <=0 and not self.game_over:
                self.game_over = True
                print("You lost!")
                return None

    def update_game_state(self, guess):
        """
        Updates the game state based on the player's guess.

        Args:
            guess (str): The player's guess (single uppercase letter).
        """
        self.guessed_letters.add(guess)

        if guess in self.word_to_guess:
            for i, letter in enumerate(self.word_to_guess):
                if letter == guess:
                    self.word_display[i] = guess
        else:
            self.attempts_left -= 1
            print("Incorrect guess.")

    def check_game_over(self):
        """
        Checks if the game is over (either won or lost).
        """
        if "_" not in self.word_display:
            self.game_over = True
            print("Congratulations! You guessed the word:", self.word_to_guess)
        elif self.attempts_left <= 0:
            self.game_over = True
            print("You ran out of attempts. The word was:", self.word_to_guess)

    def play(self):
        """
        Plays the Hangman game.
        """
        print("Welcome to Hangman!")
        self.display_game_state()

        while not self.game_over:
            guess = self.get_player_guess()
            if guess is None:
                break #handle if the player lost on a previous turn before guessing
            self.update_game_state(guess)
            self.display_game_state()
            self.check_game_over()


if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    game = Hangman(word_list)
    game.play()