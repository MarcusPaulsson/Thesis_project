def solve():
    n = input()
    n_len = len(n)

    def calculate_moves(target):
        s = list(n)
        moves = 0
        
        # Find the last occurrence of target[1]
        idx2 = -1
        for i in range(n_len - 1, -1, -1):
            if s[i] == target[1]:
                idx2 = i
                break
        
        if idx2 == -1:
            return float('inf')
        
        # Move target[1] to the end
        for i in range(idx2, n_len - 1):
            s[i], s[i+1] = s[i+1], s[i]
            moves += 1
        
        # Find the last occurrence of target[0] before the last digit
        idx1 = -1
        for i in range(n_len - 2, -1, -1):
            if s[i] == target[0]:
                idx1 = i
                break
        
        if idx1 == -1:
            return float('inf')
        
        # Move target[0] to the second last position
        for i in range(idx1, n_len - 2):
            s[i], s[i+1] = s[i+1], s[i]
            moves += 1
        
        # Remove leading zeros
        first_digit_index = 0
        while first_digit_index < n_len - 2 and s[first_digit_index] == '0':
            first_digit_index += 1
            moves += 1
        
        return moves

    min_moves = min(calculate_moves("00"), calculate_moves("25"), calculate_moves("50"), calculate_moves("75"))
    
    if min_moves == float('inf'):
        print("-1")
    else:
        print(min_moves)

solve()