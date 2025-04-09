d, k, a, b, t = map(int, input().split())

if d <= k:
    print(d * a)
else:
    if a * k + t >= b * k:
        print(k * a + (d - k) * b)
    else:
        num_breaks = (d - 1) // k
        
        if num_breaks * k + k >= d:
            print(num_breaks * (a * k + t) + (d - num_breaks * k) * a)
        else:
            print(num_breaks * (a * k + t) + (d - num_breaks * k) * a)