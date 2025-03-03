import random
import string

class Boggle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.generate_board()
        self.valid_words = set()
        self.found_words = set()

    def generate_board(self):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return [[random.choice(letters) for _ in range(self.size)] for _ in range(self.size)]

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def load_words(self, word_list_file):
        with open(word_list_file, 'r') as f:
            for line in f:
                self.valid_words.add(line.strip().upper())

    def is_valid_word(self, word):
        return word in self.valid_words

    def find_words(self):
        for row in range(self.size):
            for col in range(self.size):
                self._search_word(row, col, "", set())

    def _search_word(self, row, col, current_word, visited):
        if (row < 0 or row >= self.size or col < 0 or col >= self.size or
                (row, col) in visited):
            return

        current_word += self.board[row][col]
        visited.add((row, col))

        if len(current_word) >= 3 and self.is_valid_word(current_word):
            self.found_words.add(current_word)

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    self._search_word(row + dr, col + dc, current_word, visited)

        visited.remove((row, col))

    def play(self):
        print("Welcome to Boggle!")
        self.display_board()
        self.find_words()
        print("Found words:")
        for word in sorted(self.found_words):
            print(word)

def main():
    boggle = Boggle()
    boggle.load_words("words.txt")  # Ensure you have a words.txt file with valid words
    boggle.play()

if __name__ == "__main__":
    main()