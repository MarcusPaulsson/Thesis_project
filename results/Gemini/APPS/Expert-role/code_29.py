def solve():
    s = input()
    ans = 6
    for i in range(1000):
        s1 = str(i).zfill(3)
        for j in range(1000):
            s2 = str(j).zfill(3)
            if sum(int(d) for d in s1) == sum(int(d) for d in s2):
                cnt = 0
                temp = s1 + s2
                for k in range(6):
                    if s[k] != temp[k]:
                        cnt += 1
                ans = min(ans, cnt)
    print(ans)

solve()