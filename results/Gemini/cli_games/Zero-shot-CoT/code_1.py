import random

class Hangman:
    def __init__(self, word_list, max_attempts=6):
        """
        Initializes the Hangman game.

        Args:
            word_list (list): A list of words to choose from.
            max_attempts (int): The maximum number of incorrect guesses allowed.
        """
        self.word_list = word_list
        self.word_to_guess = random.choice(word_list).upper()
        self.guessed_letters = set()
        self.attempts_left = max_attempts
        self.word_progress = ['_'] * len(self.word_to_guess)
        self.game_over = False

    def display_game_state(self):
        """
        Displays the current state of the game to the player.
        """
        print("\n" + "=" * 20)
        print("Word:", " ".join(self.word_progress))
        print("Guessed letters:", ", ".join(sorted(self.guessed_letters)))
        print("Attempts left:", self.attempts_left)
        print("=" * 20 + "\n")

    def get_player_guess(self):
        """
        Gets a letter guess from the player.

        Returns:
            str: The player's guess (a single uppercase letter).
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
        Updates the game state based on the player's guess.

        Args:
            guess (str): The player's guess.
        """
        self.guessed_letters.add(guess)
        if guess in self.word_to_guess:
            for i, letter in enumerate(self.word_to_guess):
                if letter == guess:
                    self.word_progress[i] = guess
            if "".join(self.word_progress) == self.word_to_guess:
                self.game_over = True
                print("Congratulations! You guessed the word:", self.word_to_guess)
        else:
            self.attempts_left -= 1
            print("Incorrect guess.")
            if self.attempts_left == 0:
                self.game_over = True
                print("You ran out of attempts. The word was:", self.word_to_guess)

    def play_game(self):
        """
        Plays the Hangman game.
        """
        print("Welcome to Hangman!")

        while not self.game_over:
            self.display_game_state()
            guess = self.get_player_guess()
            self.update_game_state(guess)

        print("Game over!")


if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    game = Hangman(word_list)
    game.play_game()