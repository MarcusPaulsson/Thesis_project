def minimum_cost_to_make_fence_great(q, queries):
    results = []
    for query in queries:
        n, boards = query
        cost = 0
        
        # Initialize previous board height to a very small number
        prev_height = 0
        
        for i in range(n):
            a_i, b_i = boards[i]
            # If the current board height is the same as the previous one
            if a_i <= prev_height:
                # Calculate how much we need to raise this board
                needed_height = prev_height + 1
                # Calculate the cost to raise it
                cost += (needed_height - a_i) * b_i
                # Update current board height to the needed height
                a_i = needed_height
            
            # Update previous height to current board height
            prev_height = a_i
        
        results.append(cost)
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

index = 0
q = int(data[index])
index += 1
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

# Getting the results and printing them
results = minimum_cost_to_make_fence_great(q, queries)
for result in results:
    print(result)