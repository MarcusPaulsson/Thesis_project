def min_seconds_to_close_tabs(n, pos, l, r):
    if l == 1 and r == n:
        return 0  # No tabs to close

    seconds = 0

    if pos < l:
        # Move to l and close left tabs, then move to r and close right tabs
        seconds += (l - pos) + 1 + (r - l) + 1
    elif pos > r:
        # Move to r and close right tabs, then move to l and close left tabs
        seconds += (pos - r) + 1 + (r - l) + 1
    else:
        # pos is between l and r
        if l > 1:
            seconds += (pos - l) + 1  # Move to l and close left tabs
        if r < n:
            seconds += (r - pos) + 1  # Move to r and close right tabs

    return seconds

# Example usage
n, pos, l, r = map(int, input().split())
print(min_seconds_to_close_tabs(n, pos, l, r))