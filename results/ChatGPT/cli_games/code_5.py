import random

class Mastermind:
    def __init__(self, code_length=4, max_attempts=10, colors=None):
        self.code_length = code_length
        self.max_attempts = max_attempts
        self.colors = colors if colors else ['R', 'G', 'B', 'Y', 'O', 'P']
        self.secret_code = self.generate_code()

    def generate_code(self):
        return [random.choice(self.colors) for _ in range(self.code_length)]

    def evaluate_guess(self, guess):
        if len(guess) != self.code_length:
            raise ValueError(f"Guess must be {self.code_length} characters long.")
        
        correct_position = sum(1 for i in range(self.code_length) if guess[i] == self.secret_code[i])
        correct_color = sum(min(guess.count(color), self.secret_code.count(color)) for color in set(guess)) - correct_position
        
        return correct_position, correct_color

    def play(self):
        print("Welcome to Mastermind!")
        print(f"Guess the secret code composed of {self.code_length} colors from: {', '.join(self.colors)}.")
        print(f"You have {self.max_attempts} attempts to guess the code.")

        for attempt in range(1, self.max_attempts + 1):
            guess = input(f"Attempt {attempt}: Enter your guess: ").upper().strip()

            try:
                correct_position, correct_color = self.evaluate_guess(guess)
            except ValueError as e:
                print(e)
                continue

            if correct_position == self.code_length:
                print("Congratulations! You've cracked the code!")
                break
            
            print(f"Correct color and position: {correct_position}, Correct color but wrong position: {correct_color}")
        else:
            print(f"Sorry, you've used all attempts. The secret code was: {''.join(self.secret_code)}")

if __name__ == "__main__":
    game = Mastermind()
    game.play()