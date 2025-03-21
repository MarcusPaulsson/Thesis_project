import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = random.choice(self.word_list).upper()
        self.guessed_letters = set()
        self.max_attempts = 6
        self.attempts = 0

    def display_word(self):
        displayed_word = ''.join(letter if letter in self.guessed_letters else '_' for letter in self.word)
        return displayed_word

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return False
        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.attempts += 1
        return True

    def is_word_guessed(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def is_game_over(self):
        return self.attempts >= self.max_attempts or self.is_word_guessed()

    def get_remaining_attempts(self):
        return self.max_attempts - self.attempts

    def play(self):
        print("Welcome to Hangman!")
        while not self.is_game_over():
            print(f"Word: {self.display_word()}")
            print(f"Attempts remaining: {self.get_remaining_attempts()}")
            guess = input("Guess a letter: ").upper()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            if not self.guess_letter(guess):
                print("You've already guessed that letter.")
        
        if self.is_word_guessed():
            print(f"Congratulations! You've guessed the word: {self.word}")
        else:
            print(f"Game over! The word was: {self.word}")

if __name__ == "__main__":
    word_list = ['PYTHON', 'JAVA', 'HANGMAN', 'DEVELOPER', 'COMPUTER']
    game = Hangman(word_list)
    game.play()