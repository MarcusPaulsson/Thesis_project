import random

class Mastermind:
    def __init__(self, code_length=4, num_colors=6):
        self.code_length = code_length
        self.num_colors = num_colors
        self.secret_code = self.generate_code()

    def generate_code(self):
        return [random.randint(1, self.num_colors) for _ in range(self.code_length)]

    def get_feedback(self, guess):
        correct_positions = sum(1 for i in range(self.code_length) if guess[i] == self.secret_code[i])
        correct_colors = sum(min(guess.count(color), self.secret_code.count(color)) for color in set(guess))
        correct_colors -= correct_positions  # Remove correct positions from correct colors
        return correct_positions, correct_colors

    def play(self):
        attempts = 10
        print("Welcome to Mastermind!")
        print(f"Guess the code of length {self.code_length} using {self.num_colors} colors (1 to {self.num_colors}).")
        
        while attempts > 0:
            guess_input = input(f"You have {attempts} attempts left. Enter your guess: ")
            try:
                guess = list(map(int, guess_input.split()))
                if len(guess) != self.code_length or any(color < 1 or color > self.num_colors for color in guess):
                    print(f"Invalid input. Please enter {self.code_length} numbers between 1 and {self.num_colors}.")
                    continue
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            correct_positions, correct_colors = self.get_feedback(guess)
            print(f"Feedback: {correct_positions} correct positions and {correct_colors} correct colors.")
            
            if correct_positions == self.code_length:
                print("Congratulations! You've cracked the code!")
                break

            attempts -= 1

        if attempts == 0:
            print("You've run out of attempts! The secret code was:", self.secret_code)

if __name__ == "__main__":
    game = Mastermind()
    game.play()