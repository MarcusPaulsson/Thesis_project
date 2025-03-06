def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")


def check_win(board, player):
    """Checks if the given player has won."""
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def check_tie(board):
    """Checks if the game is a tie."""
    for row in board:
        if " " in row:
            return False  # There's an empty cell, so it's not a tie
    return True  # All cells are filled, so it's a tie


def get_player_move(board, player):
    """Gets the player's move from the user."""
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))

            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid row or column. Please enter values between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("That cell is already occupied. Please choose another cell.")
                continue

            return row, col

        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")


def play_tic_tac_toe():
    """Plays a game of Tic-Tac-Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize empty board
    current_player = "X"
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over:
        row, col = get_player_move(board, current_player)
        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_tie(board):
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_tic_tac_toe()