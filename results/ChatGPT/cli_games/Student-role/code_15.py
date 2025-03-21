import random
import string

class Boggle:
    def __init__(self, size=4, word_list=None):
        self.size = size
        self.board = self.generate_board()
        self.word_list = word_list if word_list else set()
        self.found_words = set()

    def generate_board(self):
        letters = string.ascii_uppercase
        return [[random.choice(letters) for _ in range(self.size)] for _ in range(self.size)]

    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def load_words(self, file_path):
        with open(file_path, 'r') as file:
            self.word_list = set(word.strip().upper() for word in file)

    def is_valid_word(self, word):
        return word in self.word_list

    def search_word(self, word):
        visited = [[False] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if self._search_recursive(word, i, j, 0, visited):
                    return True
        return False

    def _search_recursive(self, word, x, y, index, visited):
        if index == len(word):
            return True
        if x < 0 or y < 0 or x >= self.size or y >= self.size or visited[x][y]:
            return False
        if self.board[x][y] != word[index]:
            return False

        visited[x][y] = True
        found = (self._search_recursive(word, x-1, y, index+1, visited) or
                 self._search_recursive(word, x+1, y, index+1, visited) or
                 self._search_recursive(word, x, y-1, index+1, visited) or
                 self._search_recursive(word, x, y+1, index+1, visited) or
                 self._search_recursive(word, x-1, y-1, index+1, visited) or
                 self._search_recursive(word, x-1, y+1, index+1, visited) or
                 self._search_recursive(word, x+1, y-1, index+1, visited) or
                 self._search_recursive(word, x+1, y+1, index+1, visited))

        visited[x][y] = False
        return found

    def play(self):
        print("Welcome to Boggle!")
        self.display_board()
        print("Enter words you find (type 'exit' to finish):")

        while True:
            word = input("> ").strip().upper()
            if word == 'EXIT':
                break
            if self.is_valid_word(word):
                if word not in self.found_words and self.search_word(word):
                    self.found_words.add(word)
                    print(f"Good job! '{word}' is a valid word!")
                else:
                    print(f"'{word}' is not found on the board or already used.")
            else:
                print(f"'{word}' is not a valid word.")

        print("Game Over! You found the following words:")
        print(", ".join(sorted(self.found_words)))


if __name__ == "__main__":
    game = Boggle()
    game.load_words("words.txt")  # Provide a path to a file with valid words
    game.play()