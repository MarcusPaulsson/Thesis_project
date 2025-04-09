def solve():
    n = int(input())
    divisors = list(map(int, input().split()))
    divisors.sort()
    x = divisors[-1]
    
    divisors_x = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            divisors_x.append(i)
            if i * i != x:
                divisors_x.append(x // i)
    divisors_x.sort()
    
    temp_divisors = divisors[:]
    
    for val in divisors_x:
        if val in temp_divisors:
            temp_divisors.remove(val)
        else:
            break
    else:
        print(x, x)
        return
    
    y = divisors[-1]
    
    counts = {}
    for d in divisors:
        counts[d] = counts.get(d, 0) + 1
        
    divisors_x = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            divisors_x.append(i)
            if i * i != x:
                divisors_x.append(x // i)
    divisors_x.sort()
    
    for d in divisors_x:
        counts[d] -= 1

    divisors_y = []
    y = divisors[-1] if len(divisors) > 0 else 1
    
    candidates = []
    for d in divisors:
        if counts[d] > 0:
            candidates.append(d)
    
    if not candidates:
        print(x, x)
        return

    y = candidates[-1]
    
    print(x,y)
    

solve()