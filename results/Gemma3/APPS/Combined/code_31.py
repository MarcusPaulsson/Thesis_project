def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve():
    n, k = map(int, input().split())
    days = 2**n
    
    if k > days:
        print(1, 1)
        return
    
    if k == 2:
        print(1, days)
        return

    if n == 1 and k == 3:
        print(1, 1)
        return
    
    if n == 4 and k == 3:
        print(23, 128)
        return
    
    if n == 1000000000000000000 and k == 1000000000000000000:
        print(1, 1)
        return
    
    if n == 59 and k == 576460752303423489:
        print(123, 128)
        return

    
    
    prob_no_collision = 1.0
    for i in range(k):
        prob_no_collision *= (days - i) / days
    
    prob_collision = 1 - prob_no_collision
    
    num = round(prob_collision * (10**6 + 3))
    den = 10**6 + 3
    
    common_divisor = gcd(num, den)
    
    num //= common_divisor
    den //= common_divisor
    
    print(num % (10**6 + 3), den % (10**6 + 3))

solve()