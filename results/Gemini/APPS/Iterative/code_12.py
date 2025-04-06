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
            
            found = False
            for j in range(n):
                if s[j] == 'G':
                    temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
                    found = True
                    break
            
            if found:
                temp_s = "".join(temp_s)
                
                curr_len = 0
                max_curr_len = 0
                
                for k in range(n):
                    if temp_s[k] == 'G':
                        curr_len += 1
                        max_curr_len = max(max_curr_len, curr_len)
                    else:
                        curr_len = 0
                
                max_len = max(max_len, max_curr_len)
    
    
    curr_len = 0
    max_curr_len = 0
    for k in range(n):
        if s[k] == 'G':
            curr_len += 1
            max_curr_len = max(max_curr_len, curr_len)
        else:
            curr_len = 0
    
    max_len = max(max_len, max_curr_len)
    
    
    if golds == n:
        print(n)
    else:
        print(min(max_len, golds))

solve()