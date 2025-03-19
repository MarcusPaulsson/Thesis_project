import random
import string

class Boggle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.generate_board()
        self.words_found = set()
        self.dictionary = self.load_dictionary()

    def generate_board(self):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return [[random.choice(letters) for _ in range(self.size)] for _ in range(self.size)]

    def load_dictionary(self):
        # A simple dictionary for demonstration; replace with a comprehensive word list.
        return set(word.strip().upper() for word in [
            "CAT", "DOG", "COT", "BAT", "RAT", "HAT", "HATTER", "TAT", "AT", "TO", "TOY", "BOG", "BOGGLE"
        ])

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def is_valid_word(self, word):
        return word in self.dictionary

    def find_words(self):
        for row in range(self.size):
            for col in range(self.size):
                self.search_word(row, col, "", set())

    def search_word(self, row, col, current_word, visited):
        if (row < 0 or col < 0 or row >= self.size or col >= self.size or
                (row, col) in visited):
            return
        
        current_word += self.board[row][col]
        visited.add((row, col))

        if self.is_valid_word(current_word):
            self.words_found.add(current_word)

        # Explore all 8 directions
        for r in range(-1, 2):
            for c in range(-1, 2):
                if r == 0 and c == 0:
                    continue
                self.search_word(row + r, col + c, current_word, visited)

        visited.remove((row, col))

    def play(self):
        print("Welcome to Boggle!")
        self.display_board()
        
        self.find_words()
        
        print("Words found:")
        for word in sorted(self.words_found):
            print(word)

if __name__ == "__main__":
    game = Boggle()
    game.play()