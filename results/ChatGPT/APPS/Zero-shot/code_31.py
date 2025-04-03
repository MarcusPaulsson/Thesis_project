def mod_inv(a, p):
    return pow(a, p - 2, p)

def birthday_paradox(n, k):
    MOD = 10**6 + 3
    days = 1 << n  # 2^n
    
    if k > days:
        return 1, 1  # Guaranteed at least two people share a birthday
    
    # P(no shared birthday) = days / days * (days - 1) / days * ... * (days - k + 1) / days
    numerator = days
    denominator = 1
    
    for i in range(1, k):
        numerator *= (days - i)
        denominator *= days
        numerator %= MOD
        denominator %= MOD
    
    # P(at least one shared birthday) = 1 - P(no shared birthday)
    A = (denominator - numerator + MOD) % MOD
    B = denominator
    
    # Reduce A and B
    gcd_ab = gcd(A, B)
    A //= gcd_ab
    B //= gcd_ab
    
    return A, B

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

if __name__ == "__main__":
    n, k = map(int, input().split())
    A, B = birthday_paradox(n, k)
    print(A, B)