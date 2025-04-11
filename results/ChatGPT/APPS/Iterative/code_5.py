n, pos, l, r = map(int, input().split())

if l == 1 and r == n:
    print(0)
else:
    moves = 0
    
    if pos < l:
        moves += l - pos  # Move to the leftmost tab to close
        moves += (r - l + 1)  # Close all tabs to the right
    elif pos > r:
        moves += pos - r  # Move to the rightmost tab to close
        moves += (r - l + 1)  # Close all tabs to the left
    else:
        # Cursor is between l and r
        left_moves = (pos - l) + (r - l + 1)  # Move to l and close left
        right_moves = (r - pos) + (r - l + 1)  # Move to r and close right
        moves = min(left_moves, right_moves)

    print(moves)