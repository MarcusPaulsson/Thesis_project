def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n < 63 and k > (1 << n):
        print(1, 1)
        return

    if k > mod:
        print(0, 1)
        return

    numerator = 1
    denominator = 1
    power_of_2 = 0

    for i in range(k):
        if i == 0:
            continue
        numerator = (numerator * (pow(2, n, mod) - i + mod)) % mod
        
        power_of_2 += count_factors(i)

    denominator = pow(pow(2, n, mod), k - 1, mod) % mod
    
    power_of_2_denominator = 0
    if n < 63:
      power_of_2_denominator = n * (k-1)
    else:
      power_of_2_denominator = 10**18

    gcd_power_of_2 = min(power_of_2, power_of_2_denominator)
    
    
    num_div_2 = 0
    temp_num = numerator
    
    
    den_div_2 = 0
    temp_den = denominator
    
    
    if gcd_power_of_2 > 0 and gcd_power_of_2 < 100:
      
      for _ in range(gcd_power_of_2):
        temp_num = temp_num * pow(2, mod - 2, mod) % mod
        temp_den = temp_den * pow(2, mod - 2, mod) % mod

    
    
    
    numerator = numerator * pow(pow(2, gcd_power_of_2, mod), mod-2, mod) % mod
    denominator = denominator * pow(pow(2, gcd_power_of_2, mod), mod-2, mod) % mod
    

    a = (denominator - numerator + mod) % mod
    b = denominator

    print(a, b)

def count_factors(x):
    count = 0
    while x > 0 and x % 2 == 0:
        count += 1
        x //= 2
    return count

solve()