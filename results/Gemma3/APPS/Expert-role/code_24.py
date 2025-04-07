def solve():
    grid = [list(input()) for _ in range(10)]
    
    def check_win(grid):
        for r in range(10):
            for c in range(10):
                if grid[r][c] == 'X':
                    # Check horizontal
                    count = 0
                    for i in range(max(0, c - 4), min(10, c + 5)):
                        if grid[r][i] == 'X':
                            count += 1
                        else:
                            break
                    if count >= 5:
                        return True
                    
                    # Check vertical
                    count = 0
                    for i in range(max(0, r - 4), min(10, r + 5)):
                        if grid[i][c] == 'X':
                            count += 1
                        else:
                            break
                    if count >= 5:
                        return True
                    
                    # Check diagonal (top-left to bottom-right)
                    count = 0
                    for i in range(-4, 5):
                        if 0 <= r + i < 10 and 0 <= c + i < 10 and grid[r + i][c + i] == 'X':
                            count += 1
                        else:
                            break
                    if count >= 5:
                        return True
                    
                    # Check diagonal (top-right to bottom-left)
                    count = 0
                    for i in range(-4, 5):
                        if 0 <= r + i < 10 and 0 <= c - i < 10 and grid[r + i][c - i] == 'X':
                            count += 1
                        else:
                            break
                    if count >= 5:
                        return True
        return False

    for r in range(10):
        for c in range(10):
            if grid[r][c] == '.':
                temp_grid = [row[:] for row in grid]
                temp_grid[r][c] = 'X'
                if check_win(temp_grid):
                    print("YES")
                    return
    
    print("NO")

solve()