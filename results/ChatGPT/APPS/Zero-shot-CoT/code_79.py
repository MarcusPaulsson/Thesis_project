def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    target_ends = ["00", "25", "50", "75"]
    min_moves = float('inf')
    
    for target in target_ends:
        # Try to form the target ending
        last_digit_pos = -1
        for i in range(length - 1, -1, -1):
            if last_digit_pos == -1 and s[i] == target[1]:
                last_digit_pos = i
            elif last_digit_pos != -1 and s[i] == target[0]:
                # Calculate moves needed to bring these two digits to the end
                moves = (length - 1 - last_digit_pos) + (last_digit_pos - i)
                min_moves = min(min_moves, moves)
                break

    return -1 if min_moves == float('inf') else min_moves

n = int(input().strip())
print(min_moves_to_divisible_by_25(n))