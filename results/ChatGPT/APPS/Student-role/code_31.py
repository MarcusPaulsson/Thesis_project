def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, p):
    return pow(a, p - 2, p)

def birthday_paradox(n, k):
    mod = 10**6 + 3
    days = 2 ** n

    if k > days:
        return (1, 1)

    numerator = 1
    denominator = 1

    for i in range(k):
        numerator *= (days - i) % mod
        denominator *= days % mod
        numerator %= mod
        denominator %= mod

    numerator = (denominator - numerator) % mod
    denominator = denominator % mod

    common_gcd = gcd(numerator, denominator)
    numerator //= common_gcd
    denominator //= common_gcd

    return (numerator, denominator)

if __name__ == "__main__":
    n, k = map(int, input().split())
    A, B = birthday_paradox(n, k)
    print(A, B)