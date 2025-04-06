def solve():
    n = int(input())
    s = input()
    
    gold_count = s.count('G')
    
    if gold_count == 0:
        print(0)
        return
    
    if gold_count == n:
        print(n)
        return
    
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
                else:
                    max_current_len = max(max_current_len, current_len)
                    current_len = 0
            
            max_current_len = max(max_current_len, current_len)
            
            max_len = max(max_len, min(max_current_len, gold_count))
            
    print(max_len)

solve()