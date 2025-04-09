def solve():
    n = input()
    n_len = len(n)
    
    def calculate_moves(s):
        moves = 0
        for i in range(len(s)):
            if s[i] == '0':
                for j in range(i, 0, -1):
                    s[j], s[j-1] = s[j-1], s[j]
                    moves += 1
                break
        return moves, s
    
    def remove_leading_zeros(s):
        first_digit_index = -1
        for i in range(len(s)):
            if s[i] != '0':
                first_digit_index = i
                break
        
        if first_digit_index == -1:
            return -1, []
        
        return 0, s[first_digit_index:]
    
    
    min_moves = float('inf')
    
    for suffix in ['00', '25', '50', '75']:
        temp_n = list(n)
        moves = 0
        
        # Find last digit of suffix
        last_digit = suffix[1]
        last_digit_index = -1
        for i in range(n_len - 1, -1, -1):
            if temp_n[i] == last_digit:
                last_digit_index = i
                break
        
        if last_digit_index == -1:
            continue
        
        # Move last digit to the end
        for i in range(last_digit_index, n_len - 1):
            temp_n[i], temp_n[i+1] = temp_n[i+1], temp_n[i]
            moves += 1
        
        # Find second last digit of suffix
        second_last_digit = suffix[0]
        second_last_digit_index = -1
        for i in range(n_len - 2, -1, -1):
            if temp_n[i] == second_last_digit:
                second_last_digit_index = i
                break
        
        if second_last_digit_index == -1:
            continue
        
        # Move second last digit to second last position
        for i in range(second_last_digit_index, n_len - 2):
            temp_n[i], temp_n[i+1] = temp_n[i+1], temp_n[i]
            moves += 1
            
        # Remove leading zeroes
        remove_zeroes_moves, remaining_digits = remove_leading_zeros(temp_n[:n_len-2])
        if remove_zeroes_moves == -1 :
            continue
            
        min_moves = min(min_moves, moves + remove_zeroes_moves)
    
    if min_moves == float('inf'):
        print("-1")
    else:
        print(min_moves)

solve()