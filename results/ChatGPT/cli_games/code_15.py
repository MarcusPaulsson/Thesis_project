import random
import string
import time

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
        with open('dictionary.txt', 'r') as file:
            return set(word.strip().upper() for word in file)

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def is_valid_word(self, word):
        return word in self.dictionary

    def find_words(self, word, x, y, visited):
        if not self.is_valid_word(word):
            return False
        
        if word in self.words_found:
            return False
        
        self.words_found.add(word)
        return True

    def search_word(self, word, x, y, visited):
        if (x, y) in visited:
            return
        
        visited.add((x, y))
        word += self.board[x][y]

        if self.find_words(word, x, y, visited):
            print(f"Found: {word}")

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < self.size and 0 <= y + dy < self.size:
                    self.search_word(word, x + dx, y + dy, visited)

        visited.remove((x, y))

    def play(self):
        print("Welcome to Boggle!")
        self.display_board()
        start_time = time.time()
        duration = 180  # 3 minutes

        while time.time() - start_time < duration:
            word = input("Enter a word (or 'exit' to quit): ").strip().upper()
            if word == 'EXIT':
                break
            if self.is_valid_word(word):
                self.search_word('', 0, 0, set())
            else:
                print("Invalid word or not found on the board.")

        print("Game over!")
        print("Words found:", self.words_found)

if __name__ == "__main__":
    game = Boggle()
    game.play()