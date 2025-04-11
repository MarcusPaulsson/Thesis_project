def minimum_seconds(n, pos, l, r):
    if l == 1 and r == n:
        return 0  # No tabs to close

    seconds = 0

    # Close tabs to the left of l
    if l > 1:
        if pos > l:
            seconds += (pos - l) + 1  # Move to l and close
        else:
            seconds += (l - pos) + 1  # Move to l and close
    else:
        seconds += 0  # No tabs to close on the left

    # Close tabs to the right of r
    if r < n:
        if pos < r:
            seconds += (r - pos) + 1  # Move to r and close
        else:
            seconds += (pos - r) + 1  # Move to r and close

    return seconds

# Input reading
n, pos, l, r = map(int, input().split())
print(minimum_seconds(n, pos, l, r))