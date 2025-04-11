n, pos, l, r = map(int, input().split())

# If no tabs need to be closed
if l == 1 and r == n:
    print(0)
    exit()

# Calculate the number of seconds needed
seconds = 0

# Move to the leftmost tab that needs to be kept
if pos < l:
    seconds += l - pos  # Move to l
    seconds += 1  # Close to the left
elif pos > r:
    seconds += pos - r  # Move to r
    seconds += 1  # Close to the right
else:
    # If pos is within [l, r]
    left_close = (pos - l) + 1  # Move to l and close left
    right_close = (r - pos) + 1  # Move to r and close right
    seconds += min(left_close, right_close)

# Close the remaining tabs
if l > 1:
    seconds += 1  # Close left side if necessary
if r < n:
    seconds += 1  # Close right side if necessary

print(seconds)