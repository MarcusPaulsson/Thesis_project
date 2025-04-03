def solve():
    s = input()
    digits = [int(c) for c in s]
    
    ans = 6
    
    for i in range(1000):
        
        s1 = str(i).zfill(3)
        digits1 = [int(c) for c in s1]
        
        for j in range(1000):
            s2 = str(j).zfill(3)
            digits2 = [int(c) for c in s2]
            
            if sum(digits1) == sum(digits2):
                
                temp_ans = 0
                
                if digits[0] != digits1[0]:
                    temp_ans += 1
                if digits[1] != digits1[1]:
                    temp_ans += 1
                if digits[2] != digits1[2]:
                    temp_ans += 1
                if digits[3] != digits2[0]:
                    temp_ans += 1
                if digits[4] != digits2[1]:
                    temp_ans += 1
                if digits[5] != digits2[2]:
                    temp_ans += 1
                    
                ans = min(ans, temp_ans)
    
    print(ans)
    
solve()