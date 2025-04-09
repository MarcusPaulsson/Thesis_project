def solve():
    m, x = map(int, input().split())
    
    if m == 2:
        print(2)
        return
    
    print(m - 1)

solve()