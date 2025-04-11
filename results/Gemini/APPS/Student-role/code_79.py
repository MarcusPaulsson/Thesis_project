def solve():
    n = input()
    n_len = len(n)
    
    ans = float('inf')
    
    for suffix in ["00", "25", "50", "75"]:
        
        temp_n = list(n)
        moves = 0
        
        # Find the last digit of the suffix
        last_digit_idx = -1
        for i in range(n_len - 1, -1, -1):
            if temp_n[i] == suffix[1]:
                last_digit_idx = i
                break
        
        if last_digit_idx == -1:
            continue
        
        # Move the last digit to the end
        for i in range(last_digit_idx, n_len - 1):
            temp_n[i], temp_n[i+1] = temp_n[i+1], temp_n[i]
            moves += 1
        
        # Find the second to last digit of the suffix
        second_last_digit_idx = -1
        for i in range(n_len - 2, -1, -1):
            if temp_n[i] == suffix[0]:
                second_last_digit_idx = i
                break
        
        if second_last_digit_idx == -1:
            continue
        
        # Move the second to last digit to the second to last position
        for i in range(second_last_digit_idx, n_len - 2):
            temp_n[i], temp_n[i+1] = temp_n[i+1], temp_n[i]
            moves += 1
        
        # Remove leading zeros
        leading_zeros = 0
        for i in range(n_len - 2):
            if temp_n[i] == '0':
                leading_zeros += 1
            else:
                break
        
        moves += leading_zeros
        
        ans = min(ans, moves)
    
    if ans == float('inf'):
        print("-1")
    else:
        print(ans)

solve()