def min_moves(n, m):
    if m % n != 0:
        return -1
    
    k = m // n
    moves = 0
    
    while k > 1:
        if k % 2 == 0:
            k //= 2
            moves += 1
        elif k % 3 == 0:
            k //= 3
            moves += 1
        else:
            return -1
    
    return moves

# Read input
n, m = map(int, input().split())
print(min_moves(n, m))