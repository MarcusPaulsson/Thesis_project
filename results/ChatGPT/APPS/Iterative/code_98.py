def min_moves_to_product(N):
    moves = float('inf')
    
    # Check every pair (i, j) such that i * j = N
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            j = N // i
            # Calculate moves to reach (i, j)
            current_moves = (i - 1) + (j - 1)
            moves = min(moves, current_moves)
    
    return moves

if __name__ == "__main__":
    N = int(input().strip())
    print(min_moves_to_product(N))