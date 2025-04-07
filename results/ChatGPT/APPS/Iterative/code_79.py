def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    target_endings = ['00', '25', '50', '75']
    min_moves = float('inf')

    for ending in target_endings:
        last_digit, second_last_digit = ending[1], ending[0]

        # Find the position of the last digit first
        last_pos = -1
        for i in range(length - 1, -1, -1):
            if s[i] == last_digit:
                last_pos = i
                break

        if last_pos == -1:
            continue  # last digit not found

        # Now find the second last digit before the last digit
        second_last_pos = -1
        for i in range(last_pos - 1, -1, -1):
            if s[i] == second_last_digit:
                second_last_pos = i
                break

        if second_last_pos == -1:
            continue  # second last digit not found

        # Calculate moves to bring the second last digit to the front of last digit
        moves = (length - 1 - last_pos) + (last_pos - second_last_pos - 1)
        min_moves = min(min_moves, moves)

    return min_moves if min_moves != float('inf') else -1

# Input reading
n = int(input().strip())
print(min_moves_to_divisible_by_25(n))