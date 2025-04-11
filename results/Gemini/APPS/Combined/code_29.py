def solve():
    s = input()
    digits = [int(c) for c in s]
    
    ans = 6
    
    for sum1 in range(0, 28):
        for sum2 in range(0, 28):
            if sum1 == sum2:
                
                count = 0
                
                for i in range(1000):
                    s1 = str(i).zfill(3)
                    if sum(int(c) for c in s1) == sum1:
                        for j in range(1000):
                            s2 = str(j).zfill(3)
                            if sum(int(c) for c in s2) == sum2:
                                temp_digits = [int(c) for c in s1 + s2]
                                
                                diff = 0
                                for k in range(6):
                                    if digits[k] != temp_digits[k]:
                                        diff += 1
                                ans = min(ans, diff)
    print(ans)

solve()