import random

class Hangman:
    def __init__(self):
        self.words = ['python', 'hangman', 'programming', 'developer', 'challenge', 'interface']
        self.max_attempts = 6
        self.reset_game()

    def reset_game(self):
        self.secret_word = random.choice(self.words)
        self.guesses = []
        self.attempts_remaining = self.max_attempts
        self.word_completion = ['_' for _ in self.secret_word]

    def display_game_status(self):
        print("\nWord: " + " ".join(self.word_completion))
        print(f"Attempts remaining: {self.attempts_remaining}")
        print("Guessed letters: " + ", ".join(sorted(self.guesses)))

    def get_guess(self):
        while True:
            guess = input("Enter a letter: ").lower()
            if len(guess) == 1 and guess.isalpha() and guess not in self.guesses:
                self.guesses.append(guess)
                return guess
            print("Invalid input. Please enter a single unguessed letter.")

    def update_word_completion(self, guess):
        for index, letter in enumerate(self.secret_word):
            if letter == guess:
                self.word_completion[index] = letter

    def play(self):
        print("Welcome to Hangman!")
        while self.attempts_remaining > 0 and '_' in self.word_completion:
            self.display_game_status()
            guess = self.get_guess()
            if guess in self.secret_word:
                print(f"Good guess! '{guess}' is in the word.")
                self.update_word_completion(guess)
            else:
                self.attempts_remaining -= 1
                print(f"Sorry, '{guess}' is not in the word.")
        
        self.display_game_status()
        if '_' not in self.word_completion:
            print("Congratulations! You've guessed the word!")
        else:
            print(f"Game over! The word was '{self.secret_word}'.")

if __name__ == "__main__":
    game = Hangman()
    while True:
        game.play()
        if input("Play again? (y/n): ").lower() != 'y':
            break
        game.reset_game()