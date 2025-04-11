def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    moves = float('inf')

    # Check for pairs of digits that can form 00, 25, 50, or 75
    for target in ['00', '25', '50', '75']:
        last_digit = target[1]
        first_digit = target[0]
        
        # Find the last occurrence of the last_digit
        last_index = -1
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                last_index = i
                break
        
        if last_index == -1:
            continue
        
        # Now find the first_digit before last_index
        first_index = -1
        for i in range(last_index - 1, -1, -1):
            if s[i] == first_digit:
                first_index = i
                break
        
        if first_index == -1:
            continue
        
        # Calculate moves to bring first_digit to first_index and last_digit to last_index
        moves_to_first = last_index - first_index
        moves_to_last = last_index - first_index - 1
        
        total_moves = moves_to_first + moves_to_last
        moves = min(moves, total_moves)

    return moves if moves != float('inf') else -1

# Input reading
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))