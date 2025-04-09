def solve():
    n = input()
    n_len = len(n)
    
    def calculate_moves(s, target):
        moves = 0
        s_list = list(s)
        
        # Find the last occurrence of the first digit of target
        first_digit_index = -1
        for i in range(n_len - 1, -1, -1):
            if s_list[i] == target[0]:
                first_digit_index = i
                break
        
        if first_digit_index == -1:
            return float('inf')
        
        # Move the first digit to the last position
        for i in range(first_digit_index, n_len - 1):
            s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
            moves += 1
        
        # Find the last occurrence of the second digit of target in the remaining digits
        second_digit_index = -1
        for i in range(n_len - 2, -1, -1):
            if s_list[i] == target[1]:
                second_digit_index = i
                break
        
        if second_digit_index == -1:
            return float('inf')
        
        # Move the second digit to the second to last position
        for i in range(second_digit_index, n_len - 2):
            s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
            moves += 1
            
        # Remove leading zeros
        leading_zeros = 0
        for i in range(n_len - 2):
            if s_list[i] == '0':
                leading_zeros += 1
            else:
                break

        
        return moves + leading_zeros
    
    min_moves = float('inf')
    
    min_moves = min(min_moves, calculate_moves(n, "00"))
    min_moves = min(min_moves, calculate_moves(n, "25"))
    min_moves = min(min_moves, calculate_moves(n, "50"))
    min_moves = min(min_moves, calculate_moves(n, "75"))
    
    if min_moves == float('inf'):
        print("-1")
    else:
        print(min_moves)
        

solve()