def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def solve():
    n = int(input())
    divisors = list(map(int, input().split()))
    divisors.sort()
    x = divisors[-1]
    
    divisors_x = get_divisors(x)
    
    divisors_copy = divisors[:]
    
    for val in divisors_x:
        if val in divisors_copy:
            divisors_copy.remove(val)
        else:
            y = divisors_copy[-1]
            print(x, y)
            return
    
    if len(divisors_copy) > 0:
        y = divisors_copy[-1]
    else:
        y = 1
        
    print(x, y)

solve()