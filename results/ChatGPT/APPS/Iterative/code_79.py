def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    target_pairs = ['00', '25', '50', '75']
    min_moves = float('inf')

    for pair in target_pairs:
        last_digit = pair[1]
        first_digit = pair[0]
        
        # Find the last occurrence of the second digit
        last_index = -1
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                last_index = i
                break
        
        if last_index == -1:
            continue
        
        # Now find the first occurrence of the first digit before the last_index
        first_index = -1
        for i in range(last_index - 1, -1, -1):
            if s[i] == first_digit:
                first_index = i
                break
        
        if first_index == -1:
            continue
        
        # Calculate moves to bring first_index to the position before last_index
        moves = (last_index - first_index) + (length - 1 - last_index)
        min_moves = min(min_moves, moves)

    return min_moves if min_moves != float('inf') else -1

# Input reading
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))