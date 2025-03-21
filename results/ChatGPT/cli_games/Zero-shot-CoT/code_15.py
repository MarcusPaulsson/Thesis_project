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
        # Load a basic English words list, for demonstration purposes.
        # In practice, this could be a more extensive dictionary.
        return set(word.strip().upper() for word in open('dictionary.txt'))

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def is_valid_word(self, word):
        return word in self.dictionary

    def find_words(self, word, visited, x, y):
        if not self.is_valid_word(word):
            return False
        if word in self.words_found:
            return True

        self.words_found.add(word)
        return True

    def search(self, word, x, y, visited):
        if not (0 <= x < self.size and 0 <= y < self.size):
            return
        if (x, y) in visited:
            return

        visited.add((x, y))
        word += self.board[x][y]

        if self.is_valid_word(word):
            self.words_found.add(word)

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                self.search(word, x + dx, y + dy, visited)

        visited.remove((x, y))

    def play(self):
        print("Welcome to Boggle!")
        self.display_board()

        while True:
            command = input("Enter a word (or 'exit' to quit): ").strip().upper()
            if command == 'EXIT':
                break
            if self.is_valid_word(command):
                self.words_found.add(command)
                print(f"'{command}' is a valid word!")
            else:
                print(f"'{command}' is not a valid word.")
        
        print(f"You found {len(self.words_found)} words: {', '.join(sorted(self.words_found))}")

if __name__ == "__main__":
    game = Boggle()
    game.play()