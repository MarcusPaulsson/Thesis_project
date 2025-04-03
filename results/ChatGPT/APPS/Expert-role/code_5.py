def minimum_seconds(n, pos, l, r):
    if l == 1 and r == n:
        return 0  # No tabs to close
    
    left_move = max(0, pos - l)  # Move to the leftmost required tab
    right_move = max(0, r - pos)  # Move to the rightmost required tab
    
    # Closing tabs to the left of l
    close_left = 1 if l > 1 else 0
    # Closing tabs to the right of r
    close_right = 1 if r < n else 0
    
    # Calculate total time
    total_time = left_move + close_left + right_move + close_right
    return total_time

# Input reading
n, pos, l, r = map(int, input().split())
print(minimum_seconds(n, pos, l, r))