def solve():
    d, k, a, b, t = map(int, input().split())

    if d <= k:
        print(d * a)
        return

    time = k * a
    remaining_distance = d - k

    if t + k * a < k * b:
        num_breaks = remaining_distance // k
        time += num_breaks * (t + k * a)
        remaining_distance -= num_breaks * k

        if remaining_distance > 0:
            time += min(t + remaining_distance * a, remaining_distance * b)
    else:
        time += remaining_distance * b

    print(time)

solve()