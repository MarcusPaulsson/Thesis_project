def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    min_moves = float('inf')

    # Check for pairs of digits that can form 25 or 00
    for target in ['00', '25']:
        last_digit = target[1]
        first_digit = target[0]
        
        # Find the last occurrence of the last_digit
        last_index = -1
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                last_index = i
                break
        
        if last_index == -1:
            continue  # No last_digit found
        
        # Now find the first_digit before the last_digit
        first_index = -1
        for i in range(last_index - 1, -1, -1):
            if s[i] == first_digit:
                first_index = i
                break
        
        if first_index == -1:
            continue  # No first_digit found
        
        # Calculate moves to bring first_digit to the front of last_digit
        moves = (last_index - first_index) + (first_index)
        min_moves = min(min_moves, moves)

    return min_moves if min_moves != float('inf') else -1

# Read input
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))