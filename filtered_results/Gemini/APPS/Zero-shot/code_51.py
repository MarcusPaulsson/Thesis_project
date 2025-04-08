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
    
    remaining_divisors = divisors[:]
    
    for dx in divisors_x:
        if dx in remaining_divisors:
            remaining_divisors.remove(dx)
        else:
            pass
            
    
    y = 1
    if remaining_divisors:
        y = remaining_divisors[-1]
    
    print(x, y)

solve()