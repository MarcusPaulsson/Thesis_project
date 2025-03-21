def max_diagonal_moves(queries):
    results = []
    for n, m, k in queries:
        # Minimum moves required to reach (n, m) from (0, 0)
        min_moves = max(n, m)
        # Remaining moves after reaching the destination
        remaining_moves = k - min_moves
        
        # Check if it is possible to reach (n, m) in exactly k moves
        if remaining_moves < 0 or remaining_moves % 2 != 0:
            results.append(-1)
        else:
            # Maximum diagonal moves possible
            diagonal_moves = min(n, m)
            # Additional moves can be made in the same direction, thus
            # the maximum diagonal moves is min(n, m) + remaining_moves
            results.append(diagonal_moves + remaining_moves)
    
    return results

# Read input
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Get results and print
results = max_diagonal_moves(queries)
print("\n".join(map(str, results)))