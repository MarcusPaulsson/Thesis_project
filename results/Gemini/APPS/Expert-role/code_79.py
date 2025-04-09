def solve():
    n = input()
    n_len = len(n)
    
    ans = float('inf')
    
    for suffix in ["00", "25", "50", "75"]:
        temp_n = list(n)
        moves = 0
        
        # Find last digit of suffix in reverse
        last_digit = suffix[1]
        
        try:
            last_digit_index = -1
            for i in range(n_len - 1, -1, -1):
                if temp_n[i] == last_digit:
                    last_digit_index = i
                    break
            
            if last_digit_index == -1:
                continue
                
            moves += (n_len - 1) - last_digit_index
            del temp_n[last_digit_index]

            # Find second-to-last digit of suffix in reverse
            second_last_digit = suffix[0]

            second_last_digit_index = -1
            for i in range(len(temp_n) - 1, -1, -1):
                if temp_n[i] == second_last_digit:
                    second_last_digit_index = i
                    break
            
            if second_last_digit_index == -1:
                continue
                
            moves += (len(temp_n) - 1) - second_last_digit_index
            del temp_n[second_last_digit_index]
            
            # Remove leading zeros
            leading_zeros = 0
            for digit in temp_n:
                if digit == '0':
                    leading_zeros += 1
                else:
                    break
            
            moves += leading_zeros
            
            if len(temp_n) - leading_zeros == 0:
                continue
            
            ans = min(ans, moves)
        except:
            continue
            
    if ans == float('inf'):
        print("-1")
    else:
        print(ans)
        
solve()