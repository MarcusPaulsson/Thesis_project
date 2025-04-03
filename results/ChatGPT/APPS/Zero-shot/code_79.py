def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    positions = []

    # Find positions of '0' and '5' to form '25' or '00'
    for i in range(length):
        if s[i] == '0' or s[i] == '5':
            positions.append((s[i], i))

    min_moves = float('inf')
    found = False

    # Check pairs of digits that can form '25', '00', or '75'
    for i in range(length):
        for j in range(i + 1, length):
            if (s[i], s[j]) in [('2', '5'), ('7', '5'), ('0', '0')]:
                if s[i] == '2' and s[j] == '5':
                    moves = (j - i) + (length - 1 - j)
                elif s[i] == '7' and s[j] == '5':
                    moves = (j - i) + (length - 1 - j)
                elif s[i] == '0' and s[j] == '0':
                    moves = (j - i) + (length - 1 - j)

                found = True
                min_moves = min(min_moves, moves)

    return min_moves if found else -1

# Input reading
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))