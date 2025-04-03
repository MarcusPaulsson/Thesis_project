def solve():
    s = input()
    n = len(s)
    
    best_len = -1
    
    for i in range(n):
        if s[i] == '[':
            for j in range(i + 1, n):
                if s[j] == ':':
                    for k in range(j + 1, n):
                        for l in range(k, n):
                            if s[l] == ':':
                                for m in range(l + 1, n):
                                    if s[m] == ']':
                                        
                                        sub = s[i:m+1]
                                        
                                        
                                        first_bracket = -1
                                        first_colon = -1
                                        second_colon = -1
                                        second_bracket = -1
                                        
                                        
                                        for idx in range(len(sub)):
                                            if sub[idx] == '[':
                                                first_bracket = idx
                                                break
                                                
                                        for idx in range(first_bracket + 1, len(sub)):
                                            if sub[idx] == ':':
                                                first_colon = idx
                                                break
                                                
                                        for idx in range(len(sub) - 1, first_colon, -1):
                                            if sub[idx] == ']':
                                                second_bracket = idx
                                                break
                                                
                                        if second_bracket == -1:
                                            continue
                                        
                                        for idx in range(second_bracket - 1, first_colon, -1):
                                            if sub[idx] == ':':
                                                second_colon = idx
                                                break
                                                
                                        if first_bracket != 0 or first_colon == -1 or second_colon == -1 or second_bracket != len(sub) -1:
                                            continue
                                        
                                        
                                        num_pipes = 0
                                        for idx in range(first_colon + 1, second_colon):
                                            if sub[idx] == '|':
                                                num_pipes += 1
                                        
                                        curr_len = 2 + 2 + num_pipes
                                        
                                        best_len = max(best_len, curr_len)
                                        
    print(best_len)

solve()