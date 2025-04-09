def minimum_seconds(n, pos, l, r):
    if l == 1 and r == n:
        return 0  # No tabs need to be closed

    moves = 0

    # If there are tabs to close on the left
    if l > 1:
        if pos > l:  # Move cursor to the leftmost tab that needs to remain open
            moves += (pos - l)  # Move to l
        moves += 1  # Close tabs to the left of l

    # If there are tabs to close on the right
    if r < n:
        if pos < r:  # Move cursor to the rightmost tab that needs to remain open
            moves += (r - pos)  # Move to r
        moves += 1  # Close tabs to the right of r

    return moves

# Input
n, pos, l, r = map(int, input().split())
# Output
print(minimum_seconds(n, pos, l, r))