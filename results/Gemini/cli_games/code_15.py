import random
import time
import sys

class Boggle:
    def __init__(self, size=4, time_limit=180):
        self.size = size
        self.time_limit = time_limit
        self.board = self.generate_board()
        self.words = self.load_words("wordlist.txt")  # Replace with your wordlist file
        self.found_words = set()
        self.start_time = 0

    def generate_board(self):
        dice = [
            "RIFOBX", "IFEHSE", "OBJOBA", "HMQUMNI",
            "WEDSLG", "ITAEOL", "HRIUOB", "ENSIEU",
            "ATCIWO", "TLAEWR", "GONHES", "SMRZOI",
            "TOEISS", "ANEDVZ", "ANDELA", "SFPCAP"
        ]
        board = []
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                die = random.choice(dice)
                row.append(random.choice(die))
            board.append(row)
        return board

    def load_words(self, filename):
        try:
            with open(filename, "r") as f:
                words = set(word.strip().upper() for word in f)
            return words
        except FileNotFoundError:
            print(f"Error: Wordlist file '{filename}' not found.")
            sys.exit(1)

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def is_valid_word(self, word):
        return word in self.words and word not in self.found_words and len(word) >= 3

    def find_word(self, word):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == word[0]:
                    if self._search_recursive(word, row, col, 0, set()):
                        return True
        return False

    def _search_recursive(self, word, row, col, index, visited):
        if index == len(word):
            return True

        if (row < 0 or row >= self.size or
            col < 0 or col >= self.size or
            self.board[row][col] != word[index] or
            (row, col) in visited):
            return False

        visited.add((row, col))
        
        # Explore adjacent cells
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  # Skip the current cell
                new_row = row + dr
                new_col = col + dc
                if self._search_recursive(word, new_row, new_col, index + 1, visited.copy()):
                    return True
        
        return False

    def play(self):
        self.start_time = time.time()
        print("Welcome to Boggle!")
        self.print_board()
        print(f"You have {self.time_limit} seconds to find as many words as possible.")

        while time.time() - self.start_time < self.time_limit:
            remaining_time = self.time_limit - (time.time() - self.start_time)
            print(f"\nTime remaining: {int(remaining_time)} seconds")
            word = input("Enter a word (or type 'quit' to end): ").strip().upper()

            if word == "QUIT":
                break

            if self.is_valid_word(word) and self.find_word(word):
                self.found_words.add(word)
                print("Word found!")
            else:
                print("Invalid word or already found.")

        self.end_game()

    def end_game(self):
        print("\nTime's up!")
        print("Words found:")
        for word in sorted(self.found_words):
            print(word)

        score = self.calculate_score()
        print(f"Your score: {score}")

    def calculate_score(self):
        score = 0
        for word in self.found_words:
            length = len(word)
            if length == 3 or length == 4:
                score += 1
            elif length == 5:
                score += 2
            elif length == 6:
                score += 3
            elif length == 7:
                score += 5
            else:  # 8 or more
                score += 11
        return score


if __name__ == "__main__":
    boggle = Boggle()
    boggle.play()