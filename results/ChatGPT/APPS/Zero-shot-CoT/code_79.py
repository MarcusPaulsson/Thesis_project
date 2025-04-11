def min_moves_to_divisible_by_25(n):
    s = str(n)
    length = len(s)
    target = ['0', '0', '2', '5']
    
    # Check for possible pairs of digits that can form 00, 25, 50, or 75
    pairs = [(0, 0), (2, 5), (5, 0), (7, 5)]
    
    min_moves = float('inf')
    
    for a, b in pairs:
        pos_a = -1
        pos_b = -1
        
        # Find the last occurrence of b and then the last occurrence of a before it
        for i in range(length - 1, -1, -1):
            if s[i] == str(b) and pos_b == -1:
                pos_b = i
            elif s[i] == str(a) and pos_b != -1:
                pos_a = i
                break
        
        if pos_a != -1 and pos_b != -1:
            # Calculate moves to bring b to the end and a before b
            moves = (length - 1 - pos_b) + (pos_b - pos_a - 1)
            min_moves = min(min_moves, moves)
    
    return min_moves if min_moves != float('inf') else -1

# Read input
n = int(input().strip())
# Get the result
result = min_moves_to_divisible_by_25(n)
# Print the result
print(result)