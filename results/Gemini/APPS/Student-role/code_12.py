def solve():
    n = int(input())
    s = input()
    
    gold_count = s.count('G')
    
    if gold_count == 0:
        print(0)
        return
    
    max_beauty = 0
    
    for i in range(n):
        for j in range(n):
            temp_s = list(s)
            
            if i != j:
                temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
            
            current_beauty = 0
            max_current_beauty = 0
            
            for k in range(n):
                if temp_s[k] == 'G':
                    current_beauty += 1
                else:
                    max_current_beauty = max(max_current_beauty, current_beauty)
                    current_beauty = 0
            
            max_current_beauty = max(max_current_beauty, current_beauty)
            
            max_beauty = max(max_beauty, min(max_current_beauty, gold_count))
            
    print(max_beauty)
    

solve()