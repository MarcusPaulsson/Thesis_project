def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    
    # Possible pairs of digits that can form numbers divisible by 25
    target_pairs = ['00', '25', '50', '75']
    min_moves = float('inf')
    
    for target in target_pairs:
        last_digit = target[1]
        first_digit = target[0]
        
        # Find the last occurrence of the last digit
        last_digit_index = s.rfind(last_digit)
        if last_digit_index == -1:
            continue
        
        # Find the first occurrence of the first digit before the last digit
        first_digit_index = s.rfind(first_digit, 0, last_digit_index)
        if first_digit_index == -1:
            continue
        
        # Calculate moves to bring first_digit to the front of last_digit
        moves = (last_digit_index - first_digit_index) + (length - 1 - last_digit_index)
        min_moves = min(min_moves, moves)
    
    return min_moves if min_moves != float('inf') else -1

# Example usage:
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))