def solve():
    s = input()
    ans = 6
    for sum_val in range(28):  # Max sum is 9+9+9 = 27, so range is 0 to 27 inclusive
        for i in range(1000):
            s1 = str(i).zfill(3)
            if sum(int(d) for d in s1) == sum_val:
                for j in range(1000):
                    s2 = str(j).zfill(3)
                    if sum(int(d) for d in s2) == sum_val:
                        diff = 0
                        for k in range(3):
                            if s[k] != s1[k]:
                                diff += 1
                        for k in range(3):
                            if s[k+3] != s2[k]:
                                diff += 1
                        ans = min(ans, diff)
    print(ans)

solve()