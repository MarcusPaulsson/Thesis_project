class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'
        else:
            print("Invalid move! Try again.")

    def check_win(self):
        winning_conditions = [
            [self.board[i] for i in range(9) if i % 3 == j] for j in range(3)] + \
            [[self.board[i] for i in range(9) if i // 3 == j] for j in range(3)] + \
            [self.board[i] for i in [0, 1, 2, 3, 4, 5, 6, 7, 8] if i % 2 == 0]

        for condition in winning_conditions:
            if condition.count('X') == 3 or condition.count('O') == 3:
                return condition[0]
        if ' ' not in self.board:
            return 'Tie'
        return None

    def play_game(self):
        while True:
            self.print_board()
            position = int(input("Player {}: Enter your move (0-8): ".format(self.current_player)))
            self.make_move(position)
            winner = self.check_win()
            if winner:
                self.print_board()
                print("Player {} wins!".format(winner))
                break
            elif winner == 'Tie':
                self.print_board()
                print("The game ends in a tie!")
                break

game = TicTacToe()
game.play_game()
