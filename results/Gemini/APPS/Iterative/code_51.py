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
    
    divisors_copy = divisors[:]
    
    for dx in divisors_x:
        if dx in divisors_copy:
            divisors_copy.remove(dx)
            
    y = 1
    if divisors_copy:
        y = divisors_copy[-1]
    else:
        y = 1
        
    print(x, y)

solve()