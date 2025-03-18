import random

class Mastermind:
    def __init__(self, code_length=4, max_attempts=10):
        self.code_length = code_length
        self.max_attempts = max_attempts
        self.code = self.generate_code()
        self.attempts = 0

    def generate_code(self):
        return [random.randint(0, 9) for _ in range(self.code_length)]

    def get_feedback(self, guess):
        correct_position = sum(1 for i in range(self.code_length) if guess[i] == self.code[i])
        correct_color = sum(min(guess.count(n), self.code.count(n)) for n in set(guess)) - correct_position
        return correct_position, correct_color

    def play(self):
        print("Welcome to Mastermind!")
        print(f"Guess the {self.code_length}-digit code. You have {self.max_attempts} attempts.")

        while self.attempts < self.max_attempts:
            guess = input(f"Attempt {self.attempts + 1}: Enter your guess (4 digits, 0-9): ")
            if not guess.isdigit() or len(guess) != self.code_length:
                print("Invalid input. Please enter exactly 4 digits.")
                continue

            guess = list(map(int, guess))
            self.attempts += 1
            correct_position, correct_color = self.get_feedback(guess)

            if correct_position == self.code_length:
                print(f"Congratulations! You've guessed the code: {''.join(map(str, self.code))}")
                return

            print(f"Feedback: {correct_position} correct position(s), {correct_color} correct color(s)")

        print(f"Sorry! You've used all attempts. The code was: {''.join(map(str, self.code))}")

if __name__ == "__main__":
    game = Mastermind()
    game.play()