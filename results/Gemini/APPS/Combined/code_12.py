def solve():
    n = int(input())
    s = input()
    
    golds = s.count('G')
    
    max_len = 0
    
    for i in range(n):
        if s[i] == 'S':
            temp_s = list(s)
            
            for j in range(n):
                if s[j] == 'G':
                    temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
                    temp_s = "".join(temp_s)
                    
                    current_len = 0
                    max_current_len = 0
                    for k in range(n):
                        if temp_s[k] == 'G':
                            current_len += 1
                        else:
                            max_current_len = max(max_current_len, current_len)
                            current_len = 0
                    max_current_len = max(max_current_len, current_len)
                    
                    max_len = max(max_len, max_current_len)
                    
                    temp_s = list(s)
                    break
    
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
    else:
        print(min(max_len, golds))

solve()