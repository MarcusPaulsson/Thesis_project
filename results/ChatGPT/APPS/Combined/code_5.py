def min_seconds_to_close_tabs(n, pos, l, r):
    if l == 1 and r == n:
        return 0  # No tabs to close

    seconds = 0

    # Close tabs to the left of l
    if pos < l:
        seconds += l - pos  # Move to l
        seconds += 1  # Close left tabs
    elif pos > l:
        seconds += pos - l  # Move to l if needed
        seconds += 1  # Close left tabs

    # Close tabs to the right of r
    if pos > r:
        seconds += pos - r  # Move to r
        seconds += 1  # Close right tabs
    elif pos < r:
        seconds += r - pos  # Move to r if needed
        seconds += 1  # Close right tabs

    return seconds

# Example usage
n, pos, l, r = map(int, input().split())
print(min_seconds_to_close_tabs(n, pos, l, r))