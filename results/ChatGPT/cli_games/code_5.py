import random

class Mastermind:
    def __init__(self, code_length=4, num_colors=6):
        self.code_length = code_length
        self.num_colors = num_colors
        self.secret_code = self.generate_code()
        self.guesses = 0

    def generate_code(self):
        return [random.randint(1, self.num_colors) for _ in range(self.code_length)]

    def get_feedback(self, guess):
        correct_position = sum(1 for i in range(self.code_length) if guess[i] == self.secret_code[i])
        correct_color = sum(min(guess.count(x), self.secret_code.count(x)) for x in set(guess)) - correct_position
        return correct_position, correct_color

    def play(self):
        print("Welcome to Mastermind!")
        print(f"Try to guess the {self.code_length}-color code. Colors are represented by numbers 1 to {self.num_colors}.")
        print("You have 10 attempts to guess the code.")
        
        while self.guesses < 10:
            guess = input(f"Attempt {self.guesses + 1}: Enter your guess (e.g., 1 2 3 4): ")
            guess = list(map(int, guess.split()))
            
            if len(guess) != self.code_length or any(color < 1 or color > self.num_colors for color in guess):
                print(f"Invalid guess. Please enter exactly {self.code_length} numbers between 1 and {self.num_colors}.")
                continue
            
            self.guesses += 1
            correct_position, correct_color = self.get_feedback(guess)
            print(f"Correct position: {correct_position}, Correct color (wrong position): {correct_color}")
            
            if correct_position == self.code_length:
                print(f"Congratulations! You've guessed the code {self.secret_code} in {self.guesses} attempts!")
                return
        
        print(f"Sorry, you've used all attempts. The secret code was {self.secret_code}.")

if __name__ == "__main__":
    game = Mastermind()
    game.play()