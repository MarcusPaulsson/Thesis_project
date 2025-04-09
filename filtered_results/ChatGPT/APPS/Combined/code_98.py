def min_moves_to_reach_n(N):
    min_moves = float('inf')
    
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            j = N // i
            # Calculate moves to reach (i, j)
            moves = (i - 1) + (j - 1)
            min_moves = min(min_moves, moves)
    
    return min_moves

if __name__ == "__main__":
    N = int(input().strip())
    print(min_moves_to_reach_n(N))