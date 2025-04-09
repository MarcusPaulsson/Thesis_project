def count_moves(n, m):
    if m % n != 0:
        return -1
    
    ratio = m // n
    moves = 0
    
    while ratio > 1:
        if ratio % 2 == 0:
            ratio //= 2
        elif ratio % 3 == 0:
            ratio //= 3
        else:
            return -1
        moves += 1
    
    return moves

# Input reading
n, m = map(int, input().split())
print(count_moves(n, m))