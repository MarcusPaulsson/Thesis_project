import random
import string
import itertools

class Boggle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.generate_board()
        self.dictionary = self.load_dictionary()
        self.found_words = set()

    def generate_board(self):
        letters = [random.choice(string.ascii_uppercase) for _ in range(self.size * self.size)]
        return [letters[i:i + self.size] for i in range(0, len(letters), self.size)]

    def load_dictionary(self):
        # A small set of words for demonstration
        return {"BAT", "TAB", "CAT", "ACT", "COT", "DOG", "GOD", "HAT", "HARD", "HARDER", "ART", "CARD"}

    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def is_valid_word(self, word):
        return word in self.dictionary

    def find_words(self, word, x, y, visited):
        if len(word) > 1 and self.is_valid_word(word):
            self.found_words.add(word)
        
        if len(word) >= 16:  # Max length of a word is size squared
            return

        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) not in visited:
                visited.add((nx, ny))
                self.find_words(word + self.board[nx][ny], nx, ny, visited)
                visited.remove((nx, ny))

    def search_words(self):
        for x in range(self.size):
            for y in range(self.size):
                visited = {(x, y)}
                self.find_words(self.board[x][y], x, y, visited)

    def play(self):
        print("Welcome to Boggle!")
        self.display_board()
        self.search_words()
        print("Found words:", self.found_words)

if __name__ == "__main__":
    boggle_game = Boggle()
    boggle_game.play()