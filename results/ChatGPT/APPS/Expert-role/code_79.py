def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    best_moves = float('inf')
    
    # Check for valid pairs (00, 25, 50, 75)
    targets = ['00', '25', '50', '75']
    
    for target in targets:
        last_digit = target[1]
        second_last_digit = target[0]
        
        # Find the positions of the last and second last digits
        last_index = -1
        second_last_index = -1
        
        for i in range(length-1, -1, -1):
            if s[i] == last_digit and last_index == -1:
                last_index = i
            elif s[i] == second_last_digit and last_index != -1:
                second_last_index = i
                # We can stop once we found both digits
                break
        
        if last_index != -1 and second_last_index != -1:
            # Calculate moves: 
            # We need to bring second_last_index to just before last_index
            moves = (length - 1 - last_index) + (last_index - second_last_index - 1)
            best_moves = min(best_moves, moves)
    
    return best_moves if best_moves != float('inf') else -1

# Input reading
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))