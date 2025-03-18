def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print("-------------")
    for i in range(3):
        print("|", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2], "|")
        print("-------------")


def check_win(board, player):
    """Checks if the given player has won."""
    # Check rows
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False


def check_tie(board):
    """Checks if the game is a tie."""
    return all(board[i] != " " for i in range(9))


def get_player_move(board, player):
    """Gets a valid move from the player."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")


def play_tic_tac_toe():
    """Plays a game of Tic-Tac-Toe."""
    board = [" "] * 9
    player = "X"
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over:
        move = get_player_move(board, player)
        board[move] = player
        print_board(board)

        if check_win(board, player):
            print(f"Player {player} wins!")
            game_over = True
        elif check_tie(board):
            print("It's a tie!")
            game_over = True
        else:
            player = "O" if player == "X" else "X"


if __name__ == "__main__":
    play_tic_tac_toe()