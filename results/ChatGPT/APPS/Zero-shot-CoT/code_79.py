def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    
    # Find pairs of digits that can form 25 or 00
    target_pairs = ['00', '25', '50', '75']
    min_moves = float('inf')
    
    for target in target_pairs:
        found = False
        for i in range(length - 1, -1, -1):
            if s[i] == target[1]:
                # We found the second digit of the target pair
                for j in range(i - 1, -1, -1):
                    if s[j] == target[0]:
                        # We found the first digit of the target pair
                        moves = (length - 1 - i) + (i - j - 1)
                        if j > 0 or target != '00':  # Ensure no leading zeros
                            min_moves = min(min_moves, moves)
                        found = True
                        break
            if found:
                break
    
    return min_moves if min_moves != float('inf') else -1

# Example usage
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))