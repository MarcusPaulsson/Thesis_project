def min_moves_to_divisible_by_25(n: int) -> int:
    s = str(n)
    length = len(s)
    moves = float('inf')
    
    # Valid endings for divisibility by 25
    targets = ['00', '25', '50', '75']

    for target in targets:
        last_digit, first_digit = target[1], target[0]
        
        # Initialize positions as -1 (not found)
        pos_last = pos_first = -1
        
        # Find the position of the last digit in the target
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                pos_last = i
                break
        
        if pos_last == -1:
            continue  # Skip if last digit not found

        # Find the position of the first digit in the target before the last digit
        for i in range(pos_last - 1, -1, -1):
            if s[i] == first_digit:
                pos_first = i
                break
        
        if pos_first == -1:
            continue  # Skip if first digit not found
        
        # Calculate the moves required to bring first_digit next to last_digit
        moves_required = (length - 1 - pos_last) + (pos_first - (pos_last - 1))
        moves = min(moves, moves_required)

    return moves if moves != float('inf') else -1

# Read input
n = int(input().strip())
# Get result and print it
result = min_moves_to_divisible_by_25(n)
print(result)