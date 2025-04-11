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
    
    ans = min(abs(pos - l) + abs(r - l) + 2, abs(pos - r) + abs(r - l) + 2)
    print(ans)

solve()