def max_diagonal_moves(q, queries):
    results = []
    for n, m, k in queries:
        # Calculate the minimum moves required to reach (n, m)
        min_moves = max(n, m)
        # Check if it's possible to reach (n, m) in exactly k moves
        if k < min_moves or (k - min_moves) % 2 != 0:
            results.append(-1)
        else:
            # The maximum number of diagonal moves we can make
            diagonal_moves = min(n, m)
            # Remaining moves after reaching the target
            remaining_moves = k - min_moves
            # Remaining moves can be used to move back and forth
            max_diagonal = diagonal_moves + min(remaining_moves, (n + m) - diagonal_moves)
            results.append(max_diagonal)
    
    return results

# Read input
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Get results
results = max_diagonal_moves(q, queries)

# Print results
for result in results:
    print(result)