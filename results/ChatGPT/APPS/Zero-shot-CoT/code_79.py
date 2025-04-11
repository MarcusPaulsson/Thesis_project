def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    
    # Check for possible pairs of digits that can form 25 or 00
    target_pairs = ['00', '25', '50', '75']
    min_moves = float('inf')
    
    for target in target_pairs:
        # Find the last digit of the target
        last_digit = target[1]
        first_digit = target[0]
        
        # Find the position of the last digit in the number
        last_digit_pos = -1
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                last_digit_pos = i
                break
        
        if last_digit_pos == -1:
            continue
        
        # Now find the first digit before the last digit found
        first_digit_pos = -1
        for i in range(last_digit_pos - 1, -1, -1):
            if s[i] == first_digit:
                first_digit_pos = i
                break
        
        if first_digit_pos == -1:
            continue
        
        # Calculate moves to bring last_digit to the end
        moves_to_end = length - 1 - last_digit_pos
        
        # Calculate moves to bring first_digit to the position before last_digit
        moves_to_first = last_digit_pos - first_digit_pos
        
        total_moves = moves_to_end + moves_to_first
        
        min_moves = min(min_moves, total_moves)
    
    return min_moves if min_moves != float('inf') else -1

# Input reading
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))