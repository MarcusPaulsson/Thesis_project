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
    
    temp_d = d[:]
    
    for val in divisors_x:
        if val in temp_d:
            temp_d.remove(val)
    
    if not temp_d:
        print(x, x)
        return
    
    y = temp_d[-1]
    
    print(x, y)
    
solve()