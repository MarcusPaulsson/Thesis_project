def solve():
    n, pos, l, r = map(int, input().split())
    
    ans = 0
    
    if l == 1 and r == n:
        print(0)
        return
    
    if l == 1:
        ans = abs(pos - r) + 1
    elif r == n:
        ans = abs(pos - l) + 1
    else:
        ans = min(abs(pos - l) + abs(r - l) + 2, abs(pos - r) + abs(r - l) + 2)
    
    print(ans)

solve()