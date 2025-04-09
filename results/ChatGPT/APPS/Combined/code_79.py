def min_moves_to_divisible_by_25(n: int) -> int:
    s = str(n)
    length = len(s)
    target_pairs = ['00', '25', '50', '75']
    min_moves = float('inf')

    for pair in target_pairs:
        pos1 = pos2 = -1
        
        # Iterate through the string in reverse to find the required digits
        for i in range(length - 1, -1, -1):
            if s[i] == pair[1] and pos2 == -1:
                pos2 = i
            elif s[i] == pair[0] and pos2 != -1:
                pos1 = i
                break
        
        # Calculate moves if both positions are valid
        if pos1 != -1 and pos2 != -1:
            moves = (length - 1 - pos2) + (pos2 - pos1 - 1)
            min_moves = min(min_moves, moves)

    return min_moves if min_moves != float('inf') else -1

# Example usage
if __name__ == "__main__":
    n = int(input().strip())
    print(min_moves_to_divisible_by_25(n))