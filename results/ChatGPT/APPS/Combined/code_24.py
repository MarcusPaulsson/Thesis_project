def can_alice_win(board):
    def check_win(x, y):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            
            # Check in the positive direction
            count += count_in_direction(x, y, dx, dy)
            # Check in the negative direction
            count += count_in_direction(x, y, -dx, -dy)
            
            if count >= 5:
                return True
        return False

    def count_in_direction(x, y, dx, dy):
        count = 0
        nx, ny = x + dx, y + dy
        while 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 'X':
            count += 1
            nx += dx
            ny += dy
        return count

    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                board[i][j] = 'X'  # Place Alice's cross
                if check_win(i, j):
                    return "YES"
                board[i][j] = '.'  # Reset the cell
    return "NO"