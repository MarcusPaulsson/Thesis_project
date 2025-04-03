def min_cost_to_make_fence_great(q, queries):
    results = []
    
    for n, boards in queries:
        # We will keep track of the minimum cost to ensure no adjacent boards have the same height
        cost = 0
        
        # We can try to adjust each board to a height that ensures uniqueness
        # We only need to check adjacent pairs
        for i in range(n):
            # We need to check if the current board height is equal to the previous one
            if i > 0 and boards[i][0] <= boards[i - 1][0]:
                # Calculate how much we need to increase the current board
                needed_increase = boards[i - 1][0] - boards[i][0] + 1
                cost += needed_increase * boards[i][1]
                # Increase the height of the current board to maintain uniqueness
                boards[i] = (boards[i][0] + needed_increase, boards[i][1])
        
        results.append(cost)
    
    return results

# Read input data
import sys
input = sys.stdin.read
data = input().splitlines()

# Process input
index = 0
q = int(data[index])
index += 1
queries = []

for _ in range(q):
    n = int(data[index])
    index += 1
    boards = []
    for __ in range(n):
        a, b = map(int, data[index].split())
        boards.append((a, b))
        index += 1
    queries.append((n, boards))

# Get results
results = min_cost_to_make_fence_great(q, queries)

# Output results
for result in results:
    print(result)