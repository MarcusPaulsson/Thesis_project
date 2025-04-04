def min_moves_to_divisible_by_25(n):
    n_str = str(n)
    length = len(n_str)
    
    # Check for possible pairs of digits that can form '00', '25', '50', '75'
    targets = ['00', '25', '50', '75']
    min_moves = float('inf')

    for target in targets:
        last_digit = target[1]
        first_digit = target[0]
        
        # Find last_digit first
        last_index = -1
        for i in range(length - 1, -1, -1):
            if n_str[i] == last_digit:
                last_index = i
                break
        
        if last_index == -1:
            continue  # Last digit not found, move to next target
        
        # Now find the first_digit before last_index
        first_index = -1
        for i in range(last_index - 1, -1, -1):
            if n_str[i] == first_digit:
                first_index = i
                break
        
        if first_index == -1:
            continue  # First digit not found, move to next target
        
        # Calculate moves to bring first_digit to the position before last_digit
        # Each swap brings first_digit closer by 1 position
        moves = (last_index - first_index) + (last_index - (first_index + 1))
        
        # Update minimum moves
        min_moves = min(min_moves, moves)
    
    return min_moves if min_moves != float('inf') else -1

# Example usage
n = int(input().strip())
result = min_moves_to_divisible_by_25(n)
print(result)