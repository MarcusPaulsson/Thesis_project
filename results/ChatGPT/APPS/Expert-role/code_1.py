def max_diagonal_moves(q, queries):
    results = []
    for n, m, k in queries:
        # Calculate the minimum moves required to reach (n, m)
        min_moves = max(n, m)
        
        # Check if it's possible to reach (n, m) in exactly k moves
        if min_moves > k or (k - min_moves) % 2 != 0:
            results.append(-1)
        else:
            # Calculate maximum diagonal moves
            diagonal_moves = min(n, m)
            remaining_moves = k - min_moves
            # Remaining moves can be used for horizontal/vertical moves
            max_diagonal = diagonal_moves + min(remaining_moves, abs(n - m))
            results.append(max_diagonal)
    
    return results

# Input reading
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Get results
results = max_diagonal_moves(q, queries)

# Output results
for result in results:
    print(result)