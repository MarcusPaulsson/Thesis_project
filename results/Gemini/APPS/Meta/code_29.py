def solve():
    s = input()
    ans = 6
    for i in range(1000):
        s1 = str(i).zfill(3)
        for j in range(1000):
            s2 = str(j).zfill(3)
            if sum(int(d) for d in s1) == sum(int(d) for d in s2):
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