def minimum_seconds_to_close_tabs(n, pos, l, r):
    # If no tabs need to be closed, return 0
    if l == 1 and r == n:
        return 0

    seconds = 0

    # Determine if cursor needs to move to the leftmost or rightmost tab of the segment
    if pos < l:
        seconds += (l - pos) + 1  # Move to l and close tabs to the left
    elif pos > r:
        seconds += (pos - r) + 1  # Move to r and close tabs to the right
    else:
        # If the cursor is within the segment
        left_closing = (l - 1) - pos + 1 if l > 1 else 0  # Close left if needed
        right_closing = pos - (r + 1) + 1 if r < n else 0  # Close right if needed
        seconds += min(left_closing, right_closing) + (1 if left_closing or right_closing else 0)

    return seconds

# Read input and output the result
n, pos, l, r = map(int, input().strip().split())
print(minimum_seconds_to_close_tabs(n, pos, l, r))