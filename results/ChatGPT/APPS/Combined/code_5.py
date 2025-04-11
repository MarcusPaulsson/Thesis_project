def minimum_seconds_to_close_tabs(n, pos, l, r):
    # If all tabs are within the range [l, r], no action is needed
    if l == 1 and r == n:
        return 0
    
    seconds = 0

    # Close tabs to the left of l if necessary
    if l > 1:
        seconds += abs(pos - l) + 1  # Move to l and close tabs to the left

    # Close tabs to the right of r if necessary
    if r < n:
        seconds += abs(pos - r) + 1  # Move to r and close tabs to the right

    return seconds