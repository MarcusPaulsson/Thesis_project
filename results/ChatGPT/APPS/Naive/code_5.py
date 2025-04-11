def min_seconds_to_close_tabs(n, pos, l, r):
    if l == 1 and r == n:
        return 0  # No tabs to close

    seconds = 0

    # Close tabs to the left of l
    if pos > l:
        seconds += (pos - l) + 1  # Move to l and close left
    else:
        seconds += (l - pos)  # Move to l

    # Close tabs to the right of r
    if pos < r:
        seconds += (r - pos) + 1  # Move to r and close right
    else:
        seconds += (pos - r)  # Move to r

    return seconds

# Read input
n, pos, l, r = map(int, input().split())
# Output the result
print(min_seconds_to_close_tabs(n, pos, l, r))