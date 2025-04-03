def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    min_time = float('inf')

    for i in range(1 << n):
        delivery_times = []
        pickup_times = 0
        
        for j in range(n):
            if (i >> j) & 1:
                delivery_times.append(a[j])
            else:
                pickup_times += b[j]
        
        max_delivery_time = 0
        if delivery_times:
            max_delivery_time = max(delivery_times)
        
        min_time = min(min_time, max(max_delivery_time, pickup_times))

    print(min_time)

t = int(input())
for _ in range(t):
    solve()