n, pos, l, r = map(int, input().split())

ans = 0

if l == 1 and r == n:
    print(0)
elif l == 1:
    ans = abs(pos - r) + 1
    print(ans)
elif r == n:
    ans = abs(pos - l) + 1
    print(ans)
else:
    ans = min(abs(pos - l), abs(pos - r)) + (r - l) + 2
    print(ans)