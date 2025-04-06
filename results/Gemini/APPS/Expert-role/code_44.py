d, k, a, b, t = map(int, input().split())

if d <= k:
    print(d * a)
else:
    ans = k * a
    d -= k
    if a * k + t >= b * k:
        ans += d * b
    else:
        num_breaks = d // k
        ans += num_breaks * (a * k + t)
        d %= k
        if d > 0:
            ans += min(d * a + t, d * b)
    print(ans)