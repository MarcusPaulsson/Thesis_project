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
        
        moves += (n_len - 1 - idx2)
        del temp_n[idx2]
        
        # Find the first digit of the suffix
        
        idx1 = -1
        for i in range(len(temp_n) - 1, -1, -1):
            if temp_n[i] == suffix[0]:
                idx1 = i
                break
        
        if idx1 == -1:
            continue
        
        moves += (len(temp_n) - 1 - idx1)
        del temp_n[idx1]
        
        # Remove trailing zeros
        
        leading_zeros = 0
        for i in range(len(temp_n)):
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