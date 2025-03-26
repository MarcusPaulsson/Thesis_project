class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.player = 'X'
        self.turn = 1
        self.game_over = False
        self.winner = None

    def display_board(self):
        print('\n|' + '{} | {} | {} |'.format(self.board[0], self.board[1], self.board[2]) + '|')
        print('|' + '{} | {} | {} |'.format(self.board[3], self.board[4], self.board[5]) + '|')
        print('|' + '{} | {} | {} |\n'.format(self.board[6], self.board[7], self.board[8]) + '|')
        print('-----------------')

    def check_win(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ' and self.board[i] != ' ':
                self.game_over = True
                self.winner = self.board[i]
                return True
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ' and self.board[i] != '':
                self.game_over = True
                self.winner = self.board[i]
                return True
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            self.game_over = True
            self.winner = self.board[0]
            return True
        if self.board[2] == self.board[4] == self.board[6] != '':
            self.game_over = True
            self.winner = self.board[2]
            return True
        if self.board.count(' ') == 0 and not self.game_over:
            self.game_over = True
            self.winner = 'Tie'
            return True
        return False

    def play(self):
        self.display_board()
        while not self.game_over:
            try:
                move = int(input('Player {}, enter a number (1-9) to place your symbol: '.format(self.player))) - 1
            except ValueError:
                print('Invalid input! Try again.')
                continue
            if self.board[move] != ' ':
                print('Position already taken!')
                continue
            self.board[move] = self.player
            self.check_win()
            self.display_board()
            if self.game_over:
                if self.winner == 'Tie':
                    print('Tie game!')
                else:
                    print('{} wins!'.format(self.winner))
                return
            if self.turn % 2 == 0:
                self.player = 'O'
            else:
                self.player = 'X'
            self.turn += 1
            self.check_win()


game = TicTacToe()
game.play() 