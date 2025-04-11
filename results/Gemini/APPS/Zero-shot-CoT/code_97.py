def solve():
    n = int(input())
    x = list(map(int, input().split()))
    
    ans = float('inf')
    
    for target in range(1, 101):
        cost = 0
        for i in range(n):
            cost += abs(x[i] - target) % 2
        ans = min(ans, cost)
        
    print(ans)

solve()