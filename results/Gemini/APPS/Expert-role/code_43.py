def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    min_time = float('inf')
    
    for i in range(1 << n):
        delivery_time = 0
        pickup_time = 0
        
        for j in range(n):
            if (i >> j) & 1:
                delivery_time = max(delivery_time, a[j])
            else:
                pickup_time += b[j]
        
        min_time = min(min_time, max(delivery_time, pickup_time))
    
    print(min_time)

t = int(input())
for _ in range(t):
    solve()