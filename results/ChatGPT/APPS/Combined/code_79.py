def min_moves_to_divisible_by_25(n: int) -> int:
    s = str(n)
    length = len(s)
    min_moves = float('inf')

    # Check for pairs of digits that can form 00 or 25
    for target in ['00', '25']:
        moves = 0
        target_found = False

        for i in range(length - 1, -1, -1):
            if s[i] == target[1] and target_found:
                # Found the second digit of the target pair
                moves += (length - 1 - i)  # Moves to bring this digit to the end
                break
            elif s[i] == target[0]:
                # Found the first digit of the target pair
                target_found = True
            elif target_found:
                # Count moves to bring this digit to the end if we already found the first digit
                moves += 1

        if target_found and moves < min_moves:
            min_moves = moves

    return min_moves if min_moves != float('inf') else -1

# Example usage
n = int(input())
print(min_moves_to_divisible_by_25(n))