def solve():
    d, k, a, b, t = map(int, input().split())

    if d <= k:
        print(d * a)
        return

    cost_all_car = k * a + t + (d - k) * b
    cost_all_walk = d * a

    if a * k + t >= b * k:
        print(k * a + (d - k) * b)
        return

    num_breaks = d // k
    remaining_dist = d % k

    cost = num_breaks * (k * a + t)

    if remaining_dist > 0:
        cost += min(remaining_dist * a, remaining_dist * b + t)

    print(cost)


solve()