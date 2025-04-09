def solve():
    n = int(input())
    s = input()
    
    golds = s.count('G')
    
    max_len = 0
    for i in range(n):
        for j in range(n):
            temp_s = list(s)
            temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
            temp_s = "".join(temp_s)
            
            current_len = 0
            max_current_len = 0
            for k in range(n):
                if temp_s[k] == 'G':
                    current_len += 1
                    max_current_len = max(max_current_len, current_len)
                else:
                    current_len = 0
            
            max_len = max(max_len, max_current_len)
            
    
    
    
    
    original_len = 0
    max_original_len = 0
    current_original_len = 0
    for k in range(n):
        if s[k] == 'G':
            current_original_len += 1
            max_original_len = max(max_original_len, current_original_len)
        else:
            current_original_len = 0

    if golds == 0:
        print(0)
    elif golds == n:
        print(n)
    else:
        
        
        max_len = 0
        for i in range(n):
            temp_s = list(s)

            if temp_s[i] == 'S':
                
                
                for j in range(n):
                    if s[j] == 'G':
                        temp_s2 = list(s)
                        temp_s2[i], temp_s2[j] = temp_s2[j], temp_s2[i]
                        temp_s2 = "".join(temp_s2)
                        
                        current_len = 0
                        max_current_len = 0
                        for k in range(n):
                            if temp_s2[k] == 'G':
                                current_len += 1
                                max_current_len = max(max_current_len, current_len)
                            else:
                                current_len = 0
                        max_len = max(max_len, max_current_len)
        
        
        if max_len == 0:
            
            
            current_len = 0
            max_current_len = 0
            for k in range(n):
                if s[k] == 'G':
                    current_len += 1
                    max_current_len = max(max_current_len, current_len)
                else:
                    current_len = 0
            print(max_current_len)
        else:
            print(min(max_len, golds))
            
solve()