def min_paint_for_cross(q, queries):
    results = []
    for n, m, picture in queries:
        row_black_count = [0] * n
        col_black_count = [0] * m
        
        # Count black cells in each row and column
        for i in range(n):
            for j in range(m):
                if picture[i][j] == '*':
                    row_black_count[i] += 1
                    col_black_count[j] += 1
        
        # Check for existing crosses
        found_cross = False
        for i in range(n):
            for j in range(m):
                if row_black_count[i] == m and col_black_count[j] == n:
                    found_cross = True
                    break
            if found_cross:
                break
        
        if found_cross:
            results.append(0)
            continue
        
        # Now we need to find the minimum paint needed
        min_paint = float('inf')
        
        for i in range(n):
            for j in range(m):
                if picture[i][j] == '.':
                    # Calculate the number of paints needed for (i, j)
                    paints_needed = (m - row_black_count[i]) + (n - col_black_count[j]) - (1 if picture[i][j] == '.' else 0)
                    min_paint = min(min_paint, paints_needed)
        
        results.append(min_paint)
    
    return results

# Reading input and preparing the queries
import sys
input = sys.stdin.read
data = input().splitlines()

q = int(data[0])
queries = []
index = 1
for _ in range(q):
    n, m = map(int, data[index].split())
    index += 1
    picture = data[index:index + n]
    queries.append((n, m, picture))
    index += n

results = min_paint_for_cross(q, queries)
for result in results:
    print(result)