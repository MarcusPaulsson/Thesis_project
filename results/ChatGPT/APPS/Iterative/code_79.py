def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    moves = float('inf')

    for i in range(length - 1, 0, -1):
        if s[i] in '05':
            for j in range(i - 1, -1, -1):
                if s[j] in '27':
                    # Calculate moves needed to bring s[j] to the front and s[i] to the second position
                    moves_needed = (length - 1 - j) + (length - 1 - i) - 1
                    moves = min(moves, moves_needed)
                    break
                elif s[j] in '05':
                    # Calculate moves needed to bring s[j] to the front and s[i] to the second position
                    moves_needed = (length - 1 - j) + (length - 1 - i) - 1
                    moves = min(moves, moves_needed)
                    break

    return moves if moves != float('inf') else -1

n = int(input().strip())
print(min_moves_to_divisible_by_25(n))