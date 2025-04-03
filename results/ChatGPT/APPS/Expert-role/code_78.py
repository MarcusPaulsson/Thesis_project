def min_paint_to_make_cross(q, queries):
    results = []
    for n, m, grid in queries:
        row_black_count = [0] * n
        col_black_count = [0] * m
        
        # Count the number of black cells in each row and column
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    row_black_count[i] += 1
                    col_black_count[j] += 1
        
        # Find the minimum number of paintings needed to create at least one cross
        min_paint = float('inf')
        for i in range(n):
            for j in range(m):
                # Calculate the number of paintings needed for cross at (i, j)
                total_needed = (m - row_black_count[i]) + (n - col_black_count[j])
                if grid[i][j] == '.':
                    total_needed -= 1  # If the intersection is white, we need to paint it too
                min_paint = min(min_paint, total_needed)

        results.append(min_paint)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

q = int(data[0])
queries = []
index = 1
for _ in range(q):
    n, m = map(int, data[index].split())
    index += 1
    grid = [data[index + i] for i in range(n)]
    queries.append((n, m, grid))
    index += n

# Get results
results = min_paint_to_make_cross(q, queries)

# Output results
for result in results:
    print(result)