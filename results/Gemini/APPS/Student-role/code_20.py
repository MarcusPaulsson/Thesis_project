def solve():
    n, m = map(int, input().split())
    customers = []
    for _ in range(n):
        customers.append(list(map(int, input().split())))
    
    current_time = 0
    current_low = m
    current_high = m
    
    for t, l, h in customers:
        time_diff = t - current_time
        current_low -= time_diff
        current_high += time_diff
        
        if current_high < l or current_low > h:
            print("NO")
            return
        
        current_low = max(current_low, l)
        current_high = min(current_high, h)
        current_time = t
        
    print("YES")

q = int(input())
for _ in range(q):
    solve()