def min_moves_to_n(n):
    moves = float('inf')
    
    # Iterate over possible values for i from 1 to sqrt(n)
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            j = n // i
            moves = min(moves, (i - 1) + (j - 1))
    
    return moves

N = int(input())
print(min_moves_to_n(N))