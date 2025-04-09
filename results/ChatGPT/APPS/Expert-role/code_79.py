def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    
    # Check for pairs of digits that make the number divisible by 25
    possible_pairs = [(0, 5), (2, 5), (5, 0), (7, 5)]
    found = False
    min_moves = float('inf')
    
    for i in range(length):
        for j in range(i + 1, length):
            if (s[i], s[j]) in possible_pairs:
                if s[j] != '0' or (j == length - 1):
                    # Calculate moves to bring s[i] to the correct position
                    # and s[j] to the position after s[i]
                    moves = (j - i) + (length - 1 - j)
                    min_moves = min(min_moves, moves)
                    found = True
    
    return min_moves if found else -1

# Input
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))