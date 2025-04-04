n, pos, l, r = map(int, input().split())

# If the current segment already covers all tabs
if l == 1 and r == n:
    print(0)
    exit()

# Initialize the time counter
time = 0

# Close tabs to the left of segment
if l > 1:  # There are tabs to the left to close
    if pos > l:
        time += (pos - l)  # Move cursor to l
    time += 1  # Close all tabs to the left of l

# Move to the rightmost tab of the segment
if r < n:  # There are tabs to the right to close
    if pos < r:
        time += (r - pos)  # Move cursor to r
    time += 1  # Close all tabs to the right of r

print(time)