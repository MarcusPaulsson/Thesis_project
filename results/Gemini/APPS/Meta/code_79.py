def solve():
    n = input()
    s = list(n)
    l = len(s)
    ans = float('inf')

    for suffix in ["00", "25", "50", "75"]:
        temp_s = s[:]
        
        # Find last digit of suffix
        last_digit_index = -1
        for i in range(l - 1, -1, -1):
            if temp_s[i] == suffix[1]:
                last_digit_index = i
                break
        
        if last_digit_index == -1:
            continue
        
        moves = 0
        for i in range(last_digit_index, l - 1):
            temp_s[i], temp_s[i+1] = temp_s[i+1], temp_s[i]
            moves += 1
        
        # Find second to last digit of suffix
        second_last_digit_index = -1
        for i in range(l - 2, -1, -1):
            if temp_s[i] == suffix[0]:
                second_last_digit_index = i
                break
        
        if second_last_digit_index == -1:
            continue
            
        for i in range(second_last_digit_index, l - 2):
            temp_s[i], temp_s[i+1] = temp_s[i+1], temp_s[i]
            moves += 1

        # Remove leading zeros
        first_non_zero_index = -1
        for i in range(l):
            if temp_s[i] != '0':
                first_non_zero_index = i
                break

        if first_non_zero_index == -1:
            continue

        moves += first_non_zero_index
        
        ans = min(ans, moves)
    
    if ans == float('inf'):
        print("-1")
    else:
        print(ans)

solve()