def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    
    # Check for possible pairs of digits that can form 25 or 00
    target_pairs = ['00', '25', '50', '75']
    min_moves = float('inf')
    
    for pair in target_pairs:
        # Find the last digit of the pair
        last_digit = pair[1]
        last_digit_index = -1
        
        # Find the last occurrence of the last digit in the number
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                last_digit_index = i
                break
        
        if last_digit_index == -1:
            continue
        
        # Now find the first digit of the pair
        first_digit = pair[0]
        first_digit_index = -1
        
        # Find the first occurrence of the first digit before the last digit
        for i in range(last_digit_index - 1, -1, -1):
            if s[i] == first_digit:
                first_digit_index = i
                break
        
        if first_digit_index == -1:
            continue
        
        # Calculate moves to bring the first digit to the position before last digit
        moves = (last_digit_index - first_digit_index) + (last_digit_index - (first_digit_index + 1))
        min_moves = min(min_moves, moves)
    
    return min_moves if min_moves != float('inf') else -1

# Input
n = int(input().strip())
# Output
print(min_moves_to_divisible_by_25(n))