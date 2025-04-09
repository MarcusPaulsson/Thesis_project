def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def birthday_probability(n, k):
    days = 1 << n  # 2^n
    if k > days:  # More people than days, guaranteed collision
        return (1, 1)
    
    total_ways = days ** k
    no_collision_ways = 1
    for i in range(k):
        no_collision_ways *= (days - i)
    
    A = total_ways - no_collision_ways
    B = total_ways
    
    # Reduce A and B
    common_gcd = gcd(A, B)
    A //= common_gcd
    B //= common_gcd
    
    # Return A and B modulo 1000003
    return A % 1000003, B % 1000003

# Read input
n, k = map(int, input().split())
result = birthday_probability(n, k)
print(result[0], result[1])