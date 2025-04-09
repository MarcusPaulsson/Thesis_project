def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    
    # We need to check for pairs (0, 5) or (2, 5) or (5, 0)
    target_pairs = ['00', '25', '50', '75']
    min_moves = float('inf')
    
    for pair in target_pairs:
        first, second = pair
        
        # Check if we can find the second digit first
        pos_second = -1
        for i in range(length - 1, -1, -1):
            if s[i] == second:
                pos_second = i
                # Now look for the first digit before it
                for j in range(pos_second - 1, -1, -1):
                    if s[j] == first:
                        moves = (pos_second - j) + (length - 1 - pos_second)
                        min_moves = min(min_moves, moves)
                        break
                break
    
    return min_moves if min_moves != float('inf') else -1

# Read input
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))