def minimum_seconds(n, pos, l, r):
    if l == 1 and r == n:
        return 0  # No tabs to close

    seconds = 0

    # Close tabs to the left of l
    if l > 1:
        if pos > l:
            seconds += pos - l  # Move to l
        else:
            seconds += l - pos  # Move to l
        seconds += 1  # Close tabs to the left

    # Close tabs to the right of r
    if r < n:
        if pos < r:
            seconds += r - pos  # Move to r
        else:
            seconds += pos - r  # Move to r
        seconds += 1  # Close tabs to the right

    return seconds

# Read input
n, pos, l, r = map(int, input().split())
print(minimum_seconds(n, pos, l, r))