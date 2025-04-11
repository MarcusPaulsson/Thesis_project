def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    
    # We need to find pairs of digits '00', '25', '50', '75'
    targets = ['00', '25', '50', '75']
    min_moves = float('inf')
    
    for target in targets:
        # Find the last digit of the target
        last_digit = target[1]
        first_digit = target[0]
        
        # Find the position of the last digit in the number
        last_pos = -1
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                last_pos = i
                break
        
        if last_pos == -1:
            continue
        
        # Now find the first digit before the last digit
        first_pos = -1
        for i in range(last_pos - 1, -1, -1):
            if s[i] == first_digit:
                first_pos = i
                break
        
        if first_pos == -1:
            continue
        
        # Calculate moves to bring first_pos to the left of last_pos
        moves = (length - 1 - last_pos) + (last_pos - first_pos - 1)
        min_moves = min(min_moves, moves)
    
    return min_moves if min_moves != float('inf') else -1

# Read input
n = int(input().strip())
# Get the result
result = min_moves_to_divisible_by_25(n)
# Print the result
print(result)