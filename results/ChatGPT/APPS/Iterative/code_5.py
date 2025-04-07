def min_seconds_to_close_tabs(n, pos, l, r):
    if l == 1 and r == n:
        return 0  # No tabs to close

    seconds = 0

    # Adjust the cursor position if it's outside the range [l, r]
    if pos < l:
        seconds += (l - pos)  # Move right to l
        pos = l
    elif pos > r:
        seconds += (pos - r)  # Move left to r
        pos = r

    # Now pos is in the range [l, r]
    # Close tabs to the left if needed
    if l > 1:
        seconds += (l - 1)  # Close all tabs to the left of l

    # Close tabs to the right if needed
    if r < n:
        seconds += (n - r)  # Close all tabs to the right of r

    return seconds

# Read input
n, pos, l, r = map(int, input().split())
# Get the result and print it
print(min_seconds_to_close_tabs(n, pos, l, r))