def minimum_seconds_to_close_tabs(n, pos, l, r):
    # If no tabs need to be closed
    if l == 1 and r == n:
        return 0

    seconds = 0

    if pos < l:
        # Move cursor to l and close tabs to the left
        seconds += (l - pos) + 1
    elif pos > r:
        # Move cursor to r and close tabs to the right
        seconds += (pos - r) + 1
    else:
        # Cursor is between l and r
        left_moves = (pos - l) + 1  # Move to l and close left
        right_moves = (r - pos) + 1  # Move to r and close right
        seconds += min(left_moves, right_moves)

    return seconds

# Read input
n, pos, l, r = map(int, input().split())
# Print the result
print(minimum_seconds_to_close_tabs(n, pos, l, r))