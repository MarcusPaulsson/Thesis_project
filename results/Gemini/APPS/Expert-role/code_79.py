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
        
        moves += (n_len - 1) - last_digit_idx
        temp_n.pop(last_digit_idx)
        
        # Find the second last digit of the suffix
        
        second_last_digit_idx = -1
        for i in range(len(temp_n) - 1, -1, -1):
            if temp_n[i] == suffix[0]:
                second_last_digit_idx = i
                break
        
        if second_last_digit_idx == -1:
            continue
        
        moves += (len(temp_n) - 1) - second_last_digit_idx
        temp_n.pop(second_last_digit_idx)
        
        # Remove leading zeroes
        
        first_non_zero_idx = -1
        for i in range(len(temp_n)):
            if temp_n[i] != '0':
                first_non_zero_idx = i
                break
        
        if first_non_zero_idx == -1:
            moves += len(temp_n)
        else:
            moves += first_non_zero_idx
        
        ans = min(ans, moves)
        
    if ans == float('inf'):
        print("-1")
    else:
        print(ans)

solve()