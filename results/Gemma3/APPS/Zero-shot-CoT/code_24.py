def solve():
    board = [list(input()) for _ in range(10)]
    
    def check_win(board):
        for i in range(10):
            for j in range(10):
                if board[i][j] == 'X':
                    # Check horizontal
                    count = 0
                    for k in range(max(0, j - 4), min(10, j + 5)):
                        if board[i][k] == 'X':
                            count += 1
                        else:
                            break
                    if count >= 5:
                        return True
                    
                    # Check vertical
                    count = 0
                    for k in range(max(0, i - 4), min(10, i + 5)):
                        if board[k][j] == 'X':
                            count += 1
                        else:
                            break
                    if count >= 5:
                        return True
                    
                    # Check diagonal (top-left to bottom-right)
                    count = 0
                    for k in range(-4, 5):
                        r, c = i + k, j + k
                        if 0 <= r < 10 and 0 <= c < 10:
                            if board[r][c] == 'X':
                                count += 1
                            else:
                                break
                    if count >= 5:
                        return True
                    
                    # Check diagonal (top-right to bottom-left)
                    count = 0
                    for k in range(-4, 5):
                        r, c = i + k, j - k
                        if 0 <= r < 10 and 0 <= c < 10:
                            if board[r][c] == 'X':
                                count += 1
                            else:
                                break
                    if count >= 5:
                        return True
        return False

    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                board[i][j] = 'X'
                if check_win(board):
                    print("YES")
                    return
                board[i][j] = '.'
    
    print("NO")

solve()