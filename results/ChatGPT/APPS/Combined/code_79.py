def min_moves_to_divisible_by_25(n: int) -> int:
    s = str(n)
    length = len(s)
    moves = float('inf')

    # Check for pairs of digits that can form 25 or 00
    for target in ['00', '25']:
        last_index = -1
        
        # Find the last occurrence of the last_digit
        for i in range(length - 1, -1, -1):
            if s[i] == target[1]:
                last_index = i
                break
        
        if last_index == -1:
            continue  # If we can't find the last_digit, skip this target
        
        second_last_index = -1
        
        # Now find the second_last_digit before the last_index
        for i in range(last_index - 1, -1, -1):
            if s[i] == target[0]:
                second_last_index = i
                break
        
        if second_last_index == -1:
            continue  # If we can't find the second_last_digit, skip this target
        
        # Calculate moves to bring second_last_index to the front of last_index
        moves_needed = (last_index - second_last_index) + (last_index - 1 - second_last_index)
        moves = min(moves, moves_needed)

    return moves if moves != float('inf') else -1

# Read input
n = int(input().strip())
# Get the result and print it
result = min_moves_to_divisible_by_25(n)
print(result)