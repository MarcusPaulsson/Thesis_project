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
        self.word = random.choice(word_list).upper()
        self.guessed_letters = set()
        self.attempts_left = max_attempts
        self.word_completion = ["_" for _ in self.word]
        self.game_over = False

    def display_word(self):
        """
        Returns the current state of the word with guessed letters revealed.
        """
        return " ".join(self.word_completion)

    def display_status(self):
        """
        Displays the current game status to the user.
        """
        print(f"\nWord: {self.display_word()}")
        print(f"Attempts left: {self.attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")

    def get_guess(self):
        """
        Prompts the user for a letter guess and validates the input.

        Returns:
            str: The valid letter guess (uppercase).
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

    def process_guess(self, guess):
        """
        Processes the user's guess, updating the game state.

        Args:
            guess (str): The letter guessed by the user.
        """
        self.guessed_letters.add(guess)

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_completion[i] = guess
            if "_" not in self.word_completion:
                self.game_over = True
                print("Congratulations! You guessed the word!")
        else:
            self.attempts_left -= 1
            print("Incorrect guess.")
            if self.attempts_left == 0:
                self.game_over = True
                print(f"You ran out of attempts. The word was {self.word}.")

    def play(self):
        """
        Runs the main game loop.
        """
        print("Welcome to Hangman!")

        while not self.game_over:
            self.display_status()
            guess = self.get_guess()
            self.process_guess(guess)

        # Display the final word if the game ended without winning.
        if "_" in self.word_completion:
            print(f"The word was: {self.word}")


if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    game = Hangman(word_list)
    game.play()