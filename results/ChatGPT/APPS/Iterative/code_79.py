def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    
    # Target pairs for divisibility by 25
    targets = ['00', '25', '50', '75']
    
    min_moves = float('inf')
    
    for target in targets:
        last_digit = target[1]
        first_digit = target[0]
        
        last_index = -1
        first_index = -1
        
        # Search for the last character of the target in reverse
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                last_index = i
                # Now search for the first character of the target
                for j in range(last_index - 1, -1, -1):
                    if s[j] == first_digit:
                        first_index = j
                        break
                if first_index != -1:
                    # Calculate moves
                    moves = (last_index - first_index) + (last_index - 1 - first_index)
                    min_moves = min(min_moves, moves)
                break  # No need to continue searching once the last_index is found
        
    return min_moves if min_moves != float('inf') else -1

# Read input
n = int(input())
print(min_moves_to_divisible_by_25(n))