def min_seconds_to_close_tabs(n, pos, l, r):
    if l == 1 and r == n:
        return 0  # No tabs to close
    
    seconds = 0
    
    # Move to the left end of the segment
    if pos < l:
        seconds += l - pos  # Move to l
        seconds += 1  # Close tabs to the left
    else:
        # Close tabs to the left of l if needed
        if pos >= l:
            seconds += max(0, l - pos)  # Move to l if needed
            seconds += 1  # Close tabs to the left

    # Move to the right end of the segment
    if pos > r:
        seconds += pos - r  # Move to r
        seconds += 1  # Close tabs to the right
    else:
        # Close tabs to the right of r if needed
        if pos <= r:
            seconds += max(0, pos - r)  # Move to r if needed
            seconds += 1  # Close tabs to the right

    return seconds

# Read input
n, pos, l, r = map(int, input().split())
print(min_seconds_to_close_tabs(n, pos, l, r))