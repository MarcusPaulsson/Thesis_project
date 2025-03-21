import random

class Hangman:
    def __init__(self, word_list, max_attempts=6):
        self.word_list = word_list
        self.word_to_guess = random.choice(self.word_list).upper()
        self.guessed_letters = set()
        self.attempts_left = max_attempts
        self.word_display = ['_' for _ in self.word_to_guess]
        self.game_over = False
        self.won = False

    def display(self):
        print("\n" + " ".join(self.word_display))
        print(f"Attempts left: {self.attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")

    def guess_letter(self, letter):
        letter = letter.upper()

        if len(letter) != 1 or not letter.isalpha():
            print("Invalid input. Please enter a single letter.")
            return

        if letter in self.guessed_letters:
            print("You already guessed that letter.")
            return

        self.guessed_letters.add(letter)

        if letter in self.word_to_guess:
            for i, char in enumerate(self.word_to_guess):
                if char == letter:
                    self.word_display[i] = letter
            if ''.join(self.word_display) == self.word_to_guess:
                self.won = True
                self.game_over = True
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                self.game_over = True

    def play(self):
        print("Welcome to Hangman!")
        while not self.game_over:
            self.display()
            guess = input("Guess a letter: ")
            self.guess_letter(guess)

        if self.won:
            print(f"Congratulations! You guessed the word: {self.word_to_guess}")
        else:
            print(f"You ran out of attempts. The word was: {self.word_to_guess}")

if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
    game = Hangman(word_list)
    game.play()