def solve():
    board = []
    for _ in range(10):
        board.append(input())

    def check_win(board):
        n = 10
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X':
                    # Check horizontal
                    if j <= n - 5:
                        win = True
                        for k in range(5):
                            if board[i][j+k] != 'X':
                                win = False
                                break
                        if win:
                            return True
                    # Check vertical
                    if i <= n - 5:
                        win = True
                        for k in range(5):
                            if board[i+k][j] != 'X':
                                win = False
                                break
                        if win:
                            return True
                    # Check diagonal (top-left to bottom-right)
                    if i <= n - 5 and j <= n - 5:
                        win = True
                        for k in range(5):
                            if board[i+k][j+k] != 'X':
                                win = False
                                break
                        if win:
                            return True
                    # Check diagonal (top-right to bottom-left)
                    if i <= n - 5 and j >= 4:
                        win = True
                        for k in range(5):
                            if board[i+k][j-k] != 'X':
                                win = False
                                break
                        if win:
                            return True
        return False

    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                temp_board = [list(row) for row in board]
                temp_board[i][j] = 'X'
                
                new_board = ["".join(row) for row in temp_board]
                
                if check_win(new_board):
                    print('YES')
                    return

    print('NO')

solve()