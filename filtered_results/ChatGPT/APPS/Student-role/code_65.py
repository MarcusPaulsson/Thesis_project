def transform_moves(n, m):
    if m % n != 0:
        return -1

    quotient = m // n
    moves = 0

    while quotient > 1:
        if quotient % 2 == 0:
            quotient //= 2
            moves += 1
        elif quotient % 3 == 0:
            quotient //= 3
            moves += 1
        else:
            return -1

    return moves

# Input
n, m = map(int, input().split())
# Output
print(transform_moves(n, m))