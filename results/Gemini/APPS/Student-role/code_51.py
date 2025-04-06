def solve():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    x = d[-1]
    
    divisors_x = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            divisors_x.append(i)
            if i * i != x:
                divisors_x.append(x // i)
    divisors_x.sort()
    
    counts = {}
    for val in d:
        counts[val] = counts.get(val, 0) + 1
    
    for val in divisors_x:
        counts[val] = counts.get(val, 0) - 1
    
    remaining_divisors = []
    for val in counts:
        for _ in range(counts[val]):
            remaining_divisors.append(val)
            
    remaining_divisors.sort()
    
    if not remaining_divisors:
        print(x, x)
        return

    y = remaining_divisors[-1]
    
    print(x, y)

solve()