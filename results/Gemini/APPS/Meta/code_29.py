def solve():
    s = input()
    ans = 6
    for i in range(1000):
        s1 = str(i).zfill(3)
        for j in range(1000):
            s2 = str(j).zfill(3)
            if sum(int(d) for d in s1) == sum(int(d) for d in s2):
                cnt = 0
                temp = list(s)
                temp[0] = s1[0]
                temp[1] = s1[1]
                temp[2] = s1[2]
                temp[3] = s2[0]
                temp[4] = s2[1]
                temp[5] = s2[2]
                for k in range(6):
                    if s[k] != temp[k]:
                        cnt+=1
                ans = min(ans,cnt)
    print(ans)

solve()