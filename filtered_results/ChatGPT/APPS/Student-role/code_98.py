def min_moves_to_reach_n(N):
    moves = float('inf')
    
    # Iterate over possible rows (i) from 1 to sqrt(N)
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            j = N // i
            # Calculate the moves needed to reach (i, j)
            moves = min(moves, (i - 1) + (j - 1))
    
    return moves

N = int(input().strip())
print(min_moves_to_reach_n(N))