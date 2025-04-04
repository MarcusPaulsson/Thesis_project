def can_alice_win(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # vertical, horizontal, diagonal, anti-diagonal
    n = 10  # size of the board

    def check_win(x, y):
        for dx, dy in directions:
            count = 1  # count includes the new 'X' we are placing
            # Check in the positive direction
            for step in range(1, 5):
                nx, ny = x + step * dx, y + step * dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'X':
                    count += 1
                else:
                    break
            # Check in the negative direction
            for step in range(1, 5):
                nx, ny = x - step * dx, y - step * dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'X':
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False

    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                if check_win(i, j):
                    return "YES"
    
    return "NO"

# Input reading
board = [input().strip() for _ in range(10)]
print(can_alice_win(board))