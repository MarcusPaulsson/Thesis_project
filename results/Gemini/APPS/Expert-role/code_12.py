def solve():
    n = int(input())
    s = input()
    
    golds = s.count('G')
    
    max_len = 0
    
    for i in range(n):
        for j in range(n):
            temp_s = list(s)
            
            # Swap if i and j are different
            if i != j:
                temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
            
            current_len = 0
            max_current_len = 0
            
            for k in range(n):
                if temp_s[k] == 'G':
                    current_len += 1
                    max_current_len = max(max_current_len, current_len)
                else:
                    current_len = 0
            
            
            max_len = max(max_len, min(max_current_len, golds))
    
    print(max_len)

solve()