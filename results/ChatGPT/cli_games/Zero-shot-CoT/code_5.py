import random

class Mastermind:
    def __init__(self, code_length=4, num_colors=6, max_attempts=10):
        self.code_length = code_length
        self.num_colors = num_colors
        self.max_attempts = max_attempts
        self.secret_code = self.generate_code()
        self.attempts = 0

    def generate_code(self):
        return [random.randint(1, self.num_colors) for _ in range(self.code_length)]

    def get_feedback(self, guess):
        correct_positions = sum(1 for i in range(self.code_length) if guess[i] == self.secret_code[i])
        correct_colors = sum(min(guess.count(c), self.secret_code.count(c)) for c in set(guess))
        correct_colors -= correct_positions
        return correct_positions, correct_colors

    def play(self):
        print("Welcome to Mastermind!")
        print(f"Guess the {self.code_length}-digit code using numbers 1 to {self.num_colors}.")
        print(f"You have {self.max_attempts} attempts to guess the code.")

        while self.attempts < self.max_attempts:
            guess = input(f"Attempt {self.attempts + 1}: Enter your guess: ")
            if not self.is_valid_guess(guess):
                print("Invalid guess. Please enter a sequence of numbers separated by spaces.")
                continue

            guess = list(map(int, guess.split()))
            self.attempts += 1
            correct_positions, correct_colors = self.get_feedback(guess)

            if correct_positions == self.code_length:
                print(f"Congratulations! You've guessed the code: {self.secret_code}")
                return

            print(f"Feedback: {correct_positions} correct positions, {correct_colors} correct colors.")

        print(f"Sorry, you've run out of attempts! The secret code was: {self.secret_code}")

    def is_valid_guess(self, guess):
        parts = guess.split()
        if len(parts) != self.code_length:
            return False
        return all(part.isdigit() and 1 <= int(part) <= self.num_colors for part in parts)

if __name__ == "__main__":
    game = Mastermind()
    game.play()