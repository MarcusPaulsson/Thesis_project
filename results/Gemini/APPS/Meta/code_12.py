def solve():
    n = int(input())
    s = input()
    
    golds = s.count('G')
    
    max_len = 0
    for i in range(n):
        for j in range(n):
            temp = list(s)
            temp[i], temp[j] = temp[j], temp[i]
            temp_str = "".join(temp)
            
            current_len = 0
            max_current_len = 0
            for k in range(n):
                if temp_str[k] == 'G':
                    current_len += 1
                else:
                    max_current_len = max(max_current_len, current_len)
                    current_len = 0
            max_current_len = max(max_current_len, current_len)
            
            max_len = max(max_len, max_current_len)
    
    current_len = 0
    max_current_len = 0
    for k in range(n):
        if s[k] == 'G':
            current_len += 1
        else:
            max_current_len = max(max_current_len, current_len)
            current_len = 0
    max_current_len = max(max_current_len, current_len)

    max_len = max(max_len, max_current_len)
    
    if golds == 0:
        print(0)
        return
    
    if golds == n:
        print(n)
        return

    best_len = 0
    for i in range(n):
        for j in range(n):
            temp = list(s)
            temp[i], temp[j] = temp[j], temp[i]
            
            curr_len = 0
            max_curr_len = 0
            for k in range(n):
                if temp[k] == 'G':
                    curr_len += 1
                else:
                    max_curr_len = max(max_curr_len, curr_len)
                    curr_len = 0
            max_curr_len = max(max_curr_len, curr_len)
            
            best_len = max(best_len,min(max_curr_len, golds))

    print(best_len)

solve()