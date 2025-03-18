def create_board(rows=6, cols=7):
    """Creates an empty Connect Four board."""
    return [[' ' for _ in range(cols)] for _ in range(rows)]


def print_board(board):
    """Prints the Connect Four board to the console."""
    cols = len(board[0])
    print('  ' + '  '.join(str(i + 1) for i in range(cols)))  # Column numbers
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
    print('+' + '---+' * cols)  # Bottom border


def drop_piece(board, col, piece):
    """Drops a piece into the specified column."""
    rows = len(board)
    for row in range(rows - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = piece
            return row  # Return the row where the piece landed
    return None  # Column is full


def is_valid_location(board, col):
    """Checks if a column is a valid location to drop a piece."""
    rows = len(board)
    return board[0][col] == ' ' and 0 <= col < len(board[0])


def winning_move(board, piece):
    """Checks if the last move resulted in a win."""
    rows = len(board)
    cols = len(board[0])

    # Check horizontal
    for row in range(rows):
        for col in range(cols - 3):
            if (board[row][col] == piece and
                    board[row][col + 1] == piece and
                    board[row][col + 2] == piece and
                    board[row][col + 3] == piece):
                return True

    # Check vertical
    for row in range(rows - 3):
        for col in range(cols):
            if (board[row][col] == piece and
                    board[row + 1][col] == piece and
                    board[row + 2][col] == piece and
                    board[row + 3][col] == piece):
                return True

    # Check positive diagonal
    for row in range(rows - 3):
        for col in range(cols - 3):
            if (board[row][col] == piece and
                    board[row + 1][col + 1] == piece and
                    board[row + 2][col + 2] == piece and
                    board[row + 3][col + 3] == piece):
                return True

    # Check negative diagonal
    for row in range(3, rows):
        for col in range(cols - 3):
            if (board[row][col] == piece and
                    board[row - 1][col + 1] == piece and
                    board[row - 2][col + 2] == piece and
                    board[row - 3][col + 3] == piece):
                return True

    return False


def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        if ' ' in row:
            return False
    return True


def get_player_move(board, player_number):
    """Gets a valid column choice from the player."""
    while True:
        try:
            col = int(input(f"Player {player_number}, choose a column (1-{len(board[0])}): ")) - 1
            if is_valid_location(board, col):
                return col
            else:
                print("Invalid column.  It's either full or out of bounds.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError:
            print("Invalid input. Column number out of range.")



def play_connect_four():
    """Plays a game of Connect Four."""
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    while not game_over:
        # Player turn
        if turn % 2 == 0:
            player = 1
            piece = 'X'
        else:
            player = 2
            piece = 'O'

        col = get_player_move(board, player)

        if drop_piece(board, col, piece) is not None:
            print_board(board)

            if winning_move(board, piece):
                print(f"Player {player} wins!")
                game_over = True
            elif is_board_full(board):
                print("It's a draw!")
                game_over = True
            else:
                turn += 1
        else:
            print("That column is full. Try again.")  # Should not happen due to input validation


if __name__ == "__main__":
    play_connect_four()