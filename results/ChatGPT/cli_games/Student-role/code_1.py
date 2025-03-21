import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = random.choice(self.word_list).upper()
        self.guesses = []
        self.max_attempts = 6
        self.attempts = 0

    def display_word(self):
        displayed = ''.join([letter if letter in self.guesses else '_' for letter in self.word])
        return displayed

    def guess(self, letter):
        letter = letter.upper()
        if letter in self.guesses:
            print("You've already guessed that letter.")
            return False

        self.guesses.append(letter)
        if letter not in self.word:
            self.attempts += 1
            print(f"Wrong guess! Attempts left: {self.max_attempts - self.attempts}")
        return True

    def is_won(self):
        return all(letter in self.guesses for letter in self.word)

    def is_lost(self):
        return self.attempts >= self.max_attempts

    def play(self):
        print("Welcome to Hangman!")
        while not self.is_won() and not self.is_lost():
            print(f"Current word: {self.display_word()}")
            print(f"Guessed letters: {', '.join(self.guesses)}")
            guess = input("Guess a letter: ")
            if len(guess) == 1 and guess.isalpha():
                self.guess(guess)
            else:
                print("Please enter a single alphabetical character.")

        if self.is_won():
            print(f"Congratulations! You've guessed the word: {self.word}")
        else:
            print(f"Sorry, you've lost. The word was: {self.word}")

if __name__ == "__main__":
    word_list = ['PYTHON', 'HANGMAN', 'DEVELOPER', 'COMPUTER', 'PROGRAMMING']
    game = Hangman(word_list)
    game.play()