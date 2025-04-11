def min_moves_to_reach_n(N):
    moves = float('inf')
    
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            j = N // i
            moves = min(moves, i + j - 2)
    
    return moves

N = int(input().strip())
print(min_moves_to_reach_n(N))