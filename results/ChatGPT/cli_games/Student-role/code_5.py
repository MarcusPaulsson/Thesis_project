import random

class Mastermind:
    def __init__(self, code_length=4, possible_colors=6, max_attempts=10):
        self.code_length = code_length
        self.possible_colors = possible_colors
        self.max_attempts = max_attempts
        self.secret_code = self.generate_code()
        self.attempts = 0

    def generate_code(self):
        return [random.randint(1, self.possible_colors) for _ in range(self.code_length)]

    def get_feedback(self, guess):
        correct_position = sum([1 for i in range(self.code_length) if guess[i] == self.secret_code[i]])
        correct_color = sum(min(guess.count(color), self.secret_code.count(color)) for color in set(guess))
        return correct_position, correct_color - correct_position

    def play(self):
        print("Welcome to Mastermind!")
        print(f"Guess the secret code of length {self.code_length} using {self.possible_colors} colors.")
        print("You have a maximum of 10 attempts.")

        while self.attempts < self.max_attempts:
            guess = input(f"Attempt {self.attempts + 1}: Enter your guess (space-separated numbers 1-{self.possible_colors}): ")
            guess = list(map(int, guess.split()))

            if len(guess) != self.code_length:
                print(f"Please enter exactly {self.code_length} numbers.")
                continue

            self.attempts += 1
            correct_position, correct_color = self.get_feedback(guess)

            if correct_position == self.code_length:
                print(f"Congratulations! You've guessed the code: {self.secret_code}")
                break
            else:
                print(f"Correct position: {correct_position}, Correct color (wrong position): {correct_color}")

        if self.attempts == self.max_attempts:
            print(f"Sorry, you've used all attempts. The secret code was: {self.secret_code}")

if __name__ == "__main__":
    game = Mastermind()
    game.play()