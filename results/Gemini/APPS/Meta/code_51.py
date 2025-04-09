def solve():
    n = int(input())
    divisors = list(map(int, input().split()))

    divisors.sort()
    x = divisors[-1]

    divisors_x = []
    for d in divisors:
        if x % d == 0:
            divisors_x.append(d)
    
    divisors_x.sort()
    
    remaining_divisors = []
    counts = {}
    for d in divisors:
        if d not in counts:
            counts[d] = 0
        counts[d] += 1
    
    for d in divisors_x:
        counts[d] -= 1
        
    for d in divisors:
        if counts[d] > 0:
            remaining_divisors.append(d)
            counts[d] -= 1
    
    if not remaining_divisors:
        y = 1
        divisors_y = [1]
    else:
        remaining_divisors.sort()
        y = remaining_divisors[-1]
        divisors_y = []
        for d in remaining_divisors:
            if y % d == 0:
                divisors_y.append(d)
        divisors_y.sort()
        
    print(x, y)

solve()