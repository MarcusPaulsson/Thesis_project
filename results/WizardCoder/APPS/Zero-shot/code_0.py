class Game:
    def __init__(self):
        self.board = [' ']*9
        self.reset()

    def mark(self, player):
        if player == "You":
            return "X" if self.player1 == "X" else "O"   # the opposite
        elif player == "Me":
            return self.player1                         # either X or O
        else:
             raise Exception(f'Invalid Player Mark "{mark}"')      # neither a playable player nor just a mark
    def print_board(self):
        print('\n'.join(' '.join(row) for row in (self.board[i*3 : i*3 + 3] for i in range(3))))
    def reset(self, first=True):
         self.player1 = "X" if first else "O"  # X goes first, O second
         self.player2 = self.mark("You")   if not first else self.mark("Me")

    def play_turn(self):
        self.reset(not self.player1 == "X") # if it's X's turn, reset for O; otherwise, do the opposite

    def play_game(self):
        while True:  # until a winner is decided or a draw occurs
            self.play_turn()   # switch to the other player's turn

if __name__ == "__main__":
     Game().play_game()
