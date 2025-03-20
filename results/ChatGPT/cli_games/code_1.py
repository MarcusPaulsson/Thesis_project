import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = ""
        self.guesses = []
        self.max_attempts = 6
        self.attempts = 0
        self.is_won = False

    def choose_word(self):
        self.word = random.choice(self.word_list).upper()

    def display_word(self):
        display = ''.join([letter if letter in self.guesses else '_' for letter in self.word])
        return display

    def guess_letter(self, letter):
        if letter in self.guesses:
            return "You already guessed that letter."
        self.guesses.append(letter)
        if letter not in self.word:
            self.attempts += 1
            return "Incorrect guess."
        if all(letter in self.guesses for letter in self.word):
            self.is_won = True
            return "Congratulations! You've guessed the word!"
        return "Good guess!"

    def is_game_over(self):
        return self.attempts >= self.max_attempts or self.is_won

    def play(self):
        self.choose_word()
        print("Welcome to Hangman!")
        
        while not self.is_game_over():
            print(f"Word: {self.display_word()}")
            print(f"Attempts left: {self.max_attempts - self.attempts}")
            guess = input("Guess a letter: ").upper()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single valid letter.")
                continue

            result = self.guess_letter(guess)
            print(result)

        if not self.is_won:
            print(f"You've run out of attempts! The word was: {self.word}")

if __name__ == "__main__":
    words = ["python", "hangman", "challenge", "programming", "developer"]
    game = Hangman(words)
    game.play()