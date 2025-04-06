def solve():
    n, pos, l, r = map(int, input().split())
    
    ans = 0
    
    if l == 1 and r == n:
        print(0)
        return
    
    if l == 1:
        ans = abs(pos - r) + 1
        print(ans)
        return
    
    if r == n:
        ans = abs(pos - l) + 1
        print(ans)
        return
    
    if pos <= l:
        ans = (l - pos) + 1 + (r - l) + 1
        print(ans)
        return
    
    if pos >= r:
        ans = (pos - r) + 1 + (r - l) + 1
        print(ans)
        return
        
    ans = min((pos - l) + 1 + (r - l) + 1, (r - pos) + 1 + (r - l) + 1)
    print(ans)

solve()