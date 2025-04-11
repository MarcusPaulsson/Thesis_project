n, pos, l, r = map(int, input().split())

if l == 1 and r == n:
    print(0)
else:
    moves = 0
    if pos < l:
        moves += (l - pos) + 1  # Move to l and close left
    elif pos > r:
        moves += (pos - r) + 1  # Move to r and close right
    else:
        # Move to l and close left, then move to r and close right
        moves += min(pos - l, r - pos) + (r - l + 1) + 2  # Move to l and r, close both sides

    print(moves)