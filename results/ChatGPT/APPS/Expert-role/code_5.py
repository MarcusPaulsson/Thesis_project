n, pos, l, r = map(int, input().split())

if l == 1 and r == n:
    print(0)
else:
    moves = 0
    if pos < l:
        moves += l - pos  # Move to l
        moves += 1  # Close left
        moves += r - l  # Move to r
        moves += 1  # Close right
    elif pos > r:
        moves += pos - r  # Move to r
        moves += 1  # Close right
        moves += r - l  # Move to l
        moves += 1  # Close left
    else:
        if pos < l:
            moves += l - pos  # Move to l
            moves += 1  # Close left
        elif pos > r:
            moves += pos - r  # Move to r
            moves += 1  # Close right
        
        moves += (r - l)  # Move from l to r
        moves += 1  # Close right
    
    print(moves)