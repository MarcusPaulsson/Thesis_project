class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 'X'
    
    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.cols * 2 - 1))
        print(' '.join(str(i) for i in range(self.cols)))

    def drop_piece(self, col):
        if col < 0 or col >= self.cols:
            print("Invalid column. Choose a column between 0 and 6.")
            return False
        for row in reversed(range(self.rows)):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                return True
        print("Column is full. Choose another column.")
        return False

    def check_win(self):
        # Check horizontal, vertical, and diagonal for win
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if self.board[r][c] == self.current_player and all(self.board[r][c + i] == self.current_player for i in range(4)):
                    return True
        
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if self.board[r][c] == self.current_player and all(self.board[r + i][c] == self.current_player for i in range(4)):
                    return True
        
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if self.board[r][c] == self.current_player and all(self.board[r + i][c + i] == self.current_player for i in range(4)):
                    return True
        
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                if self.board[r][c] == self.current_player and all(self.board[r - i][c + i] == self.current_player for i in range(4)):
                    return True
        
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            col = int(input(f"Player {self.current_player}, choose a column (0-6): "))
            if self.drop_piece(col):
                if self.check_win():
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                self.switch_player()

if __name__ == "__main__":
    game = ConnectFour()
    game.play()