n, pos, l, r = map(int, input().split())

# If all tabs are within the range l to r, no need to do anything
if l == 1 and r == n:
    print(0)
else:
    time = 0

    # Move to the leftmost needed tab if needed
    if pos < l:
        time += (l - pos)  # move to l
        time += 1          # close tabs to the left
    elif pos > r:
        time += (pos - r)  # move to r
        time += 1          # close tabs to the right
    else:
        # If cursor is within [l, r], close left and right as needed
        if l > 1:
            time += (pos - l) + 1  # move to l and close left
        if r < n:
            time += (r - pos) + 1  # move to r and close right

    print(time)