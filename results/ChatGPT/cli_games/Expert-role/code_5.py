import random

class Mastermind:
    def __init__(self, code_length=4, max_attempts=10, colors=['R', 'G', 'B', 'Y', 'O', 'P']):
        self.code_length = code_length
        self.max_attempts = max_attempts
        self.colors = colors
        self.secret_code = self.generate_code()

    def generate_code(self):
        return [random.choice(self.colors) for _ in range(self.code_length)]

    def get_feedback(self, guess):
        correct_positions = sum(g == s for g, s in zip(guess, self.secret_code))
        correct_colors = sum(min(guess.count(color), self.secret_code.count(color)) for color in set(guess))
        correct_colors -= correct_positions
        return correct_positions, correct_colors

    def play(self):
        print("Welcome to Mastermind!")
        print(f"Guess the secret code of length {self.code_length} using the colors: {', '.join(self.colors)}.")
        print(f"You have {self.max_attempts} attempts.")
        
        for attempt in range(1, self.max_attempts + 1):
            guess = input(f"Attempt {attempt}: Enter your guess: ").upper().strip().split()
            
            if len(guess) != self.code_length or not all(color in self.colors for color in guess):
                print("Invalid guess. Please enter a valid combination of colors.")
                continue
            
            correct_positions, correct_colors = self.get_feedback(guess)
            print(f"Feedback: {correct_positions} correct positions, {correct_colors} correct colors.")
            
            if correct_positions == self.code_length:
                print("Congratulations! You've cracked the code!")
                break
        else:
            print(f"Sorry! You've used all attempts. The secret code was: {''.join(self.secret_code)}.")

if __name__ == "__main__":
    game = Mastermind()
    game.play()