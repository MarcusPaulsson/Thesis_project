def solve():
    n = int(input())
    s = input()

    golds = s.count('G')

    if golds == 0:
        print(0)
        return

    max_len = 0
    for i in range(n):
        if s[i] == 'S':
            temp_s = list(s)
            
            
            
            best_len = 0
            for j in range(n):
                if temp_s[j] == 'G':
                    temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
                    
                    current_len = 0
                    max_current_len = 0
                    for k in range(n):
                        if temp_s[k] == 'G':
                            current_len += 1
                            max_current_len = max(max_current_len, current_len)
                        else:
                            current_len = 0
                    
                    best_len = max(best_len, min(max_current_len, golds))
                    
                    temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
            
            max_len = max(max_len, best_len)
    
    
    current_len = 0
    max_current_len = 0
    for k in range(n):
        if s[k] == 'G':
            current_len += 1
            max_current_len = max(max_current_len, current_len)
        else:
            current_len = 0
    
    max_len = max(max_len, min(max_current_len, golds))

    print(max_len)

solve()