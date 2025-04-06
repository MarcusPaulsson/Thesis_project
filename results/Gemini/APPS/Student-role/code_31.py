def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if k > 2**n:
        print(1, 1)
        return
    
    num = 1
    den = 1
    
    twos_num = 0
    twos_den = 0
    
    days = pow(2, n, mod)
    
    for i in range(int(k)):
        if i == 0:
            continue
        
        val = (days - i) % mod
        num = (num * val) % mod
        
        twos_num += count_twos(days - i)
        
        den = (den * days) % mod
        twos_den += n

    
    common_twos = min(twos_num, twos_den)
    twos_num -= common_twos
    twos_den -= common_twos

    
    num = (num * pow(2, -twos_num, mod)) % mod
    den = (den * pow(2, -twos_den, mod)) % mod

    a = (den - num + mod) % mod
    b = den % mod
    
    print(a, b)

def count_twos(x):
    count = 0
    while x > 0 and x % 2 == 0:
        count += 1
        x //= 2
    return count

solve()