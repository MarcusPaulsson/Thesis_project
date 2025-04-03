n, pos, l, r = map(int, input().split())

# If all tabs within the desired segment are already open
if l == 1 and r == n:
    print(0)
else:
    seconds = 0

    # Close tabs to the left of l
    if pos < l:
        seconds += (l - pos)  # Move to l
        seconds += 1  # Close left
    elif pos >= l and pos <= r:
        # If the cursor is within the range, close left and right as needed
        if l > 1:
            seconds += (pos - l) + 1  # Move to l and close left
        if r < n:
            seconds += (r - pos) + 1  # Move to r and close right
    else:  # pos > r
        # Move to r and close left
        seconds += (pos - r) + 1  # Move to r
        if l > 1:
            seconds += (r - l + 1)  # Close left

    print(seconds)