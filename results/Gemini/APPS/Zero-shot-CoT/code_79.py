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
        
        moves += (n_len - 1 - last_digit_idx)
        temp_n.pop(last_digit_idx)
        
        # Find the first digit of the suffix
        first_digit_idx = -1
        for i in range(len(temp_n) - 1, -1, -1):
            if temp_n[i] == suffix[0]:
                first_digit_idx = i
                break
        
        if first_digit_idx == -1:
            continue
        
        moves += (len(temp_n) - 1 - first_digit_idx)
        temp_n.pop(first_digit_idx)
        
        # Remove trailing zeroes
        trailing_zeroes = 0
        for i in range(0, len(temp_n)):
            if temp_n[i] == '0':
                trailing_zeroes += 1
            else:
                break
                
        moves += trailing_zeroes
        
        
        ans = min(ans, moves)
        
    if ans == float('inf'):
        print("-1")
    else:
        print(ans)

solve()