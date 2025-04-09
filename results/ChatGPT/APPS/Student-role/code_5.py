n, pos, l, r = map(int, input().split())

# If no tabs need to be closed
if l == 1 and r == n:
    print(0)
else:
    moves = 0

    # Close left tabs if needed
    if l > 1:
        if pos > l:
            moves += pos - l  # Move to l
        moves += 1  # Close left tabs

    # Close right tabs if needed
    if r < n:
        if pos < r:
            moves += r - pos  # Move to r
        moves += 1  # Close right tabs

    print(moves)