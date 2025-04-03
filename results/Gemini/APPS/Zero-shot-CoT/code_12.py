def solve():
    n = int(input())
    s = input()
    
    golds = s.count('G')
    
    if golds == 0:
        print(0)
        return
    
    if golds == n:
        print(n)
        return
    
    max_len = 0
    for i in range(n):
        for j in range(n):
            temp_s = list(s)
            temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
            temp_s = "".join(temp_s)
            
            curr_len = 0
            max_curr_len = 0
            for k in range(n):
                if temp_s[k] == 'G':
                    curr_len += 1
                    max_curr_len = max(max_curr_len, curr_len)
                else:
                    curr_len = 0
            
            max_len = max(max_len, min(max_curr_len, golds))
    
    print(max_len)

solve()