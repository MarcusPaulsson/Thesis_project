def min_seconds_to_close_tabs(n, pos, l, r):
    if l == 1 and r == n:
        return 0  # No tabs need to be closed
    
    seconds = 0
    
    # Close tabs to the left of l
    if pos < l:
        # Move cursor to l
        seconds += (l - pos) + 1  # Move to l and close
    elif pos > r:
        # Move cursor to r
        seconds += (pos - r) + 1  # Move to r and close
    else:
        # Cursor is between l and r
        if l > 1:
            seconds += (pos - l) + 1  # Move to l and close
        seconds += 1  # Close all tabs to the right of r
        if r < n:
            seconds += (r - pos) + 1  # Move to r
    
    return seconds

# Read input
n, pos, l, r = map(int, input().split())
print(min_seconds_to_close_tabs(n, pos, l, r))