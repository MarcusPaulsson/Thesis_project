def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n, k = map(int, data[i].split())
        
        # Create an n x n grid initialized to 0
        grid = [[0] * n for _ in range(n)]
        
        # Fill the grid with 1s in a diagonal pattern
        for j in range(k):
            row = j // n
            col = j % n
            grid[row][col] = 1
            
        # Calculate row sums and column sums
        row_sums = [sum(grid[r]) for r in range(n)]
        col_sums = [sum(grid[r][c] for r in range(n)) for c in range(n)]
        
        max_row = max(row_sums)
        min_row = min(row_sums)
        max_col = max(col_sums)
        min_col = min(col_sums)
        
        # Calculate f(A)
        f_value = (max_row - min_row) ** 2 + (max_col - min_col) ** 2
        
        # Store results
        results.append(f_value)
        for row in grid:
            results.append(''.join(map(str, row)))
    
    # Output results
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

# Uncomment the following line to run the function
# solve()