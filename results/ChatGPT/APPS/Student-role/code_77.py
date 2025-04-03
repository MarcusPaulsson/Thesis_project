def min_cost_to_make_fence_great(q, queries):
    results = []
    
    for query in queries:
        n = query[0]
        boards = query[1]
        
        # Cost to make the fence great
        total_cost = 0
        
        # We can keep track of the height we need to ensure no duplicates
        prev_height = -1
        
        for i in range(n):
            a_i, b_i = boards[i]
            
            # If the previous height is the same as the current height, we need to increase
            if a_i == prev_height:
                # We can increase this board's height
                # We have to choose the minimum cost option
                # We can increase it to `a_i + 1`, `a_i + 2`, ..., until it differs from `prev_height`
                # Cost for increasing this board to a_i + k is k * b_i
                # We need to find the minimum cost to make it different from prev_height
                
                # We can only increase it to a height greater than a_i
                # Calculate the cost to make it a_i + 1, a_i + 2, etc.
                # Start with a_i + 1
                if prev_height == a_i:
                    cost_to_increase = b_i  # For a_i + 1
                    total_cost += cost_to_increase
                    a_i += 1  # We assume we increased it by 1
            
            # Update previous height
            prev_height = a_i
            
        results.append(total_cost)
    
    return results

# Reading input and executing function
import sys
input = sys.stdin.read
data = input().splitlines()

q = int(data[0])
queries = []
index = 1

for _ in range(q):
    n = int(data[index])
    boards = []
    for i in range(n):
        a, b = map(int, data[index + 1 + i].split())
        boards.append((a, b))
    queries.append((n, boards))
    index += n + 1

results = min_cost_to_make_fence_great(q, queries)
print("\n".join(map(str, results)))