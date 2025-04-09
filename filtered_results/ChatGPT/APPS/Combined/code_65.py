def moves_to_transform(n, m):
    if m % n != 0:
        return -1
    
    quotient = m // n
    moves = 0
    
    while quotient > 1:
        if quotient % 2 == 0:
            quotient //= 2
        elif quotient % 3 == 0:
            quotient //= 3
        else:
            return -1
        moves += 1
    
    return moves

# Input
n, m = map(int, input().split())
# Output
print(moves_to_transform(n, m))