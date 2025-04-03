def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n, k = map(int, data[i].split())
        
        # Initialize grid
        grid = [[0] * n for _ in range(n)]
        
        # Fill the grid in a diagonal manner
        for idx in range(k):
            row = idx // n
            col = idx % n
            grid[row][col] = 1
        
        # Calculate row sums and column sums
        R = [sum(row) for row in grid]
        C = [sum(grid[j][i] for j in range(n)) for i in range(n)]
        
        max_R = max(R)
        min_R = min(R)
        max_C = max(C)
        min_C = min(C)
        
        f_A = (max_R - min_R) ** 2 + (max_C - min_C) ** 2
        
        results.append(str(f_A))
        for row in grid:
            results.append(''.join(map(str, row)))
    
    print('\n'.join(results))

# Call the function to execute
solve()