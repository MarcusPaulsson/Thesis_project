n, pos, l, r = map(int, input().split())

# If all tabs are within the range l to r, no action is needed
if l == 1 and r == n:
    print(0)
    exit()

total_time = 0

# If there are tabs to the left of l
if l > 1:
    # Move to the left tab l
    total_time += abs(pos - l)  # Move to the leftmost needed tab
    total_time += 1  # Close all tabs to the left of l

# If there are tabs to the right of r
if r < n:
    # Move to the right tab r
    total_time += abs(pos - r)  # Move to the rightmost needed tab
    total_time += 1  # Close all tabs to the right of r

print(total_time)