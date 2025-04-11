n, pos, l, r = map(int, input().split())

# If no tabs need to be closed
if l == 1 and r == n:
    print(0)
else:
    seconds = 0

    # Close tabs to the left of l
    if l > 1:
        if pos > l:
            seconds += (pos - l) + 1  # Move to l and close
        else:
            seconds += (l - pos) + 1  # Move to l and close
    else:
        if pos > 1:
            seconds += (pos - 1) + 1  # Move to 1 and close

    # Close tabs to the right of r
    if r < n:
        if pos < r:
            seconds += (r - pos) + 1  # Move to r and close
        else:
            seconds += (pos - r) + 1  # Move to r and close
    else:
        if pos < n:
            seconds += (n - pos) + 1  # Move to n and close

    print(seconds)