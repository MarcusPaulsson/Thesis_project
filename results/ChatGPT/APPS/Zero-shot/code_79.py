def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    moves = float('inf')

    # Check for pairs of digits that can form 25 or 00
    for target in ['00', '25', '50', '75']:
        last_digit = target[1]
        second_last_digit = target[0]
        
        # Find the last occurrence of the last_digit
        last_index = -1
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                last_index = i
                break
        
        if last_index == -1:
            continue
        
        # Now find the second_last_digit before last_index
        second_last_index = -1
        for i in range(last_index - 1, -1, -1):
            if s[i] == second_last_digit:
                second_last_index = i
                break
        
        if second_last_index == -1:
            continue
        
        # Calculate moves to bring second_last_index to the front of last_index
        moves_needed = (last_index - second_last_index) + (length - 1 - last_index)
        moves = min(moves, moves_needed)

    return moves if moves != float('inf') else -1

n = int(input().strip())
print(min_moves_to_divisible_by_25(n))