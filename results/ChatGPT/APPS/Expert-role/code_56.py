def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    results = []
    
    for case in range(1, t + 1):
        n, k = map(int, data[case].split())
        
        # Prepare the grid
        grid = [[0] * n for _ in range(n)]
        
        # Fill the grid with 1s in a diagonal pattern
        row = 0
        col = 0
        
        for _ in range(k):
            grid[row][col] = 1
            col += 1
            if col == n:
                col = 0
                row += 1
            if row == n:
                break
        
        # Calculate R and C
        row_sums = [sum(grid[i]) for i in range(n)]
        col_sums = [sum(grid[i][j] for i in range(n)) for j in range(n)]
        
        max_row = max(row_sums)
        min_row = min(row_sums)
        max_col = max(col_sums)
        min_col = min(col_sums)
        
        # Calculate f(A)
        f_A = (max_row - min_row) ** 2 + (max_col - min_col) ** 2
        
        results.append(f_A)
        for line in grid:
            results.append(''.join(map(str, line)))
    
    # Print all results
    print("\n".join(map(str, results)))

# Invoke the solve function
solve()