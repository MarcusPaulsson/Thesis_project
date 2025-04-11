s = input()
ans = 6
for i in range(1000):
    x = str(i).zfill(3)
    for j in range(1000):
        y = str(j).zfill(3)
        if sum(map(int, x)) == sum(map(int, y)):
            cnt = 0
            for k in range(3):
                if s[k] != x[k]:
                    cnt += 1
            for k in range(3):
                if s[k + 3] != y[k]:
                    cnt += 1
            ans = min(ans, cnt)
print(ans)