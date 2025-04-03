def min_seconds_to_close_tabs(n, pos, l, r):
    # If all tabs are already within the range [l, r]
    if l <= pos <= r:
        return 0
    
    # Calculate operations needed
    seconds = 0
    
    # Move to the leftmost tab in the range if necessary
    if pos < l:
        seconds += (l - pos)  # Move to tab l
        seconds += 1          # Close tabs to the left of l
    elif pos > r:
        seconds += (pos - r)  # Move to tab r
        seconds += 1          # Close tabs to the right of r
    
    # Close all tabs outside the segment
    if l > 1:  # Close left side if there are tabs to close
        seconds += 1
    if r < n:  # Close right side if there are tabs to close
        seconds += 1
    
    return seconds

# Read input
n, pos, l, r = map(int, input().split())
# Get the result and print it
print(min_seconds_to_close_tabs(n, pos, l, r))