def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    moves = float('inf')
    
    # Check for pairs of digits that can form 25, 50, or 00
    for target in ['00', '25', '50']:
        last_digit = target[1]
        second_last_digit = target[0]
        
        # Find the last occurrence of the second_last_digit
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                # Now find the second last digit before the last_digit
                for j in range(i - 1, -1, -1):
                    if s[j] == second_last_digit:
                        # Calculate the moves needed to bring these digits together
                        moves_needed = (i - j)  # Moves to bring second_last_digit to just before last_digit
                        # We need to check if moving second_last_digit before last_digit won't create leading zeros
                        if not (target[0] == '0' and j == 0):
                            moves = min(moves, moves_needed)
                        break
                break

    return moves if moves != float('inf') else -1

# Read input
n = int(input().strip())
# Get the result
result = min_moves_to_divisible_by_25(n)
# Print the result
print(result)