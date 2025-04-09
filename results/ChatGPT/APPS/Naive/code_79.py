def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    moves = float('inf')

    # Look for pairs of digits that make the number divisible by 25
    for i in range(length - 1):
        for j in range(i + 1, length):
            if (s[i] == '0' and s[j] == '5') or (s[i] == '5' and s[j] == '0'):
                # Count moves to bring s[j] to s[i+1] and s[i] to s[i]
                moves_needed = (j - i) + (i + 1 - j)
                moves = min(moves, moves_needed)

    if moves == float('inf'):
        return -1
    return moves

# Input reading
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))