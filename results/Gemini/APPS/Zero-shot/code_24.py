def solve():
    grid = []
    for _ in range(10):
        grid.append(input())

    def check_win(grid):
        for i in range(10):
            for j in range(10):
                if grid[i][j] == 'X':
                    # Check horizontal
                    if j <= 5:
                        count = 0
                        for k in range(5):
                            if grid[i][j+k] == 'X':
                                count += 1
                        if count == 5:
                            return True

                    # Check vertical
                    if i <= 5:
                        count = 0
                        for k in range(5):
                            if grid[i+k][j] == 'X':
                                count += 1
                        if count == 5:
                            return True
                    
                    # Check diagonal (top-left to bottom-right)
                    if i <= 5 and j <= 5:
                        count = 0
                        for k in range(5):
                            if grid[i+k][j+k] == 'X':
                                count += 1
                        if count == 5:
                            return True

                    # Check diagonal (top-right to bottom-left)
                    if i <= 5 and j >= 4:
                        count = 0
                        for k in range(5):
                            if grid[i+k][j-k] == 'X':
                                count += 1
                        if count == 5:
                            return True
        return False

    for i in range(10):
        for j in range(10):
            if grid[i][j] == '.':
                new_grid = []
                for row in grid:
                    new_grid.append(list(row))
                new_grid[i][j] = 'X'
                new_grid = ["".join(row) for row in new_grid]
                
                if check_win(new_grid):
                    print("YES")
                    return

    print("NO")

solve()