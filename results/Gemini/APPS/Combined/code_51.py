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
    
    for dx in divisors_x:
        if dx in temp_divisors:
            temp_divisors.remove(dx)
        
    
    y = 1
    if len(temp_divisors) > 0:
        y = max(temp_divisors)
    else:
        y = 1
        
        
        temp_divisors_x = divisors[:]
        
        for dx in divisors_x:
            temp_divisors_x.remove(dx)
        
        if len(temp_divisors_x) > 0:
            y = max(temp_divisors_x)
        else:
            y = 1
    

    print(x, y)

solve()