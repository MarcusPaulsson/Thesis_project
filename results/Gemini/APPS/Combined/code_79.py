def solve():
    n = input()
    s = list(n)
    l = len(s)
    ans = float('inf')

    for suffix in ['00', '25', '50', '75']:
        temp_s = s[:]
        moves = 0
        
        # Find the last digit of the suffix
        last_digit_index = -1
        for i in range(l - 1, -1, -1):
            if temp_s[i] == suffix[1]:
                last_digit_index = i
                break
        
        if last_digit_index == -1:
            continue
        
        moves += l - 1 - last_digit_index
        temp_s.pop(last_digit_index)
        
        # Find the second to last digit of the suffix
        second_last_digit_index = -1
        for i in range(len(temp_s) - 1, -1, -1):
            if temp_s[i] == suffix[0]:
                second_last_digit_index = i
                break
        
        if second_last_digit_index == -1:
            continue
        
        moves += len(temp_s) - 1 - second_last_digit_index
        temp_s.pop(second_last_digit_index)
        
        # Remove leading zeros
        leading_zeros = 0
        for i in range(len(temp_s)):
            if temp_s[i] == '0':
                leading_zeros += 1
            else:
                break
        
        moves += leading_zeros
        
        if len(temp_s) == 0 and leading_zeros > 0:
            ans = min(ans, float('inf'))
        elif len(temp_s) > 0:
            ans = min(ans, moves)
    
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

solve()