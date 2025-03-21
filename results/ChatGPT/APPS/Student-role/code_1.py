def max_diagonal_moves(q, queries):
    results = []
    for n, m, k in queries:
        # Calculate the minimum required moves to reach (n, m)
        min_moves = max(n, m)
        
        # Check if it's possible to reach (n, m) in exactly k moves
        if k < min_moves or (k - min_moves) % 2 != 0:
            results.append(-1)
        else:
            # Maximum diagonal moves possible
            total_diagonal_moves = min(n, m)
            remaining_moves = k - min_moves
            
            # We can use remaining moves to either remain at the diagonal or go straight
            # Each remaining move can be either diagonal or straight, but we want to maximize diagonals
            max_diagonal_moves = total_diagonal_moves + remaining_moves
            
            results.append(max_diagonal_moves)
    
    return results

# Read input
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Get results
results = max_diagonal_moves(q, queries)

# Output results
for res in results:
    print(res)