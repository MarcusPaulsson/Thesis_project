def min_moves_to_reach_n(N):
    min_moves = float('inf')
    
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            j = N // i
            moves = (i - 1) + (j - 1)
            min_moves = min(min_moves, moves)
    
    return min_moves

N = int(input().strip())
print(min_moves_to_reach_n(N))