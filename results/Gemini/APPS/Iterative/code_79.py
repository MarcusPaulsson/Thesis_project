def solve():
    n = input()
    n_len = len(n)
    
    ans = float('inf')
    
    for suffix in ["00", "25", "50", "75"]:
        
        temp_n = list(n)
        moves = 0
        
        # Find the last digit of the suffix
        
        idx2 = -1
        for i in range(n_len - 1, -1, -1):
            if temp_n[i] == suffix[1]:
                idx2 = i
                break
        
        if idx2 == -1:
            continue
        
        # Move the last digit to the end
        
        for i in range(idx2, n_len - 1):
            temp_n[i], temp_n[i+1] = temp_n[i+1], temp_n[i]
            moves += 1
        
        # Find the second to last digit of the suffix
        
        idx1 = -1
        for i in range(n_len - 2, -1, -1):
            if temp_n[i] == suffix[0]:
                idx1 = i
                break
                
        if idx1 == -1:
            continue
        
        # Move the second to last digit to the second to last position
        
        for i in range(idx1, n_len - 2):
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
        
        
        if n_len - 2 - leading_zeros < 0:
            continue
        ans = min(ans, moves)
        
    if ans == float('inf'):
        print("-1")
    else:
        print(ans)

solve()