def min_seconds_to_close_tabs(n, pos, l, r):
    if l == 1 and r == n:
        return 0  # No tabs to close
    seconds = 0

    # Close tabs to the left of l
    if l > 1:
        if pos < l:
            seconds += (l - pos) + 1  # Move to l and close
        else:
            seconds += (pos - l) + 1  # Move to l and close
    else:
        seconds += 0  # No tabs to close on the left

    # Close tabs to the right of r
    if r < n:
        if pos > r:
            seconds += (pos - r) + 1  # Move to r and close
        else:
            seconds += (r - pos) + 1  # Move to r and close
    else:
        seconds += 0  # No tabs to close on the right

    return seconds

# Read input
n, pos, l, r = map(int, input().split())
# Output the result
print(min_seconds_to_close_tabs(n, pos, l, r))