def solve():
    n = int(input())
    q = list(map(int, input().split()))
    
    def check(p):
        for i in range(n - 1):
            if p[i+1] - p[i] != q[i]:
                return False
        return True
    
    import itertools
    
    for p in itertools.permutations(range(1, n + 1)):
        if check(list(p)):
            print(*p)
            return
    
    print(-1)

solve()