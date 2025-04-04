n, pos, l, r = map(int, input().split())

if l == 1 and r == n:
    print(0)  # No tabs to close
else:
    moves = 0

    # Move to the left side if needed
    if l > 1:
        if pos > l:
            moves += (pos - l)  # Move to the leftmost tab in segment
        moves += 1  # Close tabs to the left

    # Move to the right side if needed
    if r < n:
        if pos < r:
            moves += (r - pos)  # Move to the rightmost tab in segment
        moves += 1  # Close tabs to the right

    print(moves)