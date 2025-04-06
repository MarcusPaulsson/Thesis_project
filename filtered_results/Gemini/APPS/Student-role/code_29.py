s = input()
a = [int(c) for c in s]
ans = 6
for i in range(1000):
    s1 = str(i).zfill(3)
    for j in range(1000):
        s2 = str(j).zfill(3)
        if sum(int(c) for c in s1) == sum(int(c) for c in s2):
            cnt = 0
            t = [int(c) for c in s1 + s2]
            for k in range(6):
                if a[k] != t[k]:
                    cnt += 1
            ans = min(ans, cnt)
print(ans)