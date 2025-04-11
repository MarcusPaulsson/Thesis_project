def min_seconds_to_close_tabs(n, pos, l, r):
    # If all tabs are within the range [l, r], no action is needed
    if l == 1 and r == n:
        return 0
    
    seconds = 0
    
    # Close tabs to the left of l
    if l > 1:
        # Move to l if not already there
        if pos < l:
            seconds += (l - pos)  # Move right to l
        else:
            seconds += (pos - l)  # Move left to l
        
        seconds += 1  # Close tabs to the left of l
    
    # Close tabs to the right of r
    if r < n:
        # Move to r if not already there
        if pos > r:
            seconds += (pos - r)  # Move left to r
        else:
            seconds += (r - pos)  # Move right to r
        
        seconds += 1  # Close tabs to the right of r
    
    return seconds

# Read input
n, pos, l, r = map(int, input().split())
# Print the result
print(min_seconds_to_close_tabs(n, pos, l, r))