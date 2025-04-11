n, pos, l, r = map(int, input().split())

if l == 1 and r == n:
    print(0)
else:
    seconds = 0
    
    if pos < l:
        seconds += l - pos  # Move to l
        seconds += 1  # Close left
        seconds += r - l  # Move to r
        seconds += 1  # Close right
    elif pos > r:
        seconds += pos - r  # Move to r
        seconds += 1  # Close right
        seconds += r - l  # Move to l
        seconds += 1  # Close left
    else:
        # pos is between l and r
        if pos < l:
            seconds += l - pos  # Move to l
            seconds += 1  # Close left
        elif pos > r:
            seconds += pos - r  # Move to r
            seconds += 1  # Close right
        
        # Close left if needed
        if l > 1:
            seconds += 1  # Close left
        # Close right if needed
        if r < n:
            seconds += 1  # Close right

    print(seconds)