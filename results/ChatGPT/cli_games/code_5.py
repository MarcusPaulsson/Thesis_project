import random

class Mastermind:
    def __init__(self, code_length=4, num_colors=6, max_attempts=10):
        self.code_length = code_length
        self.num_colors = num_colors
        self.max_attempts = max_attempts
        self.code = self.generate_code()
        
    def generate_code(self):
        return [random.randint(1, self.num_colors) for _ in range(self.code_length)]

    def get_feedback(self, guess):
        exact_matches = sum(1 for i in range(self.code_length) if guess[i] == self.code[i])
        color_matches = sum(min(guess.count(x), self.code.count(x)) for x in set(guess)) - exact_matches
        return exact_matches, color_matches

    def play(self):
        print("Welcome to Mastermind!")
        print(f"Code length: {self.code_length}, Number of colors: {self.num_colors}")
        print("You have {} attempts to guess the code.".format(self.max_attempts))
        
        for attempt in range(1, self.max_attempts + 1):
            guess = input(f"Attempt {attempt}: Enter your guess (space-separated numbers from 1 to {self.num_colors}): ")
            guess = list(map(int, guess.split()))
            
            if len(guess) != self.code_length:
                print(f"Invalid guess length! Please enter exactly {self.code_length} numbers.")
                continue
            
            exact, color = self.get_feedback(guess)
            print(f"Feedback: {exact} exact matches, {color} color matches.")
            
            if exact == self.code_length:
                print("Congratulations! You've cracked the code!")
                return
            
        print(f"Sorry, you've run out of attempts. The code was: {self.code}")

if __name__ == "__main__":
    game = Mastermind()
    game.play()