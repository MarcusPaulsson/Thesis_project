def min_moves_to_reach_n(N: int) -> int:
    min_moves = float('inf')

    # To find the factors of N
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            j = N // i
            # Calculate moves to (i, j)
            current_moves = (i - 1) + (j - 1)
            min_moves = min(min_moves, current_moves)

    return min_moves

# Read input
N = int(input().strip())
# Output the minimum moves
print(min_moves_to_reach_n(N))