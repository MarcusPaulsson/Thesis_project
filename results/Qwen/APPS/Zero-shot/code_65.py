def game23(n, m):
    if n == m:
        return 0
    moves = 0
    while m > n:
        if m % 2 == 0:
            m //= 2
        elif m % 3 == 0:
            m //= 3
        else:
            return -1
        moves += 1
    if m == n:
        return moves
    else:
        return -1

n, m = map(int, input().split())
print(game23(n, m))