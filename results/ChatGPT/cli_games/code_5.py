import random

class Mastermind:
    def __init__(self, code_length=4, max_attempts=10, colors=None):
        self.code_length = code_length
        self.max_attempts = max_attempts
        self.colors = colors or ['R', 'G', 'B', 'Y', 'O', 'P']
        self.secret_code = self.generate_secret_code()
        self.attempts = 0

    def generate_secret_code(self):
        return random.choices(self.colors, k=self.code_length)

    def get_feedback(self, guess):
        if len(guess) != self.code_length:
            return "Invalid guess length."
        
        correct_position = sum(1 for g, s in zip(guess, self.secret_code) if g == s)
        correct_color = sum(min(guess.count(c), self.secret_code.count(c)) for c in set(guess)) - correct_position
        
        return correct_position, correct_color

    def play(self):
        print("Welcome to Mastermind!")
        print(f"Try to guess the secret code of length {self.code_length}.")
        print(f"You have {self.max_attempts} attempts.")
        
        while self.attempts < self.max_attempts:
            guess = input(f"Attempt {self.attempts + 1}: Enter your guess (colors: {', '.join(self.colors)}): ").upper()
            feedback = self.get_feedback(guess)

            if isinstance(feedback, str):
                print(feedback)
                continue
            
            correct_position, correct_color = feedback
            self.attempts += 1

            if correct_position == self.code_length:
                print(f"Congratulations! You've guessed the code: {''.join(self.secret_code)}")
                return
            
            print(f"Feedback: {correct_position} correct in position, {correct_color} correct color but wrong position.")

        print(f"Game over! The secret code was: {''.join(self.secret_code)}")

if __name__ == "__main__":
    game = Mastermind()
    game.play()