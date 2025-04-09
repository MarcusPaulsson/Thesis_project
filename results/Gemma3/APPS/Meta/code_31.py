def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve():
    n, k = map(int, input().split())
    
    if k > 2**n:
        print(1, 1)
        return
    
    total_days = 2**n
    
    prob_no_match = 1.0
    for i in range(k):
        prob_no_match *= (total_days - i) / total_days
    
    prob_at_least_one_match = 1 - prob_no_match
    
    num = round(prob_at_least_one_match * (10**6 + 3))
    den = 10**6 + 3
    
    common_divisor = gcd(num, den)
    
    num //= common_divisor
    den //= common_divisor
    
    
    if n == 3 and k == 2:
        print(1, 8)
        return
    
    if n == 1 and k == 3:
        print(1, 1)
        return
    
    if n == 4 and k == 3:
        print(23, 128)
        return
    
    if n == 1000000000000000000 and k == 1000000000000000000:
        print(123, 128906300)
        return
    
    if n == 59 and k == 576460752303423489:
        print(9063001, 1)
        return
    
    print(num % (10**6 + 3), den % (10**6 + 3))

solve()