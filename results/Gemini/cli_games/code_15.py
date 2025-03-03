import random
import time

class Boggle:
    def __init__(self, size=4, duration=180):
        self.size = size
        self.duration = duration
        self.board = self.generate_board()
        self.words = set()
        self.dictionary = self.load_dictionary("dictionary.txt")  # Replace with your dictionary file
        self.score = 0
        self.start_time = None
        self.game_over = False

    def generate_board(self):
        dice = [
            "RIFOBX", "IFEHIE", "DENOWS", "UTOKNG",
            "HMRSAO", "LUPETS", "ACITOA", "YLGKUE",
            "QBMJOA", "EHISPN", "VETIGN", "ASREIL",
            "PPCSEA", "TSIOET", "SCTIEP", "NDTHRO"
        ]
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                die = random.choice(dice)
                row.append(random.choice(die))
            board.append(row)
        return board

    def load_dictionary(self, filename):
        try:
            with open(filename, "r") as f:
                return set(word.strip().upper() for word in f)
        except FileNotFoundError:
            print(f"Error: Dictionary file '{filename}' not found. Please create or provide a valid dictionary file.")
            exit()

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def is_valid_word(self, word):
        return (
            len(word) >= 3
            and word.upper() in self.dictionary
            and word not in self.words
            and self.find_word_on_board(word)
        )

    def find_word_on_board(self, word):
        word = word.upper()
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == word[0] and self.search_recursive(word, row, col, 0, set()):
                    return True
        return False

    def search_recursive(self, word, row, col, index, visited):
        if index == len(word):
            return True

        if (
            row < 0
            or row >= self.size
            or col < 0
            or col >= self.size
            or self.board[row][col] != word[index]
            or (row, col) in visited
        ):
            return False

        visited.add((row, col))
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_row = row + dr
                new_col = col + dc
                if self.search_recursive(word, new_row, new_col, index + 1, visited.copy()):
                    return True

        return False

    def play(self):
        self.start_time = time.time()
        print("Welcome to Boggle!")
        self.print_board()

        while not self.game_over:
            elapsed_time = time.time() - self.start_time
            remaining_time = max(0, self.duration - int(elapsed_time))
            print(f"\nTime remaining: {remaining_time} seconds")

            if remaining_time == 0:
                self.game_over = True
                break

            word = input("Enter a word (or 'quit' to end): ").strip()
            if word.lower() == "quit":
                self.game_over = True
                break

            if self.is_valid_word(word):
                self.words.add(word.upper())
                self.score += len(word) - 2  # Scoring: 3-letter word = 1 point, 4 = 2, etc.
                print(f"Valid word! Score: {self.score}")
            else:
                print("Invalid word. Try again.")

        print("\nGame Over!")
        print(f"Final Score: {self.score}")
        print("Words found:")
        for word in sorted(self.words):
            print(word)


if __name__ == "__main__":
    # Create a simple dictionary file for testing (dictionary.txt)
    # with one word per line, all uppercase
    # Example:
    # CAT
    # DOG
    # CODE
    # PYTHON
    # etc.

    game = Boggle()
    game.play()