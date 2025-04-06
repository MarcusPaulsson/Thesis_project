def solve():
    s = input()
    digits = [int(c) for c in s]
    
    ans = 6
    
    for i in range(1000):
        s1 = str(i).zfill(3)
        sum1 = sum(int(c) for c in s1)
        
        for j in range(1000):
            s2 = str(j).zfill(3)
            sum2 = sum(int(c) for c in s2)
            
            if sum1 == sum2:
                
                t1 = [int(c) for c in s1]
                t2 = [int(c) for c in s2]
                
                diff = 0
                
                if digits[0] != t1[0]:
                    diff += 1
                if digits[1] != t1[1]:
                    diff += 1
                if digits[2] != t1[2]:
                    diff += 1
                if digits[3] != t2[0]:
                    diff += 1
                if digits[4] != t2[1]:
                    diff += 1
                if digits[5] != t2[2]:
                    diff += 1
                    
                ans = min(ans, diff)
                
    print(ans)
    
solve()