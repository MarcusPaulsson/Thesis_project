def solve():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    x = d[-1]
    
    divisors_x = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            divisors_x.append(i)
            if i != x // i:
                divisors_x.append(x // i)
    divisors_x.sort()
    
    temp_d = d[:]
    for val in divisors_x:
        if val in temp_d:
            temp_d.remove(val)
        else:
            pass
            
    y = 1
    if len(temp_d) > 0:
        y = temp_d[-1]
    else:
        y = 1
        
    divisors_y = []
    for i in range(1, int(y**0.5) + 1):
        if y % i == 0:
            divisors_y.append(i)
            if i != y // i:
                divisors_y.append(y // i)
    divisors_y.sort()
    
    all_divisors = divisors_x + divisors_y
    all_divisors.sort()
    d.sort()
    
    if all_divisors == d:
        print(x, y)
    else:
        print(x, y)

solve()