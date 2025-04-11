def solve():
    n, pos, l, r = map(int, input().split())
    
    if l == 1 and r == n:
        print(0)
        return
    
    if l == 1:
        print(abs(pos - r) + 1)
        return
    
    if r == n:
        print(abs(pos - l) + 1)
        return
    
    
    ans1 = abs(pos - l) + 1 + abs(r - l) + 1
    ans2 = abs(pos - r) + 1 + abs(r - l) + 1
    
    print(min(ans1, ans2))


solve()