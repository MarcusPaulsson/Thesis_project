n, pos, l, r = map(int, input().split())

# If all tabs are already in the range, no action is needed
if l <= pos <= r:
    # Close left and right if needed
    left_closes = pos - l
    right_closes = r - pos
    total_time = max(0, left_closes) + max(0, right_closes)
    print(total_time)
else:
    # Calculate the number of seconds to close tabs
    time = 0

    # If we need to close tabs on the left
    if pos < l:
        time += (l - pos)  # Move to l
        time += 1  # Close left tabs

    # If we need to close tabs on the right
    elif pos > r:
        time += (pos - r)  # Move to r
        time += 1  # Close right tabs

    # If we need to close both sides
    if l > 1:  # If there's something to close on the left
        time += (l - 1) + 1  # Move to l and close left

    if r < n:  # If there's something to close on the right
        time += (n - r) + 1  # Move to r and close right

    print(time)