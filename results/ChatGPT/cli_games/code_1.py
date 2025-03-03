import random

class Hangman:
    def __init__(self):
        self.words = ["python", "hangman", "programming", "developer", "software", "keyboard", "interface", "challenge"]
        self.secret_word = random.choice(self.words)
        self.guesses = []
        self.max_attempts = 6
        self.attempts = 0

    def display_word(self):
        return ' '.join([letter if letter in self.guesses else '_' for letter in self.secret_word])

    def guess_letter(self, letter):
        if letter in self.guesses:
            print("You already guessed that letter.")
            return False
        self.guesses.append(letter)
        if letter not in self.secret_word:
            self.attempts += 1
            print(f"Incorrect guess. You have {self.max_attempts - self.attempts} attempts left.")
            return False
        return True

    def is_won(self):
        return all(letter in self.guesses for letter in self.secret_word)

    def is_lost(self):
        return self.attempts >= self.max_attempts

    def play(self):
        print("Welcome to Hangman!")
        while not self.is_won() and not self.is_lost():
            print("\nCurrent word:", self.display_word())
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            self.guess_letter(guess)

        if self.is_won():
            print("\nCongratulations! You've guessed the word:", self.secret_word)
        else:
            print("\nSorry, you've lost. The word was:", self.secret_word)

if __name__ == "__main__":
    game = Hangman()
    game.play()