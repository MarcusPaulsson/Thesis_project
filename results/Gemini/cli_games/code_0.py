def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")


def check_win(board, player):
    """Checks if the given player has won the game."""
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def check_draw(board):
    """Checks if the board is full (draw)."""
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False  # There's still an empty space

    return True


def get_player_move(board, player):
    """Gets a valid move from the player."""
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))

            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid row or column.  Must be between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("That space is already taken. Try again.")
                continue

            return row, col

        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting.")
            exit()



def play_tic_tac_toe():
    """Main function to play the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize the board
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row, col = get_player_move(board, current_player)

        board[row][col] = current_player  # Make the move
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_tic_tac_toe()