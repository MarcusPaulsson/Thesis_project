def solve():
    s = input()
    digits = [int(c) for c in s]
    
    ans = 6
    for sum1 in range(28): 
        for sum2 in range(28):
            if sum1 == sum2:
                
                for i in range(1000):
                    s1 = str(i).zfill(3)
                    if sum(int(c) for c in s1) == sum1:
                        
                        for j in range(1000):
                            s2 = str(j).zfill(3)
                            if sum(int(c) for c in s2) == sum2:
                                
                                count = 0
                                s1_digits = [int(c) for c in s1]
                                s2_digits = [int(c) for c in s2]
                                
                                for k in range(3):
                                    if digits[k] != s1_digits[k]:
                                        count += 1
                                for k in range(3):
                                    if digits[k+3] != s2_digits[k]:
                                        count += 1
                                
                                ans = min(ans, count)
    print(ans)

solve()