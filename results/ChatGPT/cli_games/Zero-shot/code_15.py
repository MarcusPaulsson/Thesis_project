import random

class Boggle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.generate_board()
        self.valid_words = set()
        self.found_words = set()

    def generate_board(self):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return [[random.choice(letters) for _ in range(self.size)] for _ in range(self.size)]

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def load_dictionary(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                self.valid_words.add(line.strip().upper())

    def is_valid_word(self, word):
        return word in self.valid_words

    def find_words(self):
        for row in range(self.size):
            for col in range(self.size):
                self.search_word(row, col, "", set())

    def search_word(self, row, col, current_word, visited):
        if len(current_word) > 0 and self.is_valid_word(current_word):
            self.found_words.add(current_word)

        if len(current_word) >= 16:
            return

        for r in range(max(0, row - 1), min(self.size, row + 2)):
            for c in range(max(0, col - 1), min(self.size, col + 2)):
                if (r, c) not in visited:
                    visited.add((r, c))
                    self.search_word(r, c, current_word + self.board[r][c], visited)
                    visited.remove((r, c))

    def play(self):
        print("Welcome to Boggle!")
        self.print_board()
        self.find_words()
        print("Found Words:")
        for word in sorted(self.found_words):
            print(word)

if __name__ == "__main__":
    boggle = Boggle()
    boggle.load_dictionary('dictionary.txt')  # Make sure to have a valid dictionary file
    boggle.play()