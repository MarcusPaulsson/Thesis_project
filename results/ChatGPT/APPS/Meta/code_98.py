def min_moves_to_reach(N):
    moves = float('inf')
    
    # Loop over all possible i values
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:  # If i is a divisor of N
            j = N // i
            # Calculate moves required to reach (i, j)
            moves = min(moves, i + j - 2)
    
    return moves

# Read input
N = int(input().strip())
# Output the result
print(min_moves_to_reach(N))