def solve():
    d, k, a, b, t = map(int, input().split())

    if d <= k:
        print(d * a)
        return

    cost_only_driving = k * a + (d - k) * b
    cost_with_repairs = 0

    num_breaks = (d - 1) // k
    cost_with_repairs = k * a + num_breaks * t + (d - k) * a

    if t + k * a < k * b:
        cost_with_repairs = (d // k) * (k * a + t) + (d % k) * a if d % k != 0 else (d // k) * (k * a + t) - t
        cost_with_repairs = cost_with_repairs if d % k != 0 else cost_with_repairs + t if d == k else cost_with_repairs
        cost_with_repairs = (d // k) * (k * a + t) + (d % k) * a if d % k != 0 else (d // k -1) * (k * a + t) + k * a
        if d % k == 0 and d == k:
            cost_with_repairs = k * a
        elif d % k == 0 and d > k:
            cost_with_repairs = (d // k - 1) * t + (d // k) * (k * a)
        else:
            cost_with_repairs = (d // k) * (k * a + t) + (d % k) * a
    else:
        cost_with_repairs = k * a + (d - k) * b
    
    print(min(cost_only_driving, cost_with_repairs))

solve()