import random
import string

class Boggle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.generate_board()
        self.words = set()

    def generate_board(self):
        letters = string.ascii_uppercase
        return [[random.choice(letters) for _ in range(self.size)] for _ in range(self.size)]

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def is_valid_word(self, word):
        return word in self.words

    def add_word(self, word):
        self.words.add(word.upper())

    def find_words(self, word, visited, x, y):
        if not (0 <= x < self.size and 0 <= y < self.size):
            return

        if (x, y) in visited:
            return

        visited.add((x, y))
        word += self.board[x][y]

        if len(word) > 2 and self.is_valid_word(word):
            print(f'Found: {word}')
        
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    self.find_words(word, visited.copy(), x + dx, y + dy)

    def search_words(self):
        for x in range(self.size):
            for y in range(self.size):
                self.find_words("", set(), x, y)

    def load_dictionary(self, dictionary_file):
        with open(dictionary_file, 'r') as f:
            for line in f:
                self.add_word(line.strip())

def main():
    boggle = Boggle()
    boggle.load_dictionary('dictionary.txt')  # Ensure you have a dictionary file with words
    print("Boggle Board:")
    boggle.print_board()
    print("Searching for words...")
    boggle.search_words()

if __name__ == "__main__":
    main()