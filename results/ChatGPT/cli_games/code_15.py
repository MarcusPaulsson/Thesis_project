import random
import string

class Boggle:
    def __init__(self):
        self.board = self.generate_board()
        self.dictionary = self.load_dictionary()
        self.found_words = set()

    def generate_board(self):
        letters = [
            'A', 'A', 'A', 'E', 'E', 'E', 'E', 'I', 'I', 'I', 'L', 'L', 'N', 'N', 'O', 'O',
            'O', 'O', 'R', 'R', 'S', 'S', 'T', 'T', 'U', 'U', 'W', 'Y', 'B', 'C', 'D', 'F',
            'G', 'H', 'J', 'K', 'M', 'P', 'Q', 'V', 'X', 'Z'
        ]
        return [random.sample(letters, 4) for _ in range(4)]

    def load_dictionary(self):
        # Example dictionary, you can expand this with a real dictionary file or a larger set of words.
        return {
            'word', 'test', 'sample', 'boggle', 'game', 'play', 'code', 'python', 'hello',
            'world', 'example', 'random', 'letter', 'grid'
        }

    def display_board(self):
        print("Boggle Board:")
        for row in self.board:
            print(" ".join(row))
        print()

    def is_valid_word(self, word):
        return word in self.dictionary

    def find_words(self):
        print("Enter words (type 'exit' to finish):")
        while True:
            word = input("> ").strip().upper()
            if word == 'EXIT':
                break
            if self.is_valid_word(word):
                if word not in self.found_words:
                    self.found_words.add(word)
                    print(f"Found: {word}")
                else:
                    print("Already found this word.")
            else:
                print("Invalid word or not in dictionary.")

    def play(self):
        self.display_board()
        self.find_words()
        print("\nYou found the following words:")
        print(", ".join(self.found_words) if self.found_words else "No words found.")


if __name__ == "__main__":
    game = Boggle()
    game.play()