def min_minutes_to_cross(q, queries):
    results = []
    for n, m, grid in queries:
        # Count black cells in each row and each column
        row_black_counts = [0] * n
        col_black_counts = [0] * m
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    row_black_counts[i] += 1
                    col_black_counts[j] += 1
        
        # Find the minimum number of paints required for each possible cross
        min_paints = float('inf')
        
        for x in range(n):
            for y in range(m):
                if grid[x][y] == '.':
                    # Calculate needed paints for cross at (x, y)
                    total_paints = (n - row_black_counts[x]) + (m - col_black_counts[y])
                    min_paints = min(min_paints, total_paints)
        
        # If there's already a cross, no need to paint
        if min_paints == float('inf'):
            min_paints = 0
        
        results.append(min_paints)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

q = int(data[0])
queries = []
index = 1

for _ in range(q):
    n, m = map(int, data[index].split())
    grid = data[index + 1:index + 1 + n]
    queries.append((n, m, grid))
    index += 1 + n

# Get results
results = min_minutes_to_cross(q, queries)

# Print results
for result in results:
    print(result)