def min_moves_to_divisible_by_25(n):
    s = str(n)
    len_s = len(s)
    
    # To form a number divisible by 25, we need the last two digits to be 00, 25, 50, or 75
    targets = ['00', '25', '50', '75']
    
    min_moves = float('inf')
    
    for target in targets:
        # The last two digits we want
        last_digit = target[1]
        second_last_digit = target[0]
        
        # Find the position of the last digit from the end
        last_digit_index = -1
        for i in range(len_s - 1, -1, -1):
            if s[i] == last_digit:
                last_digit_index = i
                break
        
        # If we couldn't find the last digit, continue to the next target
        if last_digit_index == -1:
            continue
        
        # Now we need to find the second last digit before the last digit
        second_last_digit_index = -1
        for i in range(last_digit_index - 1, -1, -1):
            if s[i] == second_last_digit:
                second_last_digit_index = i
                break
        
        # If we couldn't find the second last digit, continue to the next target
        if second_last_digit_index == -1:
            continue
        
        # Calculate moves to bring second last digit to the position before last digit
        moves = (last_digit_index - second_last_digit_index) + (last_digit_index - (second_last_digit_index + 1))
        
        min_moves = min(min_moves, moves)
    
    return min_moves if min_moves != float('inf') else -1

# Input
n = int(input().strip())
# Output
print(min_moves_to_divisible_by_25(n))