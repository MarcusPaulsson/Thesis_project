def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    instability1 = a[n-2] - a[0]
    instability2 = a[n-1] - a[1]
    
    print(min(instability1, instability2))

solve()