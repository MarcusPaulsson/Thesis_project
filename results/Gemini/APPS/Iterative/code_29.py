s = input()
ans = 6
for sum1 in range(28):
    for sum2 in range(28):
        if sum1 == sum2:
            for i in range(1000):
                s1 = str(i).zfill(3)
                if sum(int(d) for d in s1) == sum1:
                    for j in range(1000):
                        s2 = str(j).zfill(3)
                        if sum(int(d) for d in s2) == sum2:
                            cnt = 0
                            for k in range(3):
                                if s[k] != s1[k]:
                                    cnt += 1
                            for k in range(3):
                                if s[k + 3] != s2[k]:
                                    cnt += 1
                            ans = min(ans, cnt)
print(ans)