n, pos, l, r = map(int, input().split())

if l == 1 and r == n:
    print(0)
else:
    time = 0
    # Close tabs to the left of l
    if pos < l:
        time += l - pos  # Move cursor to l
        time += 1        # Close left tabs
    elif pos > r:
        time += pos - r  # Move cursor to r
        time += 1        # Close right tabs
    else:
        # Move to the closest end to start closing
        if pos < l:
            time += l - pos  # Move cursor to l
            time += 1        # Close left tabs
            time += (r - l)  # Move right to r
            time += 1        # Close right tabs
        elif pos > r:
            time += pos - r  # Move cursor to r
            time += 1        # Close right tabs
            time += (r - l)  # Move left to l
            time += 1        # Close left tabs
        else:
            # If in the range [l, r], we can close both sides
            time += min(pos - l, r - pos) + 1 + (r - l) + 2  # Move to one side, close, move to other side, close

    print(time)