def solve():
    s = input()
    digits = [int(c) for c in s]
    
    ans = 6
    
    for sum_val in range(28):  # Max sum of 3 digits is 9+9+9 = 27, plus 1 for range
        for i in range(1000):
            s1 = str(i).zfill(3)
            if sum(int(c) for c in s1) == sum_val:
                for j in range(1000):
                    s2 = str(j).zfill(3)
                    if sum(int(c) for c in s2) == sum_val:
                        
                        temp_digits = [int(c) for c in s1 + s2]
                        
                        diff = 0
                        for k in range(6):
                            if digits[k] != temp_digits[k]:
                                diff += 1
                        ans = min(ans, diff)
    print(ans)

solve()