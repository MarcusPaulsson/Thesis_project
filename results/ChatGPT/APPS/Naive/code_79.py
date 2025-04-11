def min_moves_to_divisible_by_25(n):
    n_str = str(n)
    length = len(n_str)
    
    # Possible endings for a number to be divisible by 25
    targets = ['00', '25', '50', '75']
    
    min_moves = float('inf')
    
    for target in targets:
        # Try to form the target at the end of the number
        target_len = len(target)
        j = length - 1
        
        # Count moves needed to place the target at the end
        for i in range(target_len - 1, -1, -1):
            while j >= 0 and n_str[j] != target[i]:
                j -= 1
            if j < 0:
                break
            # Count the moves needed to bring this digit to the end
            min_moves += (length - 1 - j)
            j -= 1
        
        # If we successfully placed all target digits
        if j >= -1:
            min_moves = min(min_moves, length - target_len)
    
    return min_moves if min_moves != float('inf') else -1

# Input reading
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))