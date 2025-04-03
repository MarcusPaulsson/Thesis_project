def min_cost_to_make_fence_great(q, queries):
    results = []
    
    for query in queries:
        n, boards = query
        total_cost = 0
        
        # We will store the minimum cost to adjust each board
        cost = [0] * n
        
        # Process boards from left to right
        for i in range(n):
            if i > 0 and boards[i][0] <= boards[i-1][0]:
                # We need to increase the current board's height
                needed_height = boards[i-1][0] + 1
                increase = needed_height - boards[i][0]
                cost[i] = increase * boards[i][1]
                boards[i] = (needed_height, boards[i][1])
                total_cost += cost[i]
        
        # Process boards from right to left
        for i in range(n-2, -1, -1):
            if boards[i][0] >= boards[i+1][0]:
                # We need to increase the current board's height
                needed_height = boards[i+1][0] - 1
                increase = boards[i][0] - needed_height
                if increase > 0:
                    cost[i] += increase * boards[i][1]
                    boards[i] = (needed_height, boards[i][1])
                    total_cost += increase * boards[i][1]
        
        results.append(total_cost)
    
    return results

# Reading input and executing the function
import sys
input = sys.stdin.read
data = input().splitlines()

q = int(data[0])
index = 1
queries = []

for _ in range(q):
    n = int(data[index])
    index += 1
    boards = []
    for _ in range(n):
        a, b = map(int, data[index].split())
        boards.append((a, b))
        index += 1
    queries.append((n, boards))

results = min_cost_to_make_fence_great(q, queries)

for result in results:
    print(result)