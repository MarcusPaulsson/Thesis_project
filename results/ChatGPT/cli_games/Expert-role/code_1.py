import random

class Hangman:
    def __init__(self, words):
        self.words = words
        self.word_to_guess = random.choice(self.words).upper()
        self.guessed_letters = set()
        self.attempts_remaining = 6
        self.word_guessed = False

    def display_hangman(self):
        stages = [
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               |
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   /
               |
            """,
            """
               ------
               |    |
               |    O
               |   /|
               |
               |
            """,
            """
               ------
               |    |
               |    O
               |    
               |
               |
            """,
            """
               ------
               |    |
               |    
               |    
               |
               |
            """,
            """
               ------
               |    
               |    
               |    
               |
               |
            """,
        ]
        return stages[self.attempts_remaining]

    def display_word(self):
        displayed_word = ''.join(letter if letter in self.guessed_letters else '_' for letter in self.word_to_guess)
        return displayed_word

    def guess_letter(self, letter):
        letter = letter.upper()
        if letter in self.guessed_letters:
            return False, "You already guessed that letter."
        
        self.guessed_letters.add(letter)

        if letter in self.word_to_guess:
            if all(l in self.guessed_letters for l in self.word_to_guess):
                self.word_guessed = True
            return True, "Good guess!"
        else:
            self.attempts_remaining -= 1
            return False, "Wrong guess!"

    def play(self):
        print("Welcome to Hangman!")
        while self.attempts_remaining > 0 and not self.word_guessed:
            print(self.display_hangman())
            print(f"Word: {self.display_word()}")
            print(f"Guessed letters: {' '.join(sorted(self.guessed_letters))}")
            print(f"Attempts remaining: {self.attempts_remaining}")
            
            guess = input("Guess a letter: ").strip()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            
            correct, message = self.guess_letter(guess)
            print(message)
        
        if self.word_guessed:
            print(f"Congratulations! You've guessed the word: {self.word_to_guess}")
        else:
            print(self.display_hangman())
            print(f"Sorry, you've run out of attempts. The word was: {self.word_to_guess}")

if __name__ == "__main__":
    word_list = ['python', 'java', 'hangman', 'programming', 'developer']
    game = Hangman(word_list)
    game.play()