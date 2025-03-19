import random

class Hangman:
    def __init__(self, word_list, max_attempts=6):
        self.word_list = word_list
        self.max_attempts = max_attempts
        self.word = random.choice(self.word_list).upper()
        self.guesses = set()
        self.attempts = 0

    def display_word(self):
        return ' '.join(letter if letter in self.guesses else '_' for letter in self.word)

    def make_guess(self, guess):
        guess = guess.upper()
        if guess in self.guesses:
            return False, "You've already guessed that letter."
        self.guesses.add(guess)
        if guess not in self.word:
            self.attempts += 1
        return True, None

    def is_won(self):
        return all(letter in self.guesses for letter in self.word)

    def is_lost(self):
        return self.attempts >= self.max_attempts

    def play(self):
        print("Welcome to Hangman!")
        while not self.is_won() and not self.is_lost():
            print(f"Word: {self.display_word()}")
            print(f"Attempts left: {self.max_attempts - self.attempts}")
            guess = input("Enter a letter: ").strip()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            
            valid, message = self.make_guess(guess)
            if message:
                print(message)

        if self.is_won():
            print(f"Congratulations! You've won! The word was '{self.word}'.")
        else:
            print(f"Game over! The word was '{self.word}'.")

if __name__ == "__main__":
    words = ["PYTHON", "HANGMAN", "PROGRAMMING", "COMPUTER", "DEVELOPER"]
    game = Hangman(words)
    game.play()