def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    pos_1 = a.index(1)
    pos_n = a.index(n)
    
    ans = max(pos_1, pos_n, n - 1 - pos_1, n - 1 - pos_n)
    
    print(ans)
    
solve()