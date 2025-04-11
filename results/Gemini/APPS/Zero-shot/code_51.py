def solve():
    n = int(input())
    divisors = list(map(int, input().split()))
    
    x = max(divisors)
    
    def get_divisors(num):
        divs = []
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divs.append(i)
                if i * i != num:
                    divs.append(num // i)
        return sorted(divs)

    divisors_x = get_divisors(x)
    
    temp_divisors = divisors[:]
    
    for val in divisors_x:
        if val in temp_divisors:
            temp_divisors.remove(val)
        else:
            break
    else:
        if not temp_divisors:
            print(x, x)
            return
            
        y = max(temp_divisors)
        
        divisors_y = get_divisors(y)
        
        combined_divisors = sorted(divisors_x + divisors_y)
        divisors.sort()
    
        if combined_divisors == divisors:
            print(x, y)
            return
        
    divisors.sort()
    
    x = max(divisors)
    divisors_x = get_divisors(x)
    temp_divisors = divisors[:]
    
    for val in divisors_x:
        if val in temp_divisors:
            temp_divisors.remove(val)
        else:
            break
    
    y = max(temp_divisors)
    divisors_y = get_divisors(y)

    print(x,y)

solve()