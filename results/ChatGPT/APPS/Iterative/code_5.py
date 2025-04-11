n, pos, l, r = map(int, input().split())

if l == 1 and r == n:
    print(0)
else:
    moves = 0
    
    if pos < l:
        moves += l - pos  # Move to l
        moves += 1  # Close left
    elif pos > r:
        moves += pos - r  # Move to r
        moves += 1  # Close right
    else:
        # If pos is between l and r
        left_moves = (pos - l) + 1  # Move to l and close left
        right_moves = (r - pos) + 1  # Move to r and close right
        moves = min(left_moves, right_moves)

    # Close all tabs to the left of l if necessary
    if l > 1:
        moves += (l - 1)  # Close all tabs to the left of l
    # Close all tabs to the right of r if necessary
    if r < n:
        moves += (n - r)  # Close all tabs to the right of r

    print(moves)