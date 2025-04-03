def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    
    # Find pairs of digits that can form 25 or 00
    targets = ['00', '25', '50', '75']
    min_moves = float('inf')
    
    for target in targets:
        target_length = len(target)
        # Find the last character of the target in reverse order
        j = length - 1
        # We need to find the target digits in the string
        for i in range(target_length - 1, -1, -1):
            while j >= 0 and s[j] != target[i]:
                j -= 1
            if j < 0:
                break
            # Once we found the digit, we move to the next digit in the target
            if i > 0:
                # Count the moves needed to bring the found digit next to the previous one
                min_moves += (j - (i if i == target_length - 1 else j + 1))
            j -= 1
        
        if j >= 0:  # This means we found all target digits
            moves = len(s) - (j + 1) - target_length + 1
            min_moves = min(min_moves, moves)
        
        # Reset min_moves for the next target
        min_moves = float('inf')

    return -1 if min_moves == float('inf') else min_moves

# Input reading
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))