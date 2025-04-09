def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    min_moves = float('inf')

    # Check for pairs '00', '25', '50', '75'
    targets = ['00', '25', '50', '75']

    for target in targets:
        last_digit = target[1]
        second_last_digit = target[0]
        
        # We need to find last_digit first, then second_last_digit
        last_digit_index = -1
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                last_digit_index = i
                # Look for second_last_digit to the left of last_digit
                for j in range(last_digit_index - 1, -1, -1):
                    if s[j] == second_last_digit:
                        # Calculate moves: (last_digit_index - j) + (length - 1 - last_digit_index)
                        moves = (last_digit_index - j) + (length - 1 - last_digit_index)
                        min_moves = min(min_moves, moves)
                        break  # Found a valid pair, no need to search further for this last_digit
                break  # Move to the next target after finding the last_digit

    return min_moves if min_moves != float('inf') else -1

n = int(input().strip())
print(min_moves_to_divisible_by_25(n))