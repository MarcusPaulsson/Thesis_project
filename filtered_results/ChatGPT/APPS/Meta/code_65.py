def transform_moves(n, m):
    if m % n != 0:
        return -1
    
    ratio = m // n
    moves = 0
    
    while ratio > 1:
        if ratio % 2 == 0:
            ratio //= 2
            moves += 1
        elif ratio % 3 == 0:
            ratio //= 3
            moves += 1
        else:
            return -1
            
    return moves

# Read input
n, m = map(int, input().split())
# Print the result
print(transform_moves(n, m))