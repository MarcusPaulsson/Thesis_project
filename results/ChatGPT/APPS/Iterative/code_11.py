import math

def max_chocolates(n, a, b, p, q):
    count_red = n // a
    count_blue = n // b
    lcm_ab = a * (b // math.gcd(a, b))  # Calculate LCM using GCD
    count_both = n // lcm_ab
    
    # Calculate chocolates for both painting strategies
    chocolates_option_1 = (count_red - count_both) * p + count_blue * q
    chocolates_option_2 = count_red * p + (count_blue - count_both) * q
    
    return max(chocolates_option_1, chocolates_option_2)

n, a, b, p, q = map(int, input().split())
result = max_chocolates(n, a, b, p, q)
print(result)