def solve():
    n = input()
    n_len = len(n)
    
    ans = float('inf')
    
    for suffix in ["00", "25", "50", "75"]:
        
        temp_n = list(n)
        moves = 0
        
        # Find the last digit of the suffix
        last_digit = suffix[1]
        last_digit_index = -1
        for i in range(n_len - 1, -1, -1):
            if temp_n[i] == last_digit:
                last_digit_index = i
                break
        
        if last_digit_index == -1:
            continue
        
        moves += (n_len - 1 - last_digit_index)
        temp_n.pop(last_digit_index)
        
        # Find the first digit of the suffix
        first_digit = suffix[0]
        first_digit_index = -1
        for i in range(len(temp_n) - 1, -1, -1):
            if temp_n[i] == first_digit:
                first_digit_index = i
                break
        
        if first_digit_index == -1:
            continue
        
        moves += (len(temp_n) - 1 - first_digit_index)
        temp_n.pop(first_digit_index)
        
        # Remove trailing zeros
        trailing_zeros = 0
        for i in range(0, len(temp_n)):
            if temp_n[i] != '0':
                break
            trailing_zeros += 1
        
        moves += trailing_zeros
        
        if len(temp_n) - trailing_zeros > 0:
            ans = min(ans, moves)
    
    if ans == float('inf'):
        print("-1")
    else:
        print(ans)

solve()