import random

class Hangman:
    def __init__(self):
        self.words = ["python", "hangman", "programming", "developer", "interface", "function"]
        self.word = random.choice(self.words)
        self.guesses = []
        self.max_attempts = 6
        self.attempts = 0

    def display_word(self):
        displayed = ''.join([letter if letter in self.guesses else '_' for letter in self.word])
        print(f"Word: {displayed}")

    def get_guess(self):
        while True:
            guess = input("Enter a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in self.guesses:
                    print("You've already guessed that letter.")
                else:
                    return guess
            else:
                print("Invalid input. Please enter a single letter.")

    def play(self):
        print("Welcome to Hangman!")
        while self.attempts < self.max_attempts:
            self.display_word()
            guess = self.get_guess()
            self.guesses.append(guess)

            if guess not in self.word:
                self.attempts += 1
                print(f"Wrong guess! You have {self.max_attempts - self.attempts} attempts left.")

            if all(letter in self.guesses for letter in self.word):
                print(f"Congratulations! You've guessed the word: {self.word}")
                return
        
        print(f"Game over! The word was: {self.word}")

if __name__ == "__main__":
    game = Hangman()
    game.play()