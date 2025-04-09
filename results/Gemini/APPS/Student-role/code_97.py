def solve():
    n = int(input())
    x = list(map(int, input().split()))
    
    ans = float('inf')
    for target in set(x):
        cost = 0
        for val in x:
            cost += abs(val - target) % 2
        ans = min(ans, cost)
        
    print(ans)

solve()