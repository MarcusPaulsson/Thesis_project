import numpy as np

ROWS = 6
COLUMNS = 7
EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2

def create_board():
    return np.zeros((ROWS, COLUMNS), dtype=int)

def print_board(board):
    for row in board:
        print(" | ".join(str(int(cell)) for cell in row))
        print("-" * (COLUMNS * 4 - 3))

def is_valid_location(board, col):
    return board[ROWS - 1][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == EMPTY:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if all(board[r][c + i] == piece for i in range(4)):
                return True

    # Check vertical locations
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True

    # Check positively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

    return False

def main():
    board = create_board()
    game_over = False
    turn = 0

    print("Welcome to Connect Four!")
    print_board(board)

    while not game_over:
        col = int(input(f"Player {turn % 2 + 1}, make your selection (0-{COLUMNS - 1}): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, PLAYER1 if turn % 2 == 0 else PLAYER2)

            print_board(board)

            if winning_move(board, PLAYER1 if turn % 2 == 0 else PLAYER2):
                print(f"Player {turn % 2 + 1} wins!")
                game_over = True

            turn += 1

if __name__ == "__main__":
    main()