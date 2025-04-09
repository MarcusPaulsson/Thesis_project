def solve():
    board = []
    for _ in range(10):
        board.append(input())

    def check_win(b):
        for i in range(10):
            for j in range(10):
                if b[i][j] == 'X':
                    # Check horizontal
                    if j <= 5:
                        count = 0
                        for k in range(5):
                            if b[i][j+k] == 'X':
                                count += 1
                        if count == 5:
                            return True

                    # Check vertical
                    if i <= 5:
                        count = 0
                        for k in range(5):
                            if b[i+k][j] == 'X':
                                count += 1
                        if count == 5:
                            return True

                    # Check diagonal (top-left to bottom-right)
                    if i <= 5 and j <= 5:
                        count = 0
                        for k in range(5):
                            if b[i+k][j+k] == 'X':
                                count += 1
                        if count == 5:
                            return True

                    # Check diagonal (top-right to bottom-left)
                    if i <= 5 and j >= 4:
                        count = 0
                        for k in range(5):
                            if b[i+k][j-k] == 'X':
                                count += 1
                        if count == 5:
                            return True
        return False

    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                temp_board = [list(row) for row in board]
                temp_board[i][j] = 'X'
                temp_board = ["".join(row) for row in temp_board]
                if check_win(temp_board):
                    print("YES")
                    return

    print("NO")

solve()