import random
import string

class Boggle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.generate_board()
        self.dictionary = set()

    def generate_board(self):
        letters = [random.choice(string.ascii_uppercase) for _ in range(self.size * self.size)]
        return [letters[i * self.size:(i + 1) * self.size] for i in range(self.size)]

    def load_dictionary(self, words):
        self.dictionary = set(words)

    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def is_valid_word(self, word):
        return word in self.dictionary

    def find_words(self, word, x, y, visited, found_words):
        if not (0 <= x < self.size and 0 <= y < self.size) or (x, y) in visited:
            return
        
        visited.add((x, y))
        word += self.board[x][y]

        if self.is_valid_word(word):
            found_words.add(word)

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                self.find_words(word, x + dx, y + dy, visited, found_words)

        visited.remove((x, y))

    def play(self):
        print("Welcome to Boggle!")
        self.display_board()

        found_words = set()
        for x in range(self.size):
            for y in range(self.size):
                self.find_words("", x, y, set(), found_words)

        print("You found the following words:")
        for word in sorted(found_words):
            print(word)

# Example usage
if __name__ == "__main__":
    boggle_game = Boggle()
    boggle_game.load_dictionary(["CAT", "CART", "BAT", "BAR", "RAT", "ART", "TAB", "TAR", "AT", "A", "BATMAN"])
    boggle_game.play()