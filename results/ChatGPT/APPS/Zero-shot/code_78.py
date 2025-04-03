def min_minutes_to_cross(q, queries):
    results = []
    
    for n, m, grid in queries:
        row_black_count = [0] * n
        col_black_count = [0] * m
        
        # Count black cells in each row and column
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    row_black_count[i] += 1
                    col_black_count[j] += 1
        
        # Find the minimum number of paints required to get at least one cross
        min_paints = float('inf')
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '.':
                    # Calculate the number of paints to make this cell (i, j) part of a cross
                    paints_needed = (n - row_black_count[i]) + (m - col_black_count[j]) - (1 if row_black_count[i] + col_black_count[j] == 0 else 0)
                    min_paints = min(min_paints, paints_needed)
        
        # If there's already a cross, no paints are needed
        if min_paints == float('inf'):
            min_paints = 0
        
        results.append(min_paints)
    
    return results

# Read input
q = int(input())
queries = []
for _ in range(q):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    queries.append((n, m, grid))

# Process queries and print results
results = min_minutes_to_cross(q, queries)
for result in results:
    print(result)