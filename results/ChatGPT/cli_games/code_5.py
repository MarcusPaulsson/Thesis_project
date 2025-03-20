import random

class Mastermind:
    def __init__(self, code_length=4, num_colors=6, max_attempts=10):
        self.code_length = code_length
        self.num_colors = num_colors
        self.max_attempts = max_attempts
        self.code = self.generate_code()
        self.attempts = 0

    def generate_code(self):
        return [random.randint(1, self.num_colors) for _ in range(self.code_length)]

    def get_feedback(self, guess):
        correct_position = sum(1 for i in range(self.code_length) if guess[i] == self.code[i])
        correct_color = sum(min(guess.count(x), self.code.count(x)) for x in set(guess)) - correct_position
        return correct_position, correct_color

    def play(self):
        print("Welcome to Mastermind!")
        print(f"Guess the code consisting of {self.code_length} colors (1 to {self.num_colors}).")
        print(f"You have {self.max_attempts} attempts.")
        
        while self.attempts < self.max_attempts:
            guess = input(f"Attempt {self.attempts + 1}: Enter your guess (comma separated): ")
            guess = list(map(int, guess.split(',')))

            if len(guess) != self.code_length or any(g < 1 or g > self.num_colors for g in guess):
                print(f"Invalid guess. Please enter {self.code_length} numbers between 1 and {self.num_colors}.")
                continue

            self.attempts += 1
            correct_position, correct_color = self.get_feedback(guess)

            if correct_position == self.code_length:
                print(f"Congratulations! You've guessed the code: {self.code}")
                break
            else:
                print(f"Feedback: {correct_position} correct position(s), {correct_color} correct color(s).")

        if self.attempts == self.max_attempts:
            print(f"Sorry, you've run out of attempts. The code was: {self.code}")

if __name__ == "__main__":
    game = Mastermind()
    game.play()