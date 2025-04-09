def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    moves = float('inf')
    
    # Check for all pairs of digits that can form 00, 25, 50, 75
    for target in ["00", "25", "50", "75"]:
        last_digit = target[1]
        second_last_digit = target[0]
        
        # Find the position of the last digit first
        last_position = -1
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                last_position = i
                break
        
        if last_position == -1:
            continue
        
        # Now find the second last digit before the last digit found
        second_last_position = -1
        for i in range(last_position - 1, -1, -1):
            if s[i] == second_last_digit:
                second_last_position = i
                break
        
        # If we found both digits
        if second_last_position != -1:
            # The number of moves to bring them to the end
            move_count = (last_position - second_last_position) + (length - 1 - last_position)
            moves = min(moves, move_count)
    
    return moves if moves != float('inf') else -1

# Input reading
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))