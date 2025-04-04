def min_moves_to_divisible_by_25(n: int) -> int:
    s = str(n)
    length = len(s)
    min_moves = float('inf')
    
    # We need to find pairs of digits that form 00, 25, 50, or 75
    targets = ['00', '25', '50', '75']
    
    for target in targets:
        last_digit = target[1]
        second_last_digit = target[0]
        
        # Find the position of the last digit in the target pair
        last_digit_pos = -1
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                last_digit_pos = i
                break
        
        if last_digit_pos == -1:
            continue  # Last digit of target not found, skip
        
        # Find the position of the second last digit in the target pair
        second_last_digit_pos = -1
        for i in range(last_digit_pos - 1, -1, -1):
            if s[i] == second_last_digit:
                second_last_digit_pos = i
                break
        
        if second_last_digit_pos == -1:
            continue  # Second last digit of target not found, skip
        
        # Calculate moves needed to bring these digits together
        moves = (last_digit_pos - second_last_digit_pos) + (length - 1 - last_digit_pos)
        min_moves = min(min_moves, moves)
    
    return min_moves if min_moves != float('inf') else -1

# Input reading
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))